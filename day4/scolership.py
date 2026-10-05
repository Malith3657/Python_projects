average = int(input("\nEnter Average :"))
attendent = int(input("\nEnter Attendent:"))
income = int(input("\nEnter Income :"))
achivement= (input("\nDo yo have Achivement (yes/no) :"))


if average > 75 and attendent > 75 and income > 100000 or achivement:
    if average > 90:
        print("\nyou got 100% scolership")
    elif average > 80:
        print("\nyou got 75% scolership")
    else:
        print("\nothers got 50%")

else:
    print("\nsorry. unsuccsesful")