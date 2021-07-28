a = int(input('input the 3-digits number: '))
if a < 100 or a > 999:
    raise ValueError('Value error.')

b = []
for i in range(0,3):
    c = a % 10
    a = (a - c) // 10
    b.append(c)

sum, mul = 0, 1
for i in b:
    sum += i
    mul *= i

print(f'numbers sum: {sum}, numbers mul: {mul}')
