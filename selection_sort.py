
from random import randint
import time

N = 100

# Selection Sort
array = []
for _ in range(N):
    array.append(randint(1, N))
print(array)

for i in range(N):
    min = array[i]
    min_idx = i
    for j in range(i+1, N):
        if array[j] < min:
            min = array[j]
            min_idx = j
    temp = array[i]
    array[i] = array[min_idx]
    array[min_idx] = temp

print(array)

