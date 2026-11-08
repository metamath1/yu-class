import ast
import datetime
import json
import operator
import os
import re
import time
from http.client import HTTPException, HTTPSConnection
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types


BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def get_current_time(location: str) -> str:
    """특정 지역의 현재 시간을 반환합니다."""
    return f"{location}의 현재 시간은 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 입니다."


def evaluate_number(node):
    if isinstance(node, ast.Constant):
        value = node.value
    elif isinstance(node, ast.UnaryOp):
        value = UNARY_OPERATORS[type(node.op)](evaluate_number(node.operand))
    elif isinstance(node, ast.BinOp):
        left = evaluate_number(node.left)
        right = evaluate_number(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("지수 범위 초과")
        value = BINARY_OPERATORS[type(node.op)](left, right)
    else:
        raise ValueError("숫자와 산술 연산만 허용")
    if type(value) not in (int, float) or not abs(value) <= 10**100:
        raise ValueError("실수 범위 초과")
    return value


def calculate_math(expression: str) -> str:
    """수학 수식을 계산하여 결과를 반환합니다."""
    if len(expression) > 200:
        return "계산 오류: 수식 길이 초과"
    try:
        tree = ast.parse(expression.strip(), mode="eval")
        return str(evaluate_number(tree.body))
    except (ArithmeticError, KeyError, SyntaxError, ValueError):
        return "계산 오류: 숫자와 허용된 산술 연산으로 이뤄진 수식을 입력하세요."


def answer(chat, question: str) -> str:
    response = chat.send_message(question)
    tools = {"get_current_time": get_current_time, "calculate_math": calculate_math}
    for _ in range(4):
        if not response.function_calls:
            break
        parts = []
        for call in response.function_calls:
            args = call.args or {}
            print(f"[함수 요청] {call.name} {args!r}", flush=True)
            try:
                result = tools[call.name](**args)
            except (KeyError, TypeError):
                result = "도구 실행 오류: 도구 이름과 인수를 확인하세요."
            print(f"[실행 결과 → Gemini] {result!r}", flush=True)
            part = types.Part.from_function_response(name=call.name, response={"result": result})
            part.function_response.id = call.id
            parts.append(part)
        response = chat.send_message(parts)
    if response.function_calls:
        raise RuntimeError("도구 호출 횟수 제한")
    text = response.text
    if not text or not text.strip():
        raise RuntimeError("Gemini 응답이 비어 있습니다.")
    print(f"[Gemini 최종 응답] {text!r}", flush=True)
    return text


def telegram(token: str, method: str, payload: dict, timeout: int):
    connection = HTTPSConnection("api.telegram.org", timeout=timeout)
    try:
        connection.request(
            "POST", f"/bot{token}/{method}", json.dumps(payload).encode("utf-8"),
            {"Content-Type": "application/json"},
        )
        with connection.getresponse() as response:
            if response.status != 200:
                raise RuntimeError(f"{method} HTTP {response.status}")
            data = json.load(response)
            if not data.get("ok"):
                raise RuntimeError(f"{method} API 요청 실패")
            return data["result"]
    finally:
        connection.close()


def dm_text(update: dict, chat_id: int) -> str | None:
    message = update.get("message", {})
    chat = message.get("chat", {})
    text = message.get("text")
    if chat.get("id") == chat_id and chat.get("type") == "private" and text and text.strip():
        return text
    return None


def poll(token: str, chat_id: int, chat) -> None:
    offset = 0
    poll_timeout = 0
    while True:
        try:
            updates = telegram(token, "getUpdates", {
                "offset": offset, "timeout": poll_timeout, "allowed_updates": ["message"],
            }, timeout=poll_timeout + 8)
        except (OSError, HTTPException) as error:
            print(f"[Telegram 연결 실패] {type(error).__name__}. 잠시 후 다시 연결합니다.", flush=True)
            time.sleep(3)
            continue
        if poll_timeout == 0:
            print("[Telegram getUpdates 성공] 복시리 대기 중 (Ctrl+C 종료)", flush=True)
            poll_timeout = 20
        for update in updates:
            offset = update["update_id"] + 1
            question = dm_text(update, chat_id)
            if question is None:
                continue
            print("[Telegram DM 수신]", flush=True)
            try:
                text = answer(chat, question)
            except Exception as error:
                print(f"[Gemini 처리 실패] {type(error).__name__}", flush=True)
                text = "답변 중 문제가 생겼어요. 잠시 후 다시 질문해 주세요."
            try:
                for start in range(0, len(text), 2000):
                    telegram(token, "sendMessage", {
                        "chat_id": chat_id, "text": text[start:start + 2000],
                    }, timeout=10)
                    print("[Telegram sendMessage 성공]", flush=True)
            except (OSError, HTTPException, RuntimeError, ValueError) as error:
                print(f"[Telegram 전송 실패] {type(error).__name__}", flush=True)


def load_settings() -> None:
    folder = Path(__file__).resolve().parent
    parent = folder.parent
    if folder.name == "telegram_demo" and parent.name == "agent0" and (parent / "agent.py").is_file():
        load_dotenv(parent / ".env")
    load_dotenv(folder / ".env")


def main():
    load_settings()
    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
    if not re.fullmatch(r"[0-9]+:[A-Za-z0-9_-]+", token) or not re.fullmatch(r"[0-9]+", chat_id):
        raise SystemExit("TELEGRAM_BOT_TOKEN과 개인 대화방의 숫자 TELEGRAM_CHAT_ID를 설정하세요.")
    client = genai.Client(http_options=types.HttpOptions(
        timeout=20_000, retry_options=types.HttpRetryOptions(attempts=1),
    ))
    chat = client.chats.create(
        model="gemini-3.8-flash",
        config=types.GenerateContentConfig(
            tools=[get_current_time, calculate_math],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        ),
    )
    try:
        poll(token, int(chat_id), chat)
    except KeyboardInterrupt:
        print("\n복시리 종료")
    except RuntimeError as error:
        raise SystemExit(f"[Telegram 폴링 종료] {error}") from None


if __name__ == "__main__":
    main()
