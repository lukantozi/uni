nums = [12, 14, 13, 5, 6]

def insetion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr
#print(insetion_sort(nums))

# insertion ascending, in place A1
def insetion_sort_in_place(arr, l, r):
    for i in range(l+1, r+1):
        key = arr[i]
        j = i - 1

        while j >= l and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#print(insetion_sort_in_place(nums, 1, 3))

# A2: print array after each outer pass
def insetion_sort_print_outer(arr):
    n = len(arr)
    print(f"initial array: {arr}")

    for i in range(1, n):
        key = arr[i] 
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
        print(f"{6*'-'}pass #{i}: {arr}")
#insetion_sort_print_outer(nums)

# B1: descending insertion sort
def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#print(insertion_sort_desc(nums))

# B2: count shifts (how many moves happen)
def insertion_sort_count_shifts(arr):
    n = len(arr)
    count = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            count += 1
        arr[j+1] = key
    return count
#print(insertion_sort_count_shifts(nums))
#print(nums)

# B4: insert a value into already sorted list
def insert_into_sorted(arr, val):
    arr.append("")
    n = len(arr)
    j = n - 2
    while j >= 0 and val < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = val
    return arr
#print(insetion_sort(nums))
#print(insert_into_sorted(nums, 8))

# C1: asc + desc
def insertion_asc_timed(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#print(insertion_asc_timed(nums))

def insertion_desc_timed(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#print(insertion_desc_timed(nums))

# C2: count shifts implementation
def insertion_shift_count_timed(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            count += 1
        arr[j+1] = key
    return count
#print(insertion_shift_count_timed(nums))
#print(nums)
