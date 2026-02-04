arr = ["Monia", "BaNana", "bool", "luka", "mania", "apple"]

def merge_sort_strings(arr, key):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort_strings(left, key)
        merge_sort_strings(right, key)
        merge(left, right, arr, key)
    return arr

def merge(l, r, a, key):
    i, j, k = 0, 0, 0
    size_l = len(l)
    size_r = len(r)

    while i < size_l and j < size_r:
        if key(l[i]) <= key(r[j]):
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k +=1

    while i < size_l:
        a[k] = l[i]
        i += 1
        k += 1 

    while j < size_r:
        a[k] = r[j]
        j += 1
        k += 1

print(merge_sort_strings(arr, key=str.lower))
