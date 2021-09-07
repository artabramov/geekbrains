numbers_count = 0
for i in range(2,100):

    is_multiple = True
    for j in range(2,10):
        if i % j != 0:
            is_multiple = False
            break

    if is_multiple:
        numbers_count += 1

print(numbers_count)
