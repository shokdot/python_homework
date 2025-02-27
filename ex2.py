while True:
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print('Please valid number')
        continue
    if num == 0:
        print('exiting.')
        break
    elif num % 2 == 0:
        print('Number is even.')
    elif num % 2 != 0:
        print('Number is odd')
    continue
