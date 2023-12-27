# this is used to find the max sum of a subarray


def kadanes(nums):
    result = nums[0]
    window = 0

    for n in nums:
        # ensures that the window will never be negative
        # if the window in negative, our window will just be size 1 and point to current number
        window = max(window, 0) + n

        # see if our window is larger than our overall max
        result = max(window, result)

    return result


nums = [4, -1, 2, -7, 3, 4]
print(kadanes(nums))


def slidingWindow(nums):
    # init max to be first index
    maxSum = nums[0]
    currSum = 0

    # indexes for where max occurs. since we have first index as the max, it will be 0
    maxL, maxR = 0, 0

    L = 0
    for R in range(len(nums)):
        # if currSum is negative, reset it to 0 and shrink the window to size 1
        if currSum < 0:
            currSum = 0
            L = R

        # do math
        currSum = currSum + nums[R]

        # update maxSum and pointers
        if currSum > maxSum:
            maxSum = currSum
            maxL, maxR = L, R

    return [maxL, maxR]


nums = [4, -1, 2, -7, 3, 4]

print(slidingWindow(nums))
