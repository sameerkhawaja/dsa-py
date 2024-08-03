arr = [0, 1, 2, 2, 3, 0, 4, 2]
idx = 4
print(arr)


# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted
    return arr


print(removeMiddle(arr, idx, len(arr)))
