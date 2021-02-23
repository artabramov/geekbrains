def print_plural(number: int):

    if not isinstance(number, int):
        number = 0

    # use abs for calculate the correct remain of negative numbers
    remain, ending = abs(number) % 10, ""

    if 5 <= number <= 20 or remain in [0, 5, 6, 7, 8, 9]:
        ending = "ов"

    elif remain in [2, 3, 4]:
        ending = "а"

    print(number, "процент" + ending)
    return True


for i in range(0, 21):
    print_plural(i)
