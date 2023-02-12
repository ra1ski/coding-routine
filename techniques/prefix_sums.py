from itertools import accumulate

nums = [1, 2, 3, 4, 5, 6, 7]


def get_prefix_sums(nums: list):
    prefix_sums = []

    for i in range(len(nums)):
        prefix_sums.append(nums[i])

        if i > 0:
            prefix_sums[i] = nums[i] + prefix_sums[i - 1]

    return prefix_sums


def get_prefix_sums2(nums: list):
    prefix_sums = []

    prefix_sums.append(nums[0])

    for i in range(1, len(nums)):
        prefix_sums.append(nums[i] + prefix_sums[i - 1])

    return prefix_sums


def get_prefix_sum_accumulated(nums):
    return list(accumulate(nums))

ps = get_prefix_sums(nums)
...