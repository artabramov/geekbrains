import os
import json


def round_size(size: int):
    i = 10
    while size // 10 != 0:
        size = size // 10
        i = i * 10
    return i


def get_stats(path: str):
    stats = {}
    for item in os.listdir(path):
        size = os.path.getsize(os.path.join(path, item))
        ext = os.path.splitext(item)[1][1:]

        _size = round_size(size)
        if _size not in stats:
            stats[_size] = [0, []]

        stats[_size][0] = stats[_size][0] + 1

        if ext not in stats[_size][1]:
            stats[_size][1].append(ext)

    for _ in stats:
        stats[_] = tuple(stats[_])

    return stats


_dir = './my_project/templates'
stats = get_stats(_dir)
print(stats)


try:
    file = os.path.join(_dir, os.path.split(_dir)[-1] + '_summary.json')
    with open(file, 'w') as f:
        json.dump(stats, f)
except Exception as e:
    print(e)
