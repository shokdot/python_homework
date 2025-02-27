print("Hello samiy krutoy hashvich v mire")
while True:
    opcode = input("Please enter operation +,-,*,/, 5 for exit\n")
    if opcode == '5':
        print("paka")
        break
    elif opcode == '+':
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(f"{num1} + {num2} = {num1 + num2}")
            continue
        except ValueError:
            print("Please enter valid number")
            continue
    elif opcode == '-':
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(f"{num1} - {num2} = {num1 - num2}")
            continue
        except ValueError:
            print("Please enter valid number")
            continue
    elif opcode == '*':
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(f"{num1} * {num2} = {num1 * num2}")
            continue
        except:
            print("Please enter valid number")
    elif opcode == '/':
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if num2 == 0:
                print("division by zero")
                continue
            print(f"{num1} / {num2} = {num1 / num2}")
            continue
        except ValueError:
            print("Please enter valid number")
    else:
        print("Wrong operation")
        continue
