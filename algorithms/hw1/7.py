a = float(input('input first side: '))
b = float(input('input second side: '))
c = float(input('input third side: '))

if 0 < a < b + c and 0 < b < a + c and 0 < c < a + b:
    print('triangle is possible')
else:
    print('triangle is not possible')
