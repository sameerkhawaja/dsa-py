ans = [x * x for x in range(10)]
print(ans)

ans = [x * x for x in range(10) if x % 2 == 0]
print(ans)

ans = [(x, y) for x in range(3) for y in range(3)]
print(ans)

ans = [[i for i in range(5)] for j in range(3)]
print(ans)
