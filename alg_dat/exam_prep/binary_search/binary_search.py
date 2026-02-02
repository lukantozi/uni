def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr, target, mid+1, high)
    else:
        return -1
#print(binary_search([1, 3, 4, 12, 14], 5))
def binary_search_first(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    result = -1
    while high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

#print(binary_search_first([1, 3, 3, 4, 12, 12, 12, 14], 3))
#print(binary_search_first([3,3,3],3))

def binary_search_last(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    result = -1
    while high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1 
        else:
            low = mid + 1
    return result
#print(binary_search_last([1, 3, 3, 4, 12, 12, 12, 14], 12))
#print(binary_search_last([3,3,3],3))

def binary_low_bound(arr, target, low=0, high=None):
    if high is None:
        high = len(arr)
    
    while high > low:
        mid = low + (high - low) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low
print(binary_low_bound([3, 3, 4, 12, 12, 12, 14], 4))

def binary_high_bound(arr, target, low=0, high=None):
    if high is None:
        high = len(arr)
    
    while high > low:
        mid = low + (high - low) // 2

        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return high 
print(binary_high_bound([3, 3, 4, 12, 12, 12, 14], 12))
