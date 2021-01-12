
graph = [[] for _ in range(9)]
for i in range(8):
    graph[i + 1] = list(map(int, input().split()))

visited = [False] * 9
trip = []

def dfs(graph, node, visited, trip):
    visited[node] = True
    trip.append(node)
    for i in graph[node]:
        print(i)
        if not visited[i]:
            dfs(graph, i, visited, trip)

dfs(graph, 1, visited, trip)

print(trip)
