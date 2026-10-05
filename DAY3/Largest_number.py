#ask the user how many numbers they  want to enter,
#collect numbers and find the largest number among them


count = int(input("How many numbers = "))

largest = int(input("Enter your 1st number :" ))

for i in range (count-1):
    number = int(input(f"Enter {i+2} number :"))


    if number > largest :
        largest = number

print(f"Largest Number :{largest}")


