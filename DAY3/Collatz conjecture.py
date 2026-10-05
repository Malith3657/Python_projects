

num = int(input("Enter number -"))

if num < 1:
    print("please Enter a valid positive integer")
    exit()

steps = 0

while num !=1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3)+ 1

    steps += 1

print(f"no of steps taken {steps}")

