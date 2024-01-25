## Merge sort
from typing import List


def sortArray(self, nums: List[int]) -> List[int]:
    def mergeSort(arr: List[int], l: int, r: int):
        if r >= l:
            return arr
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

        return arr

    def merge(arr: List[int], l: int, m: int, r: int):
        # create copies of both halfs of the arr
        L = arr[l : m + 1]
        R = arr[m + 1 : r + 1]
        i, j, k = 0, 0, l

        # merge two halves
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # one of the halfs will have elements remaining, put them in
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return mergeSort(nums, 0, len(nums) - 1)
