# needs sorted array
# usually task is to determine if target exists in array
def binarySearch(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        if target < m:
            r = m - 1
        elif target > m:
            l = m + 1
        else:
            return m
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2
res = binarySearch(nums, target)
print("index: ", res)
