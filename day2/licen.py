age = int(input("Enter your age - "))
# licen = (input("Do you have licen- "))

if age < 18:
    has_a_licen = input("do you have licen :(yes/no)")

    if has_a_licen == "yes":

        drunk = input("Are you drink : (yes/no):")
        if drunk == "no":
            print("you are eligible to drive")
        else:
            print("you can't drive because of drunk")
    else:
        print("you are not eligible to drive because you haven't licen")

else:
    print("too young to drive")

#
#
# elif age >= 18:
#     print(f"you can drive")




