# A1 timed
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    while high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
#print(binary_search([1, 3, 3, 4, 12, 12, 12, 14], 3))

# B3 timed
def binary_search_lower_bound(arr, target, low=0, high=None):
    if high is None:
        high = len(arr)

    while high > low:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1

    return low
print(binary_search_lower_bound([1, 3, 3, 4, 12, 12, 12, 14], 15))
print(binary_search_lower_bound([1, 5, 10], 7))
