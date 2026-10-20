
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kth_largest(arr, k):
    n = len(arr)

    if k < 1 or k > n:
        raise ValueError("k must be between 1 and len(arr)")

    target = n - k
    low = 0
    high = n - 1

    while low <= high:
        pi = partition(arr, low, high)

        if pi == target:
            return arr[pi]
        elif pi < target:
            low = pi + 1
        else:
            high = pi - 1


arr = [3, 2, 1, 5, 6, 4]
k = 2

print(kth_largest(arr, k))  # 5
