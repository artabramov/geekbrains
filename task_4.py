# Task 4
def get_bigger(nums: list):
    prev_num = nums[0]
    for num in nums[1:]:
        if num > prev_num:
            yield num
        prev_num = num


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
bigger_nums = get_bigger(src)
print(type(bigger_nums))
print(list(bigger_nums))
