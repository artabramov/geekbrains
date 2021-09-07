y = int(input('input the year: '))

if (y % 100 != 0 and y % 4 == 0) or (y % 100 == 0 and y % 400 == 0):
    print('leap year')
else:
    print('common year')
