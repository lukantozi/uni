def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    first = -1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return first


def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    last = -1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return last

def count_occurences(arr, target):
    first = binary_search_first(arr, target)
    last = binary_search_last(arr, target)
    return last - first + 1

arr = [1, 2, 2, 2, 3]
print(count_occurences(arr, 2))
