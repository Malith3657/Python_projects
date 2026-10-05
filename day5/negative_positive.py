list1 = [-1, 2, -5, 10, -9, -6, 7, 12]

print("\nPositive Numbers")

for i in range(len(list1)):
    if list1[i] > 0:
        print(f"\n{list1[i]}")

print("\nNegative Numbers")

for i in range(len(list1)):
    if list1[i] < 0:
        print(f"\n{list1[i]}")