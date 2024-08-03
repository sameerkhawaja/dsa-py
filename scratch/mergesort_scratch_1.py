def merge(arr, l, m, r):
    # use an arr of size 2 to understand
    left_arr = arr[l : m + 1]
    right_arr = arr[m + 1 : r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, l, r) -> list:
    if l >= r:
        return arr
    m = (l + r) // 2
    merge_sort(arr, l, m)
    merge_sort(arr, m + 1, r)

    merge(arr, l, m, r)

    return arr


def test_merge_sort():
    # Test cases
    tests = [
        ([], []),  # Empty array
        ([1], [1]),  # Single element array
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Sorted array
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted array
        ([4, 1, 3, 4, 2], [1, 2, 3, 4, 4]),  # Array with duplicates
        ([3, -1, 4, -2, 0], [-2, -1, 0, 3, 4]),  # Array with negative numbers
        (list(range(1000, 0, -1)), list(range(1, 1001))),  # Large array
    ]

    for i, (input_array, expected_output) in enumerate(tests):
        merge_sort(input_array, 0, len(input_array) - 1)
        assert (
            input_array == expected_output
        ), f"Test case {i + 1} failed: {input_array}"

    print("All test cases passed!")


# Run the tests
test_merge_sort()
