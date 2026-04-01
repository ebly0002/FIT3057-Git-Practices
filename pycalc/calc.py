def compute(expression: str):
    num0, operator, num1 = expression.split(" ")

    if operator == "+":
        return num0 + num1
    elif operator == "-":
        return num0 - num1
    else:
        print("Unknown operation!")
        return None