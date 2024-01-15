def maxTaxi(n, rides):
    B = [0] * (n + 1)
    G = [[] for _ in range(n + 1)]

    # populate the value for each edge connecting to the node/index
    for start, end, tip in rides:
        G[end].append((start, end - start + tip))
    # calculate the most valuable path to that node/indx
    for time in range(1, n + 1):
        x = [B[time - 1]]
        y = [B[start] + dollar for start, dollar in G[time]]

        B[time] = max(x + y)

    return B[-1]


rides = [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
n = 20
maxTaxi(n, rides)
