
# ~Python Basics 복습~

# 1. List

# append 와 remove method
arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr.append(3)
print(arr)
arr.remove(3)
print(arr)

# init
N = 10
arr = [0] * 10
print(arr)

# list comprehension
arr = [i for i in range(20) if i % 7 == 0]
print(arr)

brr = [i for i in range(13) if i in arr]
print(brr)

crr = [i for i in range(10) if i not in brr]
print(crr)

# 2차원 list
N = 3; M = 2;
arr = [[0] * M for _ in range(N)]
print(arr)

for i in range(N):
    for j in range(M):
        arr[i][j] = 2 * i + j + 1
print(arr)

# methods
arr = [1, 3, 2, 5, -1, 11]
print(arr)

arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr.insert(0, 99)
print(arr)

print(arr.count(99))

# list에서 특정 값 제거하기
arr = [i for i in range(10)]
print(arr)
remove_set = [i for i in range(10) if i % 2 == 0]

removed = [i for i in arr if i not in remove_set]
print(removed)
print()

# 2. Tuple
tup = (1, 2, 3)
print(tup)
print()

# 3. Dictionary
N = 3
keys = [0, 1, 2]
values = ['전', '이', '김']

dic = dict()
for i in range(N):
    dic[keys[i]] = values[i]
print(dic)

key_list = dic.keys()
value_list = dic.values()
print(key_list, value_list)

# 4. Set
set_A = {1, 2, 3, 3, 3, 3}
set_B = {2, 3, 4, 5, 5}
print(set_A)
print(set_A | set_B)
print(set_A & set_B)
print(set_A - set_B)

# methods
set = {1, 2}
print(set)
set.add(3)
print(set)
set.update([4, 5, 6])
print(set)
set.remove(3)
print(set)

# 6. lambda
print((lambda x, y: x * y)(3, 4))
print()

# 7. 입출력
# 한줄 입력 받기
#n = int(input())

# 공백으로 구분된 경우
#data = list(map(int, input().split()))
#print(n)
#print(data)

# 빠른 입력
#import sys
#data = sys.stdin.readline().rstrip()
#print(data)

# 8. Libraries
# 내장 함수
# sum, min, max, eval
# sorted: iterable 객체의 정렬된 결과
import random
N = 10
arr = [0] * 10
print(arr)
for i in range(N):
    arr[i] = random.randrange(N)
print(arr)
sorted_arr = sorted(arr)
print(sorted_arr)
print()

# itertools
from itertools import permutations, combinations, product, combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)
print()

# heapq
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# bisect
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# deque: queue의 구현
from collections import deque
data = deque()
data.append(1)
data.append(2)
print(data)
data.appendleft(3)
print(data)
data.popleft()
print(data)
data.pop()
print(data)
print()

from collections import Counter
counter = Counter(data)
print(dict(counter))
print(counter[1])
print()

# math
import math
print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21, 14))
print(math.e, math.pi)
print()
