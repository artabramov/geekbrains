import random

numbers, numbers_stats = [], {}
for i in range(0, 100):
    numbers.append(random.randint(0, 100))

print(numbers)

for i in numbers:
    if i in numbers_stats:
        numbers_stats[i] += 1
    else:
        numbers_stats[i] = 1

key_max, value_max = 0, 0
for key, value in enumerate(numbers_stats):
    if value > value_max:
        key_max, value_max = key, value

print(key_max)
