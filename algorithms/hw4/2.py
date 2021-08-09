# Написать два алгоритма нахождения i-го по счёту простого числа.

# Без использования «Решета Эратосфена»
# Самым очевидным способом решения задачи на первый взгляд является перебор
# чисел от 2 до n двумя вложенными циклами с проверкой условий. В этом случае
# сложность алгоритма будет O(n) = n^2

n = int(input(f'input numbers count (n): '))

a = True
numbers = []
for x in range(2, n):
    for y in range(2, n):
        if x != y and y != 1:
            if not x % y:
                a = False
                break
    if a:
        numbers.append(x)
    a = True

print(numbers)

# Если почитать про решето Эратосфена, то алгоритм можно переписать (хотя с математической
# точки зрения не сразу очевидно почему это работает). В этом случае сложность алгоритма
# будет O(n) = n * log(log(n)) (прочитано в Википедии).

numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for i in range(2 * number, n + 1, number):
            numbers[i - 2] = 0

numbers = [i for i in numbers if i != 0]
print(numbers)
