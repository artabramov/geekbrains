# Task 1
def odd_nums(num_limit: int):
    for num in range(1, num_limit + 1, 2):
        yield num


# Task 2
def get_nums(num_limit: int):
    return list(range(1, num_limit + 1, 2))


# Task 3
def get_pairs(tutors: list, klasses: list):
    for id, tutor in enumerate(tutors):
        yield tutor, klasses[id] if id <= len(klasses) - 1 else None


# Task 4
def get_bigger(nums: list):
    prev_num = nums[0]
    for num in nums[1:]:
        if num > prev_num:
            yield num
        prev_num = num


# Task 5
def get_uniques(nums: list):
    """
    Get unique elements of the list in original order.
    Algorithm speed is O(2n).
    """
    unique_nums, used_nums = set(), set()

    for num in nums:
        if num in used_nums and num in unique_nums:
            unique_nums.remove(num)
        else:
            unique_nums.add(num)

        used_nums.add(num)

    result_nums = list()
    for num in nums:
        if num in unique_nums:
            result_nums.append(num)

    return result_nums


# 1
numbers = odd_nums(100)
print(type(numbers))
print(list(numbers))

# 2
numbers = get_nums(100)
print(type(numbers))
print(numbers)

# 3
_tutors =  ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
_klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
pairs = get_pairs(_tutors, _klasses)
print(type(pairs))
print(list(pairs))

# 4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
bigger_nums = get_bigger(src)
print(type(bigger_nums))
print(list(bigger_nums))

#5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniques = get_uniques(src)
print(type(uniques))
print(list(uniques))
