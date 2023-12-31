## Merge sort
from typing import List


def sortArray(self, nums: List[int]) -> List[int]:
    def mergeSort(arr: List[int], s: int, e: int):
        if e == s:
            return arr
        m = s + (e - s) // 2
        mergeSort(arr, s, m)
        mergeSort(arr, m + 1, e)
        merge(arr, s, m, e)

        return arr

    def merge(arr: List[int], s: int, m: int, e: int):
        # create copies of both halfs of the arr
        L = arr[s : m + 1]
        R = arr[m + 1 : e + 1]
        i, j, k = 0, 0, s

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
