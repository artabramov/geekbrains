sequence = str(int(input("input the sequence: ")))
number = str(int(input("input the number: ")))

j = 0
for i in sequence:
    if i == number:
        j += 1

print(f'count of the numbers in the sequence: {j}')
