number = str(int(input("input the number: ")))
even, uneven = 0, 0

for i in number:
    if int(i) % 2 == 0:
        even += 1
    else:
        uneven += 1

print(f'even: {even}, uneven: {uneven}')
