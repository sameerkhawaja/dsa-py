from typing import List

def quickSort(arr: List[int], l: int, r: int) -> List[int]:
    if l>=r:
        return
    
    pivot = arr[r]
    ptr = l

    for i in range(l,r):
        if arr[i]<pivot:
            arr[i],arr[ptr] = arr[ptr],arr[i]
            ptr+=1
    
    arr[r],arr[ptr]=arr[ptr],arr[r]

    quickSort(arr, l, ptr-1)
    quickSort(arr,ptr+1,r)

    return arr

# Example usage:
nums = [3, 1, 4, 2, 7, 3, 4, 8, 6, 2]

result = quickSort(nums, 0, len(nums) - 1)
print(result)