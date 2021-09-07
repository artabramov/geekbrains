import random

numbers = []
for i in range(0, 10):
    numbers.append(random.randint(0, 100))

print(numbers)

min_1, min_2 = 100, 100
for i in numbers:
    if i < min_1:
        min_1 = i

    if min_1 < min_2:
        min_2, min_1 = min_1, min_2

print(min_1, min_2)
