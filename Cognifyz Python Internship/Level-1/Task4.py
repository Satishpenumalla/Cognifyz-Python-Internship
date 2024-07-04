def calculator(a, b, operator):
    x = int(a)
    y = int(b)
    cal = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y,
        '%': x % y
    }
    return cal.get(operator, "Invalid operator")

x, y = input("Enter the two numbers: ").split()
operator = input("Enter the operator: ")

result = calculator(x, y, operator)
print(f"The result of {x} {operator} {y} is {result}")
