
from random import randint

N = 10
array = [0] * N
for i in range(N):
    array[i] = randint(0, N)

array = sorted(array)

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

print(array)
print(binary_search(array, 3, 0, len(array) - 1))
