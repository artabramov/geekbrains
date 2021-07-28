x1, y1 = float(input('input X1: ')), float(input('input Y1: '))
x2, y2 = float(input('input X2: ')), float(input('input Y2: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

if b >= 0:
    sign = '+'
else:
    sign = '-'

print(f'the equation: y = {k} * x {sign} {abs(b)}')