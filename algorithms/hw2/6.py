import random

number = random.randrange(1, 100, 1)
is_guess = False

for i in range(0, 10):
    j = int(input("input the humber: "))
    if j > number:
        print("the number is smaller")
    elif j < number:
        print("the number is bigger")
    else:
        is_guess = True
        break

if is_guess:
    print("the number is equal, you win")
else:
    print(f'the number was {number}, you lose')
