science = int(input("Enter Science Marks :"))
maths = int(input("Enter Maths Marks :"))
it = int(input("Enter It Marks :"))
english = int(input("Enter English Marks :"))

total = maths + science + it + english
avg = total / 4
grade = 0

if avg >= 75:
    grade = "A"
elif avg >= 65:
    grade = "B"
elif avg >= 55:
    grade = "C"
elif avg >= 35:
    grade = "S"
else:
    grade = "W"

print("\n==================" )
print(f"ypur total is {total}")
print(f"your avg is {avg}")
print("*******************")
print(f"your final grade is {grade}")
print("\n====================")