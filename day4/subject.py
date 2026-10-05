maths = int(input("Enter Maths Marks :")) >65
science = int(input("Enter Science Marks :")) >65
English = int(input("Enter English Marks :")) >65
Ict = int(input("Enter Ict Marks :")) >65


if maths and science and English or Ict:
    print("\nyou can do degree")
else:
    print("You can't do degree")