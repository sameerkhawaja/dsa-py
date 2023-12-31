# typically lists are used as the buckets
# if stability is important, then we can use linked lists
# best if we know ahead of time types of values


def bucketSort(arr):
    counter = [0, 0, 0]
    for n in arr:
        counter[n] += 1

    i = 0
    for n in range(len(counter)):
        for _ in range(counter[n]):
            arr[i] = n
            i += 1
    return arr


arr = [2, 1, 2, 0, 0, 2]
print(bucketSort(arr))


# color example
def bucketsortColor(arr):
    count = [0, 0, 0]
    # count
    for n in arr:
        match n:
            case "r":
                count[0] += 1
            case "g":
                count[1] += 1
            case "b":
                count[2] += 1

    # sort
    i = 0  # index for array
    for c in range(len(count)):  # iterate through rgb counter
        for _ in range(count[c]):  # repeat r/g/b times [1,3,2]
            match c:
                case 0:
                    arr[i] = "r"
                case 1:
                    arr[i] = "g"
                case 2:
                    arr[i] = "b"

            i += 1
    return arr


arr = [
    "r",
    "g",
    "b",
    "g",
    "b",
    "g",
]
res = bucketsortColor(arr)
print(res)
