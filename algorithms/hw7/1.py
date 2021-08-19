import random

numbers = []
for i in range(0, 100):
    numbers.append(random.randint(-100, 101))

print(numbers)

for i in range(0, 99):
    for j in range(0, 99):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
