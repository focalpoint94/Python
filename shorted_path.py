
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

ans = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def path_finder():
    # y x d
    queue = deque([[0, 0, 1]])
    while True:
        # [y x d]
        current = queue.popleft()
        # 다녀감
        graph[current[0]][current[1]] = 0
        # 도착점?
        if current[0] == N - 1 and current[1] == M - 1:
            global ans
            ans = current[2]
            return
        # 상하좌우 유효하다면?
        for i in range(4):
            next_y = current[0] + dy[i]
            next_x = current[1] + dx[i]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < M and graph[next_y][next_x] == 1:
                queue.append([next_y, next_x, current[2] + 1])

path_finder()
print(ans)

