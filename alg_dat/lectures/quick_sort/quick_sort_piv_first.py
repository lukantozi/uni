def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[low]

    start = low + 1
    end  = high
    
    while True:
        while start <= end and arr[end] >= pivot:
            end -= 1

        while start <= end and arr[start] <= pivot:
            start += 1

        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break
    arr[low], arr[end] = arr[end], arr[low]
    return end

arr = [9, 4, 1, 10, 12, 2, 3]
quick_sort(arr, 0, len(arr)-1)
print(arr)
