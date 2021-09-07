array_1, array_2 = [8, 3, 15, 6, 4, 2], []
for key, value in enumerate(array_1):
    if value % 2 == 0:
        array_2.append(key)

print(array_2)
