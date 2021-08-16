# Подсчитать, сколько было выделено памяти под переменные 
# в ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить программы 
# с наиболее эффективным использованием памяти.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Для определения используемой памяти возьмем два варианта алгоритма
# для решения задачи: "Определить, какое число в массиве встречается чаще всего."

from memory_profiler import profile
import random

# Первый вариант:

# @profile
# def my_func():
#     numbers, numbers_stats = [], {}
#     for i in range(0, 100):
#         numbers.append(random.randint(0, 100))
# 
#     print(numbers)
# 
#     for i in numbers:
#         if i in numbers_stats:
#             numbers_stats[i] += 1
#         else:
#             numbers_stats[i] = 1
# 
#     key_max, value_max = 0, 0
#     for key, value in enumerate(numbers_stats):
#         if value > value_max:
#             key_max, value_max = key, value
# 
#     print(key_max)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12   18.934 MiB   18.934 MiB           1   @profile
#     13                                         def my_func():
#     14   18.934 MiB    0.000 MiB           1       numbers, numbers_stats = [], {}
#     15   18.934 MiB    0.000 MiB         101       for i in range(0, 100):
#     16   18.934 MiB    0.000 MiB         100           numbers.append(random.randint(0, 100))
#     17
#     18   18.934 MiB    0.000 MiB           1       print(numbers)
#     19
#     20   18.934 MiB    0.000 MiB         101       for i in numbers:
#     21   18.934 MiB    0.000 MiB         100           if i in numbers_stats:
#     22   18.934 MiB    0.000 MiB          32               numbers_stats[i] += 1
#     23                                                 else:
#     24   18.934 MiB    0.000 MiB          68               numbers_stats[i] = 1
#     25
#     26   18.934 MiB    0.000 MiB           1       key_max, value_max = 0, 0
#     27   18.934 MiB    0.000 MiB          69       for key, value in enumerate(numbers_stats):
#     28   18.934 MiB    0.000 MiB          68           if value > value_max:
#     29   18.934 MiB    0.000 MiB           6               key_max, value_max = key, value
#     30
#     31   18.934 MiB    0.000 MiB           1       print(key_max)

# Второй вариант:

@profile
def my_func():
    numbers, numbers_stats = [], {}
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

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     67   18.801 MiB   18.801 MiB           1   @profile
#     68                                         def my_func():
#     69   18.801 MiB    0.000 MiB           1       numbers, numbers_stats = [], {}
#     70   18.801 MiB    0.000 MiB           1       for i in numbers:
#     71                                                 number_count = 0
#     72                                                 for j in numbers:
#     73                                                     if i == j:
#     74                                                         number_count += 1
#     75                                                 numbers_stats[i] = number_count
#     76
#     77   18.801 MiB    0.000 MiB           1       key_max, value_max = 0, 0
#     78   18.801 MiB    0.000 MiB           1       for key, value in enumerate(numbers_stats):
#     79                                                 if value > value_max:
#     80                                                     key_max, value_max = key, value
#     81
#     82   18.801 MiB    0.000 MiB           1       print(key_max)

if __name__ == '__main__':
    my_func()
