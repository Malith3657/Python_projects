numbers = [5, 6, 7, 4, 3, 2, 1, 9, 8, 10]

swapped = True

while swapped:
    swapped = False
    for i in  range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[i + 1], numbers[i]
            swapped = True

print(numbers)