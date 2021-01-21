
def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0] * (v+1)

cycle = False

for i in range(1, v+1):
    parent[i] = i

"""
Cycle의 판별:
for 모든 간선에 대해:
    연결된 두 노드의 root node를 확인한다.
    if 같다면 cycle임
    만약 다르다면 union 연산을 수행한다.
"""

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle: print("YES")
else: print("NO")

