letters = 'abcdefghijklmnopqrstuvwxyz'
a = input('input one english letter: ').lower()

if len(a) != 1 or a not in letters:
    raise ValueError('Value error.')

for i in range(0, len(letters)):
    if letters[i] == a:
        pos = i + 1
        break

print(f'letter position: {pos}')
