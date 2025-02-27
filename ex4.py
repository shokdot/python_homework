import random
num = random.randint(1,10)
count = 1
while True:
    try:
        user_num = int(input("Predict number from 1 to 10\n"))
    except ValueError:
        print("Please use valid number")
        continue
    if user_num == num:
        print("You are right")
        print(f"Atempts == {count}")
        break
    elif user_num > num:
        print("Too high!")
        count += 1
        continue
    elif user_num < num:
        print("Too low!")
        count += 1
        continue
    
