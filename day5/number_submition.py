numbers = []

for number in range(1000):
    numbers.append(number)
print(numbers)

total = 0

for i in numbers:
    total = total + i

print(f"\ntotal - {total}")