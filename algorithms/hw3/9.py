import random

i_max, j_max = 4, 5
rows = []
for i in range(0, i_max):
    cells = []
    for j in range(0, j_max):
        cells.append(random.randint(0, 100))
    rows.append(cells)

for row in rows:
    print(row)

mins = [100] * j_max
for j in range(0, j_max):
    for i in range(0, i_max):
        if rows[i][j] < mins[j]:
            mins[j] = rows[i][j]

print(' -- ' * j_max)
print(mins)
print(max(mins))

