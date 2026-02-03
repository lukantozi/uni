def binary_search(arr, target):
    left, right = 0, len(arr)-1
    first = 0

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return first

arr = [1, 2, 2, 2, 3]
print(binary_search(arr, 2))
