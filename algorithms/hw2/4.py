i, j = int(input("input the number: ")), 0
number = 1

repeat = True
while repeat:
    print(number)
    number = -1 * number / 2
    j += 1
    if j == i:
        repeat = False
