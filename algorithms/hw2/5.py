start, end = 32, 127
tmp = dict()

for i in range(start, end):
    tmp[i] = chr(i)
    if len(tmp) == 10:
        print(tmp)
        tmp = dict()
