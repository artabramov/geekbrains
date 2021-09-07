import random

numbers = []
for i in range(0, 10):
    numbers.append(random.randint(0, 100))

print(numbers)

min_value, max_value = 100, 0
min_key, max_key = 0, 0
for key, value in enumerate(numbers):
    if value > max_value:
        max_key, max_value = key, value
    elif value < min_value:
        min_key, min_value = key, value

if min_key > max_key:
    min_key, max_key = max_key, min_key
    min_value, max_value = max_value, min_value

values_sum = 0
for i in range(min_key + 1, max_key):
    values_sum += numbers[i]

print(values_sum)