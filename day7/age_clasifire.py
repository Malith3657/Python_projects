def classify_age(age = 0):
    if age < 13:
        return "Child"
    elif age < 19:
        return "Teenager"
    elif age < 50:
        return "Adult"
    else:
        return "senior citizen"

print(classify_age(51))