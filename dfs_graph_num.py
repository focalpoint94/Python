

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(y, x):
    # out of range
    if y < 0 or x < 0 or y >= N or x >= M:
        return False
    if graph[y][x] == 1:
        return False
    # 방문
    graph[y][x] = 1
    for _ in range(4):
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)
    return True

slices = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            slices += 1

print(slices)
