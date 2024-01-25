def quickSort(nums, l, r):
    if l >= r:
        return

    pivotVal = nums[r]
    ptr = l

    for i in range(l, r):
        if nums[i] < pivotVal:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1

    nums[r], nums[ptr] = nums[ptr], nums[r]

    # recursive call to itself
    quickSort(nums, l, ptr - 1)
    quickSort(nums, ptr + 1, r)
    return nums


nums = [3, 1, 4, 2, 7, 3, 4, 8, 6, 2]

result = quickSort(nums, 0, len(nums) - 1)
print(result)
