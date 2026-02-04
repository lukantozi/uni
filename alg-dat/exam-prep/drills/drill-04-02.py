# Daily drill: implement BASIC + 1 variant per topic (no sorted()).

#stack
#- BASIC: Valid brackets: (), {}, [].
def valid_brackets(seq):
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}
    if seq[0] not in match:
        return False
    stack.append(seq[0])

    for token in seq[1:]:
        if token in match:
            stack.append(token)
        elif token in match.values() and token != match[stack.pop()]:
            return False
    return len(stack) == 0

#- +1: Reverse a string.
def reverse_string(seq):
    stack = []
    for char in seq:
        stack.append(char)
    result = ""
    while stack:
        result += stack.pop()
    return result

TESTS = {"reverse": ["ainom", "hello"], "paren": ["(())", "(()", "(())()"], "brackets": ["()", "([])", "([{}])", "{[(])}", "((())"], "decimal": [13, 156, 0], "palindrome": ["madam", "racecar", "12321", "hello"], "adj_dupes": ["abbaca", "abba", "azxxzy"], "rpn": ["23+", "23*54-+", "52-", "5"], "stack_sort": [4, 3, 2, 1]} # ]]]]}}}}))))

#print(valid_brackets(TESTS["brackets"][0]))
#print(valid_brackets(TESTS["brackets"][1]))
#print(valid_brackets(TESTS["brackets"][2]))
#print(valid_brackets(TESTS["brackets"][3]))
#print(valid_brackets(TESTS["brackets"][4]))
#print(valid_brackets(["(.)"]))
#print(reverse_string(TESTS["reverse"][0]))
#print(reverse_string(TESTS["reverse"][1]))


#bubble_sort
#- BASIC: Implement bubble sort ascending (early-exit swapped flag).
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr
    return arr

#- +1: Last-swap boundary optimization.
def last_swap_bubble_sort(arr):
    pass
    # already implemented above?

TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 2, 1, 2, 1]]}

#print(bubble_sort(TESTS["lists"][0]))
#print(bubble_sort(TESTS["lists"][1]))
#print(bubble_sort(TESTS["lists"][2]))
#print(bubble_sort(TESTS["lists"][3]))

#binary_search
#- BASIC: Binary search (iterative) -> index or -1.
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
    


#- +1: First occurrence in duplicates.
def binary_first(arr, target, low=0, high=None):
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

TESTS = {"basic_case": {"arr": [11, 12, 22, 25, 34, 64, 90], "target": 25}, "not_found_case": {"arr": [10, 20, 30, 40, 60], "target": 50}, "dupes_case": {"arr": [1, 2, 2, 2, 3, 3], "target": 2}, "bounds_case": {"arr": [3, 3, 4, 12, 12, 12, 14], "target": 12}, "insert_middle": {"arr": [1, 5, 10], "target": 7}}
#print(binary_search(TESTS["basic_case"]["arr"], 12))
#print(binary_search(TESTS["basic_case"]["arr"], 22))
#print(binary_search(TESTS["basic_case"]["arr"], 91))
#print(binary_first(TESTS["dupes_case"]["arr"], 2))
#print(binary_first(TESTS["dupes_case"]["arr"], 3))

#quick_sort_3way
#- BASIC: Implement 3-way partition quicksort (less/equal/greater).
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    piv = arr[0]

    less = [x for x in arr if x < piv]
    equal = [x for x in arr if x == piv]
    more = [x for x in arr if x > piv]

    return quick_sort(less) + equal + quick_sort(more)

#- +1: Case-insensitive strings.
def quick_insen(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    piv = key(arr[0])
    less = [x for x in arr if key(x) < piv]
    equal = [x for x in arr if key(x) == piv]
    more = [x for x in arr if key(x) > piv]

    return quick_insen(less, key) + equal + quick_insen(more, key)

TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 5, 5, 5], [9, 7, 5, 3, 1], [1]], "strings": ["Bob", "alice", "Carol"], "abs_list": [-10, -3, 1, 2, -2, 5]}

#print(quick_sort(TESTS["lists"][0]))
#print(quick_sort(TESTS["lists"][1]))
#print(quick_sort(TESTS["lists"][2]))
#print(quick_sort(TESTS["lists"][3]))
#print(quick_insen(TESTS["strings"], key=str.lower))

#insertion_sort
#- BASIC: Implement insertion sort ascending (key + shifting).
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#- +1: Descending order.

def insertion_sort_desc(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 2, 4, 6], [4, 1, 3, 2], [1, 2, 3, 4]], "subarray_case": {"arr": [9, 8, 1, 7, 3, 2, 6], "l": 2, "r": 5}, "insert_case": {"arr": [1, 2, 4, 5], "x": 3}}

#print(insertion_sort(TESTS["lists"][0]))
#print(insertion_sort(TESTS["lists"][1]))
#print(insertion_sort_desc(TESTS["lists"][0]))
#print(insertion_sort_desc(TESTS["lists"][1]))

#merge_sort
#- BASIC: Implement top-down merge sort + merge helper.
def merge_sort(arr, key=lambda x: x):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left, key)
    merge_sort(right, key)
    merge(arr, left, right, key)

    return arr


def merge(arr, left, right, key):
    i, j, k = 0, 0, 0
    size_l = len(left)
    size_r = len(right)

    while i < size_l and j < size_r:
        if key(left[i]) < key(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < size_l:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < size_r:
        arr[k] = right[j]
        j += 1
        k += 1

#- +1: Case-insensitive string sort (key=str.lower).
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 1, 4, 2, 8], [-3, 10, 0, -1, 7]], "merge_two_lists": {"a": [1, 5, 12, 19, 25], "b": [3, 6, 14, 18, 23, 28]}, "strings": ["Bob", "alice", "Carol", "Ali", "Boo", "boo"], "tuples": [[3, "c"], [1, "a"], [2, "b"]]}

#print(merge_sort(TESTS["lists"][0]))
#print(merge_sort(TESTS["lists"][1]))
#print(merge_sort(TESTS["lists"][2]))
#print(merge_sort(TESTS["strings"], key=str.lower))
