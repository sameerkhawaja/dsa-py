def binarySearch(low, high):
    while low <= high:
        m = low + (high - low) // 2
        if isCorrect(m) > 0:
            high = m - 1
        elif isCorrect(m) < 0:
            low = m + 1
        else:
            return m
    return -1


# this function would be given to us to determine how good our guess is
# Return 1 if n is too big, -1 if too small, 0 if correct
guess = 101


def isCorrect(n):
    if n > guess:
        return 1
    elif n < guess:
        return -1
    else:
        return 0


res = binarySearch(0, 100)
print(res)
