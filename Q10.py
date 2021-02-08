"""
0 0 0
1 0 0
0 1 1
1 1 1
1 1 0
1 0 1
"""
import copy

# Key size
M = 3
# Lock Size
N = 3

key = [[0] * M for _ in range(M)]
for i in range(M):
    key[i] = list(map(int, input().split()))

lock = [[0] * N for _ in range(N)]
for i in range(N):
    lock[i] = list(map(int, input().split()))

graph = [[1] * (N+2*M-2) for _ in range(N+2*M-2)]
for i in range(N):
    for j in range(N):
        graph[M+i-1][M+j-1] = lock[i][j]

print(graph)

def rotate_matrix_by_90_deg(list):
    N = len(list)
    M = len(list[0])
    new = [[0] * N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            new[c][N - 1 - r] = list[r][c]
    return new

def all_is_one(graph, start, end):
    for i in range(start, end + 1):
        for j in range(start, end + 1):
            if graph[i][j] == 0:
                return False
    return True

def is_solved(graph, gey):
    # (y, x) sweep 시작 좌표
    for _ in range(4):
        keys = []
        for i in range(M):
            for j in range(M):
                if gey[i][j] == 1:
                    keys.append((i, j))
        for y in range(N+M-1):
            for x in range(N+M-1):
                locked_map = copy.deepcopy(graph)
                fail_flag = False
                for key in keys:
                    if y+key[0] >= M-1 and y+key[0] <= M+N-2 and x+key[1] >= M-1 and x+key[1] <= M+N-2 and locked_map[y+key[0]][x+key[1]] == 1:
                        fail_flag = True
                        break
                    else:
                        locked_map[y+key[0]][x+key[1]] = 1
                if fail_flag:
                    continue
                if all_is_one(locked_map, M-1, M+N-2):
                    return True
        gey = rotate_matrix_by_90_deg(gey)
    return False

print(is_solved(graph, key))
