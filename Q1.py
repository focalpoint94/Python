"""
5
2 3 1 2 2
"""

N = int(input())

people = list(map(int, input().split()))

num_group = 0

people.sort(reverse=True)

ptr = 0
while ptr < len(people):
    ptr += people[ptr]
    num_group += 1

print(num_group)

