"""
Inputs
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""

import heapq

def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

vertex = []

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b, cost = map(int, input().split())
    heapq.heappush(vertex, (cost, a, b))

result = 0
maximum_road = 0

for _ in range(M):
    cost, a, b = heapq.heappop(vertex)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        if cost > maximum_road:
            maximum_road = cost
    else:
        continue

result -= maximum_road

print(result)

