def add_value(arr, val):
    # add 800 after 700
    arr[2][2].append(val)
    
#strange_list = [1, 2, [30, 40, [500, 600, 700], 80], 8]
#add_value(strange_list, 800)
#print(strange_list)

def count_first_last(arr):
    count = 0
    for sub in arr:
        if sub[0] == sub[-1] and len(sub) > 2:
            count += 1
    return count

#print(count_first_last(['abc', 'xyz', 'aba', '1221']))

def aggr_len_sub(arr):
    count = 0
    for sub in arr:
        count += len(sub)
    return count

#print(aggr_len_sub([[1,2], [2], [2,3,4]]))

def sort_by_length(arr):
    return sorted(arr, key=len)

#print(sort_by_length(["aa", "eeeee", "ggggg", "w", "ttttttttttttttttttttt", "zzz"]))
