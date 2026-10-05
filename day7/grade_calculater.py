def grade_cal(grade=0 ):
    if grade >= 75:
        return "A"
    elif grade >= 65:
        return "B"
    elif grade >= 55:
        return "C"
    elif grade >= 35:
        return "S"
    else:
        return "Fail"

while True:

    marks = int(input("Enter your Marks:-"))

    print(grade_cal(marks))
