while True:
    number1, number2 = input("input first number: "), input("input second number: ")
    sign = input("input the sign: ")

    if sign == '0':
        break

    if sign not in ['+', '-', '*', '/']:
        print(f'the sign is incorrect!')
    elif sign == '/' and number2 == '0':
        print(f'divided by zero is incorrect!')
    else:
        print(eval(number1 + sign + number2))
