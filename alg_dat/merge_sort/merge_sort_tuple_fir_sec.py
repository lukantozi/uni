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
        if left_lis[i][0] < right_lis[j][0]:
            a.append(left_lis[i])
            i += 1
        elif left_lis[i][0] == right_lis[j][0]:
            if left_lis[i][1] <= right_lis[j][1]:
                a.append(left_lis[i])
                i += 1
            else:
                a.append(right_lis[j])
                j += 1
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

print(merge_sort([(5,1), (6,4), (6,3), (2,7), (1,0)]))
