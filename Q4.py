

N = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for num in data:
    if num > target:
        break
    else:
        target += num

print(target)
