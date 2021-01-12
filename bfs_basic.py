
from collections import deque

visited = [False] * 9

graph = [[] for _ in range(9)]
for i in range(8):
    graph[i + 1] = list(map(int, input().split()))

trip = []

def bfs(graph, node, visited, trip):
    queue = deque([node])
    visited[node] = True

    while queue:
        a = queue.popleft()
        trip.append(a)
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited, trip)

print(trip)
