def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2 
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))
    return arr


def merge(left_lis, right_lis):
    a = []
    i = 0; j = 0
    while i < len(left_lis) and j < len(right_lis):
        if left_lis[i] <= right_lis[j]:
            a.append(left_lis[i])
            i += 1
        else:
            a.append(right_lis[j])
            j += 1
    while i < len(left_lis):
        a.append(left_lis[i])
        i += 1
    while j < len(right_lis):
        a.append(right_lis[j])
        j += 1
    return a


def merge_two_sorted(arr1, arr2):
    return arr1 + arr2


print(merge_sort(merge_two_sorted([1,3,4,5,6], [12,21,30,41])))
