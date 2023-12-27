# Sorting algorithms
## Insertion sort
- Mostly sorted 
- Small amount to sort

```
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        # for the second half of the condition, we only want to perform swaps if the Right value is less than the Left value
        while j >=0 and arr[j+1] < arr[j]:
            # swap can be rewritten as this 
            # arr[j], arr[j+1] = arr[j+1], arr[j]

            temp = arr[j+1] 
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr
```
```
# without comments
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >=0 and arr[j+1] < arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr
```


## Merge sort
```
def sortArray(self, nums: List[int]) -> List[int]:
    def mergeSort(arr: List[int], s: int, e: int):
        if e == s:
            return arr
        m = (e + s) // 2 
        mergeSort(arr, s, m)
        mergeSort(arr, m+1, e)
        merge(arr, s, m, e)

        return arr

    def merge(arr: List[int], s: int, m: int, e: int):
    # create copies of both halfs of the arr
        L = arr[s:m+1]
        R = arr[m+1:e+1]
        i,j,k = 0,0,s

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

    return mergeSort(nums, 0, len(nums)-1)
```


## Bucket sort
    Dont care about space
    finite number of options

