
import heapq

S = input()

q = []
sum = 0

for idx in range(len(S)):
    if S[idx].isalpha():
        heapq.heappush(q, S[idx])
    else: sum += int(S[idx])

result = sorted(q)
for alpha in result:
    print(alpha, end='')
print(sum)
