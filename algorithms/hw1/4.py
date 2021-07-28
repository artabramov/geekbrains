from random import random
from random import randrange

a = int(random() * 10 ** 8)
b = float(random() * 10 ** 8)
c = 'abcdefghijklmnopqrstuvwxyz'[randrange(26)]

print(f'integer: {a}')
print(f'float: {b}')
print(f'letter: {c}')

