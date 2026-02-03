nums = [64, 34, 25, 12, 22, 11, 90]
nums_dup = [5, 5, 5, 5]
nums_rev = [9, 7, 5, 3, 1]
 
# A1: quicksort three way
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    piv = arr[len(arr)//2]

    less = [x for x in arr if x < piv]
    equal = [x for x in arr if x == piv]
    more = [x for x in arr if x > piv]

    return quick_sort(less) + equal + quick_sort(more)

#print(quick_sort(nums))
#print(quick_sort(nums_dup))
#print(quick_sort(nums_rev))
#print(quick_sort([1]))

# B1: descending order
def quick_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    piv = arr[len(arr)//2]

    less = [x for x in arr if x < piv]
    equal = [x for x in arr if x == piv]
    more = [x for x in arr if x > piv]

    return quick_sort_desc(more) + equal + quick_sort_desc(less)

#print(quick_sort_desc(nums))
#print(quick_sort_desc(nums_dup))
#print(quick_sort_desc(nums_rev))
#print(quick_sort_desc([1]))

# B2: case insensitive strings
def quick_sort_insens(arr):
    if len(arr) <= 1:
        return arr
    
    piv = arr[len(arr)//2]
    piv_lowered = piv.lower()

    less = [x for x in arr if x.lower() < piv_lowered]
    equal = [x for x in arr if x.lower() == piv_lowered]
    more = [x for x in arr if x.lower() > piv_lowered]

    return quick_sort_insens(less) + equal + quick_sort_insens(more)

#print(quick_sort_insens(['Bob', 'alice', 'Carol']))

def quick_sort_abs(arr):
    if len(arr) <= 1:
        return arr
    
    piv = arr[len(arr)//2]
    abs_piv = abs(piv)

    less = [x for x in arr if abs(x) < abs_piv]
    equal = [x for x in arr if abs(x) == abs_piv]
    more  = [x for x in arr if abs(x) > abs_piv]

    return quick_sort_abs(less) + equal + quick_sort_abs(more)

print(quick_sort_abs([-10, -3, 1, 2, -2, 5]))
