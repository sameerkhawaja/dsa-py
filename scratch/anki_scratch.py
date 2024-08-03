def 

# tests below
def test_kadanes():
    assert kadanes([1, 2, 3, 4, 5]) == 15, "Test case 1 failed"
    assert kadanes([-2, -3, 4, -1, -2, 1, 5, -3]) == 7, "Test case 2 failed"
    assert kadanes([-1, -2, -3, -4]) == -1, "Test case 3 failed"
    assert kadanes([5, 4, -1, 7, 8]) == 23, "Test case 4 failed"
    assert kadanes([0]) == 0, "Test case 5 failed"
    print("All kadanes tests passed")


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2, "Test case 1 failed"
    assert binary_search([1, 2, 3, 4, 5], 6) == -1, "Test case 2 failed"
    assert binary_search([], 3) == -1, "Test case 3 failed"
    assert binary_search([1], 1) == 0, "Test case 4 failed"
    assert binary_search([1, 2, 3, 4, 5], 1) == 0, "Test case 5 failed"
    print("All binary_search tests passed")


def test_insertion_sort():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 1 failed"
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 2 failed"
    assert insertion_sort([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5], "Test case 3 failed"
    assert insertion_sort([]) == [], "Test case 4 failed"
    assert insertion_sort([1]) == [1], "Test case 5 failed"
    print("All insertion_sort tests passed")


def test_merge_sort():
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], "Test case 1 failed"

    arr = [1, 2, 3, 4, 5]
    merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], "Test case 2 failed"

    arr = [4, 2, 5, 1, 3]
    merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], "Test case 3 failed"

    arr = []
    merge_sort(arr, 0, len(arr) - 1)
    assert arr == [], "Test case 4 failed"

    arr = [1]
    merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1], "Test case 5 failed"

    print("All merge_sort tests passed")


def test_quick_sort():
    arr = [5, 4, 3, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], "Test case 1 failed"

    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], "Test case 2 failed"

    arr = [4, 2, 5, 1, 3]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5], "Test case 3 failed"

    arr = []
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [], "Test case 4 failed"

    arr = [1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1], "Test case 5 failed"

    print("All quick_sort tests passed")


# Uncomment the following lines to run the tests
# test_kadanes()
# test_binary_search()
# test_insertion_sort()
# test_merge_sort()
test_quick_sort()
