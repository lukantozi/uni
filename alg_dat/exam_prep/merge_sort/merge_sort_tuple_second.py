tuple_arr = [(2,4), (4, 5), (19, 14), (12, 3), (10, 9)]

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)

def merge(l, r, a):
    i, j, k = 0, 0, 0
    size_l = len(l)
    size_r = len(r)

    while i < size_l and j < size_r:
        if l[i][1] <= r[j][1]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1

    while i < size_l:
        a[k] = l[i]
        k += 1
        i += 1

    while j < size_r:
        a[k] = r[j]
        k += 1
        j += 1

print(merge_sort(tuple_arr))
