import random
import sys

numbers = [float(x) for x in sys.argv[1:]]
result = numbers[0]
expression = str(numbers[0])

for number in numbers[1:]:
    op = random.choice(["+", "-", "*", "/"])

    if op == "+": result += number
    elif op == "-": result -= number
    elif op == "*": result *= number
    else: result /= number

    expression = f"({expression} {op} {number})"

print("Expression:", expression)
print("Result:", result)
print("🌀 chaos-calc skill executed")
