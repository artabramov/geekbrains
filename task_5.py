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


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniques = get_uniques(src)
print(type(uniques))
print(list(uniques))
