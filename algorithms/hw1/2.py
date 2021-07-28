abin, bbin = '101', '110'
_and, _or = '', ''

for i in range(0,3):
    if abin[i] == '1' or bbin[i] == '1':
        _or += '1'
    else:
        _or += '0'

    if abin[i] == '1' and bbin[i] == '1':
        _and += '1'
    else:
        _and += '0'

print(f'OR: {_or}, AND: {_and}')
