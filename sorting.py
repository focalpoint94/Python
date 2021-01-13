
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

"""
# Selection Sort
for idx in range(len(arr)):
    min_idx = idx
    for j in range(idx + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
"""

"""
# Insertion Sort
for idx in range(1, len(arr)):
    j = idx - 1
    while j >= 0 and arr[j] > arr[idx]:
        arr[idx], arr[j] = arr[j], arr[idx]
        j -= 1
        idx -= 1
"""

# Quick Sort
def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    residue = list[1:]
    left = [x for x in residue if x <= pivot]
    right = [x for x in residue if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(arr))
