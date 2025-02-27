def prt_num(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

while True:
    try:
        n_th = int(input("Input number from 1 to 10\n"))
        if n_th == 0:
            break
        prt_num(n_th)
    except ValueError:
        print("Please input valid number")
