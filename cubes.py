def calc_digits_sum(number: int):
    digits_sum = 0
    while number > 0:
        digits_sum += number % 10
        number //= 10
    return digits_sum


def print_cubes_sum():
    odd_numbers, sums = [], [0, 0]

    for i in range(1, 1001, 2):
        odd_numbers.append(i**3)

    for j in odd_numbers:
        digits_sum = calc_digits_sum(j)
        if digits_sum % 7 == 0:
            sums[0] += j

        digits_sum = calc_digits_sum(j + 17)
        if digits_sum % 7:
            sums[1] += j + 17

    print(sums[0], sums[1], sep="\n")
    return True


print_cubes_sum()
