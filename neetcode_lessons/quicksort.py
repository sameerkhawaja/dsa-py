from typing import List

def quickSort(arr: List[int], l: int, r: int) -> List[int]:
    if l >= r:
        return

    pivot = arr[r]  
    T = l  

    for i in range(l, r):
        if arr[i] < pivot:
            arr[T], arr[i] = arr[i], arr[T]
            T += 1

    arr[r], arr[T] = arr[T], arr[r]

    quickSort(arr, l, T - 1)
    quickSort(arr, T + 1, r)
    return arr

# Example usage:
nums = [3, 1, 4, 2, 7, 3, 4, 8, 6, 2]

result = quickSort(nums, 0, len(nums) - 1)
print(result)
