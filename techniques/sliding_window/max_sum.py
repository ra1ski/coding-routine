arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
window_size = 3

for i in range(len(arr) - window_size + 1):
    window = arr[i:i + window_size]
    print(window)


def max_sum(arr: list, k: int) -> list:
    if not list or len(arr) < k:
        return []

    max_sum = sum(arr[:k])

