n = int(input("input n: "))

n_sum = sum(x for x in range(1, n + 1))
n_mul = int(n * (n + 1) / 2)

print(f'sum: {n_sum}, mul: {n_mul}')
