cache = {0:0, 1:1}

def fib(n):
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

try:
    num = int(input("Enter n-th number\n"))
    for i in range(num+1):
        fib_n = fib(i)
        print(f"{fib_n}, ", end=' ')
    print('\n')
except ValueError:
    print("Invalid number, exit")
