# 텔레그램 복시리 Agent 실행 안내

복시리는 지정한 1:1 대화방에서 받은 일반 텍스트를 Gemini에 보냅니다. Gemini가 함수를 요청하면 이 파일에 있는 시간·계산 함수를 Python으로 실행하고 결과를 Gemini에 돌려줍니다. 같은 프로세스가 실행되는 동안 대화 문맥이 이어집니다. PC가 Telegram과 Gemini에 HTTPS로 접속할 수 있으면 됩니다.

## Windows에서 설치

검증 환경은 Python 3.14.7, `google-genai 1.38.0`, `python-dotenv 1.1.0`입니다. 독립 배치에서는 압축을 푼 폴더에서 PowerShell을 열어 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

`python` 명령이 없으면 가상환경을 만드는 첫 줄에서 `py -3` 또는 설치한 `python.exe`의 전체 경로를 사용합니다.

이미 사용하는 Conda 환경이 있다면 해당 환경을 활성화하고 `python -m pip install -r requirements.txt`를 실행합니다. 아래 명령의 `.\.venv\Scripts\python.exe`도 `python`으로 바꿔 실행할 수 있습니다.

프로젝트 안에서 실행하면 `agent0/.env`에 아래 값을 설정합니다. 같은 이름의 값은 기존 환경 변수, `agent0/.env`, `agent_for_telegram.py` 옆 `.env` 순으로 적용합니다. 독립 배치에서는 기존 환경 변수와 `agent_for_telegram.py` 옆 `.env`를 사용합니다.

```dotenv
GEMINI_API_KEY=여기에_Gemini_API_키
TELEGRAM_BOT_TOKEN=여기에_BotFather_토큰
TELEGRAM_CHAT_ID=여기에_복시리와의_개인_대화방_ID
```

같은 복시리 대화방을 사용하면 데스크톱에서 확인한 대화방 ID를 노트북에도 사용합니다. ID를 다시 확인하려면 봇을 종료하고 복시리에게 확인용 메시지를 보낸 뒤, 같은 폴더의 PowerShell에서 아래 명령을 실행합니다. 이 명령은 로컬의 토큰으로 공식 Telegram API를 조회하고 개인 대화방 ID만 로컬 화면에 표시합니다. `TELEGRAM_CHAT_ID`에는 본인 대화방의 ID를 넣습니다.

```powershell
.\.venv\Scripts\python.exe -c "from os import environ; from agent_for_telegram import load_settings, telegram; load_settings(); print([u['message']['chat']['id'] for u in telegram(environ['TELEGRAM_BOT_TOKEN'], 'getUpdates', {'allowed_updates':['message']}, 10) if u.get('message', {}).get('chat', {}).get('type') == 'private'])"
```

## 시작과 종료

노트북에서 실행하기 전에 데스크톱의 복시리를 종료하고 노트북의 시간대가 한국 표준시인지 확인합니다.

```powershell
.\.venv\Scripts\python.exe -X utf8 agent_for_telegram.py
```

`복시리 대기 중`이 표시되면 휴대폰의 복시리 채팅방에 질문을 보냅니다. “현재 시간을 확인하고 오늘 자정까지 남은 초를 계산해줘”라고 보내면 콘솔에서 함수 요청과 실행 결과를 비교할 수 있습니다. 종료는 `Ctrl+C`입니다. 다른 작업 폴더에서 실행할 때는 Python 실행 파일과 `agent_for_telegram.py`의 경로를 지정하면 됩니다. `.env` 경로는 실행 파일의 위치를 기준으로 정합니다.

노트북에는 ZIP을 옮겨 새 가상환경을 만들고, 기존에 관리하던 키와 토큰으로 현지 설정을 준비합니다. Telegram이 HTTP 409를 반환하면 기존 복시리 실행이나 등록된 웹훅을 확인한 뒤 다시 실행합니다.
