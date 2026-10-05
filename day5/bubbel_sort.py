numbers = [90, 60, 80, 40, 30, 20, 10, 50, 100]
for m in range(len(numbers)):
    for i in range(len(numbers) -1 - m):

        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[ i + 1], numbers[i]

print(numbers)

