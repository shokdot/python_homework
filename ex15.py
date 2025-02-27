try:
    string = input("Write numbers! \n").split()
    sum = 0
    for i in string:
        sum += int(i)
    print(sum)
except:
    print("Some error")
