def factorial(n):
    if type(n) != int or n < 0:
        print("Error")
        return 0
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial('fadfadf'))

