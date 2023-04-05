"""
The problem input is a linear data structure such as a linked list, array, or string
You’re asked to find the longest/shortest substring, subarray, or a desired value
Common problems you use the sliding window pattern with:
"""
arr = [1, 2, 3, 4, 5, 6]
k = 3


def get_max_sum(arr: list, k: int):
    if not arr or len(arr) < k:
        return None

    max_sum = current_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(current_sum, max_sum)

    return max_sum




print(get_max_sum(arr, k))
