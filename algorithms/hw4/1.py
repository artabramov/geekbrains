# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# 4. Определить, какое число в массиве встречается чаще всего.

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

# Поскольку в вышеприведенной реализации алгоритма по одному разу перебирается
# первоначальный массив и массив с различными числами, то очевидно,
# что сложность вышеприведенного алгоритма O(n) = n + m,
# где n - размер первоначального массива, а m - количество различных числе в нем.
# Самый долгий вариант выполнения (когда все числа различные), будет O(n) = 2 * n

# Для решения этой задачи можно написать другой алгоритм:

numbers_stats = {}
for i in numbers:
    number_count = 0
    for j in numbers:
        if i == j:
            number_count += 1
    numbers_stats[i] = number_count

key_max, value_max = 0, 0
for key, value in enumerate(numbers_stats):
    if value > value_max:
        key_max, value_max = key, value

print(key_max)

# Второе решение дает идентичный результат, но в этом случае сложность алгоритма
# существенно возрастает и становится O(n) = n^2 + n
