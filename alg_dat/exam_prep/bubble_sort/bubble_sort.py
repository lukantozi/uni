nums = [2, 4, 12, 9, 1, 3]

# layer A
def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(i, size):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if not swapped:
            return arr
    return arr
#print(bubble_sort(nums))

# layer B_1
def bubble_desc(arr):
    size = len(arr)
    for i in range(size):
        swapped = False
        for j in range(i, size):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if not swapped:
            return arr
    return arr
#print(bubble_desc(nums))
