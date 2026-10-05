numbers = []

for i in range(10):
    numbers.append(i)

nums = [i * 5 for i in range(10)]

print(nums)



hello = ["Hello" for i in range(10)]
print(hello)


even_numbers = [i for i in range(100) if i % 2 == 0]
print(even_numbers)

