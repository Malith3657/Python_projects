nums = [2,2,3,4,5,6,7,4,5]

unique_nums = []

for num in nums:

    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)