
"""
Inputs
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""

from collections import deque
import copy

N = int(input())

indegrees = [0] * (N+1)
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)

for i in range(1, N+1):
    inputs = list(map(int, input().split()))
    time[i] = inputs[0]
    indegrees[i] = len(inputs) - 2
    for prev in inputs[1:-1]:
        graph[prev].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, N+1):
        if indegrees[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for next in graph[now]:
            result[next] = max(result[next], result[now] + time[next])
            indegrees[next] -= 1
            if indegrees[next] == 0:
                q.append(next)

    for i in range(1, N+1):
        print(result[i])

topology_sort()
