def quick_sort(arr, low, high, hashed_arr):
    if low < high:
        pi = partition(arr, low, high, hashed_arr)
        quick_sort(arr, low, pi - 1, hashed_arr)
        quick_sort(arr, pi + 1, high, hashed_arr)

def partition(arr, low, high, hashed_arr):
    pivot = hashed_arr[arr[high]]
    i = low - 1

    for j in range(low, high):
        if hashed_arr[arr[j]] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[high], arr[i + 1] = arr[i + 1], arr[high]
    return i + 1

arr = ["abcd", "as", "a", "annkds", "dfs"]
hashed_arr = {}
for i in arr:
    hashed_arr[i] = len(i)
quick_sort(arr, 0, len(arr)-1, hashed_arr)
print(arr)
