import random

numbers = []
for i in range(0, 100):
    numbers.append(random.randint(-100, 100))

print(numbers)

key_max, value_max = 0, -100
for key, value in enumerate(numbers):
    if 0 > value > value_max:
        key_max, value_max = key, value

print(value_max)