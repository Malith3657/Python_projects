nums = [9,2,3,6,4,]

letters = ["A","B","S","M","H","C"]

letter_s = letters[1:5:2]

letter_reversed = letters[::-1]
print("reserved array -" , letter_reversed)

print(letter_s)

nums_2 = nums[:]

nums_3 = nums[0:3]

print(nums_3)

nums.append(20)

print(nums)
print(nums_2)