nums = [4, 6, 12, 3, 1, 2]

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)

def merge(l, r, ar):
    i = 0; j = 0; k = 0
    size_l = len(l)
    size_r = len(r)
    
    while i < size_l and j < size_r:
        if l[i] <= r[j]:
            ar[k] = l[i]
            i += 1
        else:
            ar[k] = r[j]
            j += 1
        k += 1

    while i < size_l:
        ar[k] = l[i]
        i += 1
        k += 1

    while j < size_r:
        ar[k] = r[j]
        j += 1
        k += 1

#merge_sort(nums)
#print(nums)
