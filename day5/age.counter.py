age_list = [21, 17, 21, 23, 21, 21, 26, 20, 23, 13, 35, 50, 80, 70, 60, 38]

kids = 0
youth = 0
middle = 0
elder = 0

for i in range(len(age_list)):
    if age_list[i] <= 14:
        kids += 1
    elif age_list[i] >= 15 and age_list[i] <= 30:
        youth += 1
    elif age_list[i] >= 31 and age_list[i] <= 59:
        middle += 1
    elif age_list[i] > 60:
        elder += 1

print(f"\nKids = {kids}")
print(f"\nYouth = {youth}")
print(f"\nMiddle = {middle}")
print(f"\nElder = {elder}")

