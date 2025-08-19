def spiralReader(arr):
    m = len(arr)
    n = len(arr[0])
    ans = []

    sr, sc = 0, 0
    er, ec = m - 1, n - 1

    while sr <= er and sc <= ec:

        # top row
        for j in range(sc, ec + 1):
            ans.append(arr[sr][j])

        # right column
        for i in range(sr + 1, er + 1):
            ans.append(arr[i][ec])

        # bottom row
        if sr < er:
            for j in range(ec - 1, sc - 1, -1):
                ans.append(arr[er][j])

        # left column
        if sc < ec:
            for i in range(er - 1, sr, -1):
                ans.append(arr[i][sc])

        # move to inner layer
        sr += 1
        sc += 1
        er -= 1
        ec -= 1

    return ans


# Driver Code
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("output is:", spiralReader(arr))
