letters = 'abcdefghijklmnopqrstuvwxyz'
ab = input('input two english letters: ').lower()

if len(ab) != 2 or ab[0] not in letters or ab[1] not in letters:
    raise ValueError('Value error.')

for i in range(0, len(letters)):
    if letters[i] == ab[0]:
        apos = i + 1
    if letters[i] == ab[1]:
        bpos = i + 1

if abs(apos - bpos) > 1:
    rpos = abs(apos - bpos) - 1
else:
    rpos = 0

print(f'positions of letters: {apos}, {bpos}')
print(f'letters number between letters: {rpos}')
