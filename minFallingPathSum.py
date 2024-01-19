def minFallingPathSum(A: List[List[int]]) -> int:
    r = len(A)
    c = len(A[0])
    for i in range(1, r):
        for j in range(c):
            if j == 0:
                A[i][j] += min(A[i - 1][j + 1], A[i - 1][j])
            elif j == c - 1:
                A[i][j] += min(A[i - 1][j - 1], A[i - 1][j])
            else:
                A[i][j] += min(A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1])
    return min(A[-1])
