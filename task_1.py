# Task 1
def odd_nums(num_limit: int):
    for num in range(1, num_limit + 1, 2):
        yield num


numbers = odd_nums(100)
print(type(numbers))
print(list(numbers))
