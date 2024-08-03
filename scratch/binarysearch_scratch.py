def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if target < arr[m]:
            r = m - 1
        elif target > arr[m]:
            l = m + 1
        else:
            return m
    return -1
