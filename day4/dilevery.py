value = int(input("How much is your product :"))
member = input("Are you member (yes / no) :")


if value >= 5000 and member == "yes":
    print("free delivery")
else:
    print("Add delivery fee")