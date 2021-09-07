# Извините, но задача прекрасно решается без хеш-функций

string = 'abcabc'
subs = set()

for i in range(0, len(string) + 1):
    for j in range(i, len(string) + 1):
        subs.add(string[i:j])
subs.remove('')

print(subs)
print(len(subs))
