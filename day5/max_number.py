num_list = [10, 8, 5, 3, 2, 3,]

max_number = 0

for i in range(len(num_list)):
    if num_list[i] > max_number:
        max_number = num_list[i]
print(max_number)


print("\n=====Even numbers=====")

for num in num_list:
    if num % 2 == 0 :
        print(num)

print("=====================")

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        print(num_list[i])