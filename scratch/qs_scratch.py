def quicksort(arr, l, r):
    if l >= r:
        return arr

    piv = arr[r]
    ptr = l

    for i in range(l, r):
        if arr[i] < piv:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[r] = arr[r], arr[ptr]

    quicksort(arr, l, ptr - 1)
    quicksort(arr, ptr + 1, r)

    return arr


def test_quicksort():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
        ([3, -2, 5, 0, -1], [-2, -1, 0, 3, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]

    for i, (input_arr, expected_output) in enumerate(test_cases):
        sorted_arr = quicksort(input_arr[:], 0, len(input_arr) - 1)
        assert (
            sorted_arr == expected_output
        ), f"Test case {i} failed: {sorted_arr} != {expected_output}"

    print("All test cases passed!")


test_quicksort()
