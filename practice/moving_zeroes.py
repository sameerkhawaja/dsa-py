def movingZeroes(arr):
    idx = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1


def movingNegativeOnes(arr):
    idx = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            arr[idx] = arr[i]
            idx += 1

    for i in range(idx, len(arr)):
        arr[i] = 0


def movingNegativeOnes2d(arr):
    idx = len(arr) - 1

    for i in range(len(arr) - 1, -1, -1):
        if arr[i][0] > 0:
            arr[idx][0] = arr[i][0]
            idx -= 1

    for i in range(idx, -1, -1):
        arr[i][0] = 0


arr = [0, 0, 0, 0, 4, 1, 411, 311, 211, 5]
movingZeroes(arr)
print(arr)

arr = [-1, -1, -1, -1, 4, 1, 411, 311, 211, 5]
movingNegativeOnes(arr)
print(arr)

arr = [-1, -1, -1, -1, 4, 1, 411, 311, 211, 5]
vertical_array = [[element] for element in reversed(arr)]
movingNegativeOnes2d(vertical_array)
print(vertical_array)
