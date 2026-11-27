def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

if __name__ == "__main__":
    print("Multiply:", calculate(10, 5, '*'))
    print("Divide:", calculate(10, 5, '/'))
