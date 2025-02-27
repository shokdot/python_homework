def count_digit(n):
    sum = 0
    while n != 0:
       sum += n % 10
       n = n // 10
    return sum

try:
    num = int(input("Input Number: "))
    print(count_digit(num))
except ValueError:
    print("Error")
