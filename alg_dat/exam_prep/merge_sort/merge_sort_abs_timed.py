nums = [4, -1, 123, -141, 42, 58, -45]

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i, j, k = 0, 0, 0
    size_l = len(left)
    size_r = len(right)

    while i < size_l and j < size_r:
        if abs(left[i]) <= abs(right[j]):
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

print(merge_sort(nums))
