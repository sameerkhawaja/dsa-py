def rotateBox(box):
    res = []
    num_rows = len(box)
    num_col = len(box[0])

    for col in range(num_col):
        new_row = []
        for row in range(num_rows):
            new_row.append(box[row][col])
        res.append(new_row)
    return res


arr = [[-1, -2, -3, -4], [1, 2, 3, 4]]
res = rotateBox(arr)
print(res)
