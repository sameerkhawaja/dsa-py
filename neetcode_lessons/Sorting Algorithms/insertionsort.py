# Sorting algorithms
## Insertion sort
# - Mostly sorted
# - Small amount to sort


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        # for the second half of the condition, we only want to perform swaps if the Right value is less than the Left value
        while j >= 0 and arr[j + 1] < arr[j]:
            # swap can be rewritten as this
            # arr[j], arr[j+1] = arr[j+1], arr[j]

            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr


# without comments
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr
