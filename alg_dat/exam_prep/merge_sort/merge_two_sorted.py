arr_1 = [1, 5, 12, 19, 25]
arr_2 = [3, 6, 14, 18, 23, 28]

def merge_two_sorted(ar_1, ar_2):
    i, j, k = 0, 0, 0
    size_ar1 = len(ar_1)
    size_ar2 = len(ar_2)
    arr = [0]*(size_ar1+size_ar2)

    while i < size_ar1 and j < size_ar2:
        if ar_1[i] <= ar_2[j]:
            arr[k] = ar_1[i]
            i += 1
        else:
            arr[k] = ar_2[j]
            j += 1
        k += 1
    
    while i < size_ar1:
        arr[k] = ar_1[i]
        i += 1
        k += 1
    while j < size_ar2:
        arr[k] = ar_2[j]
        j += 1
        k += 1
    return arr
print(merge_two_sorted(arr_1, arr_2))
