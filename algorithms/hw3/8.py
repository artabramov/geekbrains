rows = []
for i in range(0, 4):
    cells = []
    for j in range(0, 4):
        cells.append(int(input(f'input ({i}, {j}): ')))
    cells.append(sum(cells))
    rows.append(cells)

for row in rows:
    print(row)