numbers = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    n = len(arr)
    
    # outer loop runs n - 1 times
    for i in range(n-1):
        swapped = False
        for j in range(i, n-1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if not swapped:
            return arr
    return arr
#print(bubble_sort(numbers))

def merge_sort_trace(arr, depth=0):
    indent = " " * depth
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        print(f"{indent}Splitting: {arr} → Left: {left}, Right: {right}")
        depth += 1
        return merge(merge_sort_trace(left), merge_sort_trace(right), depth)
    return arr

def merge(left_l, right_l, depth):
    indent = " " * depth
    a = []
    i = 0
    j = 0
    print(f"{indent}Merging: Left={left_l}, Right={right_l}")
    while i < len(left_l) and j < len(right_l):
        if left_l[i] <= right_l[j]:
            a.append(left_l[i])
            i += 1
        else:
            a.append(right_l[j])
            j += 1
    while i < len(left_l):
        a.append(left_l[i])
        i += 1
    while j < len(right_l):
        a.append(right_l[j])
        j += 1
    return a
#print(merge_sort_trace(numbers))        

    
def quick_sort(arr, low, high, depth=0):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

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
#print(quick_sort(numbers, 0, len(numbers)-1))

def binary_search_trace(arr, target):
    left = 0
    right = len(arr) - 1
    step = 1

    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: Left={left}, Right={right}, Mid={mid}, MidValue={arr[mid]}")

        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        step += 1

    print(f"{target} not found in the list")
    return -1
#quick_sort(numbers, 0, len(numbers)-1)
#binary_search_trace(numbers, 22)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        ...

        print(f"Pushed {item} → Stack: {self.items}")

    def pop(self):
        ...

    def peek(self):
        ...

    def size(self):
        ...
