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

    while high >= low:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            while arr[mid] == target:
                mid -= 1
            return mid + 1

        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
#print(binary_search_first([1, 3, 3, 4, 12, 12, 12, 14], 3))

def binary_search_last(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    while high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            while arr[mid] == target:
                mid += 1
            return mid - 1
        elif arr[mid] > target:
            high = mid - 1 
        else:
            low = mid + 1
    return - 1
#print(binary_search_last([1, 3, 3, 4, 12, 12, 12, 14], 12))

def binary_low_bound(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    while high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            while arr[mid] == target:
                mid -= 1
            return mid + 1
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return len(arr) if arr[0] < target else 0
#print(binary_low_bound([3, 3, 4, 12, 12, 12, 14], 20))
