# 2차원 행렬의 90도 회전

def rotate_matrix_by_90_deg(list):
    N = len(list)
    M = len(list[0])
    new = [[0] * N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            new[c][N - 1 - r] = list[r][c]
    return new

arr = [[1, 2, 3, 4],
       [5, 6, 7, 8]]

print(rotate_matrix_by_90_deg(arr))
