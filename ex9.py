from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Write number: "))
    if is_prime(num):
        print("Number is prime")
    else:
        print("Number isn't prime")
except ValueError:
    print("Input valid number")
