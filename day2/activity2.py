ticket = 1000

user_height = float(input("Enter your height"))

if user_height > 1.2:
    user_age = int(input("your age"))
    if user_age < 18:
        print(f"your ticket price - {1000 - ticket * 20/100} ")
    elif user_age > 55:
        print(f"your ticket price - {1000 - ticket * 50/100}")
    else:
        print("your ticket price - 1000")

else:
    print("you are not entered")