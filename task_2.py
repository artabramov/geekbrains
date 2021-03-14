# Task 2
def get_nums(num_limit: int):
    return list(range(1, num_limit + 1, 2))


numbers = get_nums(100)
print(type(numbers))
print(numbers)
