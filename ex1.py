count = 0
while True:
    print('Choose option')
    inp = input("Valid options is 1 and 2\n")
    if inp == '1':
        num = int(input("Enter Number\n"))
        count += 1
        continue
    elif inp == '2':
        print(f"count is {count}")
        break
    else:
        print('invalid option')
        continue
