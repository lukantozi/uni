def binary_search(arr, target):
    size = len(arr)
    mid = size // 2
    
    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        binary_search(arr[:mid], target)
    else:
        binary_search(arr[mid:], target)

    return -1
print(binary_search([3, 4, 12, 14, 1], 14))
