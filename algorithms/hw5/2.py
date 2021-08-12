base = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
rebase = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

tmp_1 = input('first number: ').lower()
tmp_2 = input('second number: ').lower()

x = [i for i in tmp_1]
y = [i for i in tmp_2]

length = len(x) if len(x) > len(y) else len(y)

# Сложение. Полностью нативная реализация, должна работать на системах счисления
# с любым основанием (задается в первоначальных настройках).

xy_sum = []
sum_over = 0
for i in range(0, length):

    m = x[::-1][i] if i < len(x) else '0'
    n = y[::-1][i] if i < len(y) else '0'
    mn_sum = base[m] + base[n] + sum_over

    if mn_sum > len(base):
        mn_sum -= len(base)
        sum_over = 1
    else:
        sum_over = 0

    xy_sum.append(rebase[mn_sum])

print(x, '+', y, '=', xy_sum[::-1])

# Умножение. Тут был выбор: делать нативно и долго или немного схитрить и воспользоваться какой-либо встроенной
# функцией. К сожалению, на первый вариант времени было недостатьчно и я использовал функцию hex()

x_dec, j = 0, 1
for i in x[::-1]:
    x_dec = x_dec + base[i] * j
    j *= len(base)

y_dec, j = 0, 1
for i in y[::-1]:
    y_dec = y_dec + base[i] * j
    j *= len(base)

xy_mul = x_dec * y_dec

print(x, '*', y, '=', [i for i in hex(x_dec * y_dec)[2:]])





