def insertion_sort(arr):
    print("Start: ", arr)
    for i in range(1, len(arr)):
        key = arr[i] # number we want to insert
        j = i - 1 # pointer to the left of key

        print(f"\nInserting {key}...")

        # move all numbers bigger than key to the right
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            print("Shift:", arr)

        arr[j+1] = key
        print("Insert: ",arr)
    print("\nFinal sorted list: ", arr)
    return arr
#insertion_sort([5, 2, 4, 6])
#insertion_sort([5, 2, 4])

def insertion_sort_desc(arr):
    print("Start: ", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        print(f"\nInserting {key}...")

        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
            print("Shift: ", arr)
        
        arr[j+1] = key
        print("Insert: ", arr)
    print("\nFinal sorted list: ", arr)
#insertion_sort_desc([5,2,4,6])

def insert_into_sorted(arr, num):
    new_arr = arr
    for i in range(1, len(arr)):
        if num < arr[i]:
            new_arr = arr[:i] + [num] + arr[i:] 
            return new_arr
#print(insert_into_sorted([1,2,4,5], 3))

def insertion_sort_subarray(arr, left, right):
    for i in range(left, right+1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#print(insertion_sort_subarray([9,8,1,7,3,2,6], 2, 5))

def count_shifts_ins_sort(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] =  arr[j]
            shifts += 1
            j -= 1
        arr[j+1] = key
    return shifts
#nums_1 = [3,2,1]
#count = count_shifts_ins_sort(nums_1)
#print(f"Shifts: {count}; sorted array: {nums_1}")

def insertion_sort_key_print(arr):
    print("initial array:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"\nKey to be inserted: {key}...")
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"\nInserting the key into the list: {arr}")
    print(f"Sorted array: {arr}")
    return arr
#insertion_sort_key_print([4,3,1,2])

def count_inner_iterations(arr):
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            shifts += 1
            j -= 1
        arr[j+1] = key
    return shifts
#nums_2 = [4,3,2,1]
#print(count_inner_iterations(nums_2))
#print(nums_2)

def insertion_sort_adaptive(arr):
    sorted_flag = True
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted_flag = False
            break
    if sorted_flag:
        return arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
#print(insertion_sort_adaptive([1,2,3,4]))
#print(insertion_sort_adaptive([4,1,3,2]))


