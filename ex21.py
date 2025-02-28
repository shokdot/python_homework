def is_armstrong(num):
    sum = 0
    num_str = str(num)
    dig_len = len(num_str)
    for i in num_str:
        sum += int(i) ** dig_len
    return sum == num



try:
    num = int(input("Enter number: "))
    if is_armstrong(num):
        print(f"{num} is armstrong number")
    else:
        print(f"{num} isn't armstrong number")
except:
    print("Error")
