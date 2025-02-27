def gcd(a, b):
    if a == 0:
        return b
    gcd(b % a, a)

try:
    a = int(input("Num 1: "))
    b = int(input("Num 2: "))
    print(f"GCD is {gcd(a,b)}")
except:
    print("Error")
