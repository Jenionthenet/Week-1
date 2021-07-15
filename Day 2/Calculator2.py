first_numb = int(input("Enter the first number: "))
operation = input("Enter the mathematical operation: ")
second_numb = int(input("Enter the second number: "))

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x/y

def calculate(a, operand, b):
    if operation == "+":
        return addition(a, b)
    elif operation == "-":
        return subtraction(a, b)
    elif operation == "*":
        return multiplication(a, b)
    else:
        return division(a, b)

answer = calculate(first_numb, operation, second_numb)
print(answer)
