def quick_sort_asc(arr):
    if len(arr) <= 1:
        return arr

    piv = arr[len(arr)//2]
    less = [x for x in arr if x < piv]
    equal = [x for x in arr if x == piv]
    more = [x for x in arr if x > piv]

    return quick_sort_asc(less) + equal + quick_sort_asc(more)

def quick_sort_insens(arr):
    if len(arr) <= 1:
        return arr

    piv = arr[0]
    lower_piv = piv.lower()
    less = [x for x in arr if x.lower() < lower_piv]
    equal = [x for x in arr if x.lower() == lower_piv]
    more = [x for x in arr if x.lower() > lower_piv]

    return quick_sort_insens(less) + equal + quick_sort_insens(more)

print(quick_sort_asc([64, 34, 25, 12, 22, 11, 90]))
print(quick_sort_insens(['Bob', 'alice', 'Carol']))
