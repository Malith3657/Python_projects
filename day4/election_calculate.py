age = int(input("Enter your age :"))
citizen = input("Are you Sri Lankan ? (yes/no)")

if age >= 18 and citizen == "yes":
    print("\nYou can vote for election")
else:
    print("\nyou can't vote this election")