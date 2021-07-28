a = float(input('input first number: '))
b = float(input('input second number: '))
c = float(input('input third number: '))

numbers = [a, b, c]
if numbers[1] > numbers[0]:
    numbers[0], numbers[1] = numbers[1], numbers[0]
if numbers[2] > numbers[1]:
    numbers[1], numbers[2] = numbers[2], numbers[1]

print(f'average number is {numbers[1]}')
