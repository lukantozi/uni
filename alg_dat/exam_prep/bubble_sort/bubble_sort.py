nums = [2, 4, 12, 9, 1, 3]
nums_1 = [9, 8, 3, 4, 8, 6, 5]

# layer A
def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr
#print(bubble_sort(nums))

# B1
def bubble_desc(arr):
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr
#print(bubble_desc(nums_1))

# B2
def bubble_count(arr):
    size = len(arr)
    count = 0
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                count += 1
                swapped = True
        if not swapped:
            return count
    return count
#print(bubble_count(nums_1))

# B3
def bubble_kpasses(arr, k):
    size = len(arr) 
    for i in range(k):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr
#print(bubble_kpasses(nums_1, 2))

# B4
def bubble_swap_log(arr):
    swap_log = []
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                swap_log += [[arr[j], arr[j+1]]]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return swap_log
    return swap_log
#print(bubble_swap_log(nums_1))

# B5
def last_swap_bubble(arr):
    size = len(arr)
    while size > 1:
        last_swapped = 0
        for i in range(size-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_swapped = i + 1
        size = last_swapped
    return arr
#print(last_swap_bubble(nums_1))
#print(last_swap_bubble(nums))

# B6
def cocktail_sort(arr):
    size = len(arr)
    start = 0
    end = size - 1
    swapped = True

    while swapped == True:

        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if swapped == False:
            break

        end -= 1
        swapped = False

        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1
    return arr
#print(cocktail_sort(nums_1))
#print(cocktail_sort(nums))

# A1 + B2 (timed: 20 mins)
def bubble_sort_comparison_swaps_timed(arr):
    print(f"to sort: {arr}")
    size = len(arr)
    count = 0
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
                swapped = True
        if swapped == False:
            return count
    return count
#print(f"swaps: {bubble_sort_comparison_swaps_timed(nums_1)}\nsorted: {nums_1}")

def bubble_k_last_swap(arr, k):
    size = len(arr)
    while size > 1 and k > 0:
        last_swapped = 0
        for i in range(size - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_swapped = i + 1
        size = last_swapped
        k -= 1
    return arr
#print(bubble_k_last_swap([9,8,4,3,2,1], 3))
