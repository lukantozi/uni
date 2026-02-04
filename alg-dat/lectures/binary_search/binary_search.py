def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (right + left) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [11, 12, 25, 22, 34, 64, 90]
print(binary_search(nums, 11))
print(binary_search(nums, 25))
print(binary_search(nums, 30))
