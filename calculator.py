#Python calculator
print("💀⚠️ you can only compute two numbers at a time")

operator = input("Enter an operator (+ , -, *, /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

answer = 0

if operator  == "+":
    answer = num1 + num2
elif operator == "-":
    if num1 > num2:
        answer = num1 - num2
    elif num2 > num1:
        answer = num2 - num1
elif operator == "/":
    answer = num1/num2
elif operator == "*":
    answer = num1*num2
elif operator == "%":
    answer = num1 % num2

if num1>num2:
    print(f'{num1} {operator} {num2} = {answer} ‍🔬')
elif num2>num1:
    print(f'{num2} {operator} {num1} = {answer} ‍🔬')


