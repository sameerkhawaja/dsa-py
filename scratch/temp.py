arr = list(range(1, 10))

l = 0
r = len(arr) - 1
m = (l + r) // 2

L = arr[l : m + 1]
R = arr[m + 1 : r + 1]

print(l, m, r)
print(arr[l], arr[m], arr[r])
print(L)
print(R)
