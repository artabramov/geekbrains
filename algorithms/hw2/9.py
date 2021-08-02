tmp = input("input any numbers divided by the comma: ")
numbers = tmp.split(',')
bigger = 0

for i in numbers:
    if int(i) > bigger:
        bigger = int(i)

print(bigger)
