def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)
    return arr

def merge(arr, left, right):
    i, j, k = 0, 0, 0
    size_l = len(left)
    size_r = len(right)

    while i < size_l and j < size_r:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < size_l:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < size_r:
        arr[k] = right[j]
        j += 1
        k += 1

print(merge_sort([123, 8, 11, 34, 5, 234, 1, 4, 2]))
