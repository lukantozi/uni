# Daily drill: implement BASIC + 1 variant per topic (no sorted()).

#stack
#- BASIC: Valid brackets: (), {}, [].
def valid_brackets(seq):
    stack = []
    match = {"(": ")", "{": "}", "[": "]"}

    if seq[0] not in match:
        return False
    stack.append(seq[0])

    for br in seq[1:]:
        if br in match:
            stack.append(br)
        elif br in match.values() and br != match[stack.pop()]:
            return False
    return len(stack) == 0

#- +1: Evaluate postfix (RPN).
def eval_postfix(seq):
    stack = []
    for token in seq:
        if token.isdigit():
            stack.append(token)
        elif stack:
            match token:
                case "+":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a+b)
                case "-":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a-b)
                case "*":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a*b)
                case "/":
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a//b)
        else:
            return f"invalid operation"
    return stack[0]

#def eval_postfix(seq):
#    stack = []
#    for token in seq:
#        if token.isdigit():
#            stack.append(int(token))  # push as int directly
#        else:
#            if len(stack) < 2:
#                return "invalid: not enough operands"
#            b = stack.pop()
#            a = stack.pop()
#            match token:
#                case "+": stack.append(a + b)
#                case "-": stack.append(a - b)
#                case "*": stack.append(a * b)
#                case "/": stack.append(a // b)
#    return stack[0] if stack else "invalid: empty result"



TESTS = {"reverse": ["ainom", "hello"], "paren": ["(())", "(()", "(())()"], "brackets": ["()", "([])", "([{}])", "{[(])}", "((())"], "decimal": [13, 156, 0], "palindrome": ["madam", "racecar", "12321", "hello"], "adj_dupes": ["abbaca", "abba", "azxxzy"], "rpn": ["23+", "23*54-+", "52-", "5"], "stack_sort": [4, 3, 2, 1]} # ))))}}}}]]]]

#print(valid_brackets(TESTS["brackets"][0]))
#print(valid_brackets(TESTS["brackets"][1]))
#print(valid_brackets(TESTS["brackets"][2]))
#print(valid_brackets(TESTS["brackets"][3]))
#print(valid_brackets(TESTS["brackets"][4]))

#print(eval_postfix(TESTS["rpn"][0]))
#print(eval_postfix(TESTS["rpn"][1]))
#print(eval_postfix(TESTS["rpn"][2]))
#print(eval_postfix(TESTS["rpn"][3]))

#bubble_sort
#- BASIC: Implement bubble sort ascending (early-exit swapped flag).
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr
    return arr


#- +1: Descending order.
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n -1):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr
    return arr


TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 2, 1, 2, 1]]}

#print(bubble_sort(TESTS["lists"][0]))
#print(bubble_sort(TESTS["lists"][1]))
#print(bubble_sort(TESTS["lists"][2]))
#print(bubble_sort(TESTS["lists"][3]))

#print(bubble_sort_desc(TESTS["lists"][0]))
#print(bubble_sort_desc(TESTS["lists"][1]))
#print(bubble_sort_desc(TESTS["lists"][2]))
#print(bubble_sort_desc(TESTS["lists"][3]))


#binary_search
#- BASIC: Binary search (iterative) -> index or -1.
def binary_search(arr, target):
    n = len(arr)
    low = 0
    high = n - 1

    while high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

#- +1: Upper bound (first index with value > target).
def binary_upper(arr, target):
    n = len(arr)
    low = 0
    high = n - 1

    result = -1
    while high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid + 1
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

#def binary_upper(arr, target):
#    low, high = 0, len(arr)  # note: high = len(arr), not len(arr)-1
#    
#    while low < high:  # note: <, not <=
#        mid = low + (high - low) // 2
#        if arr[mid] <= target:  # ← key change: <= (not ==)
#            low = mid + 1
#        else:
#            high = mid
#    return low



TESTS = {"basic_case": {"arr": [11, 12, 22, 25, 34, 64, 90], "target": 25}, "not_found_case": {"arr": [10, 20, 30, 40, 60], "target": 50}, "dupes_case": {"arr": [1, 2, 2, 2, 3], "target": 2}, "bounds_case": {"arr": [3, 3, 4, 12, 12, 12, 14], "target": 12}, "insert_middle": {"arr": [1, 5, 10], "target": 7}}

#print(binary_search(TESTS["basic_case"]["arr"], 23))
#print(binary_search(TESTS["basic_case"]["arr"], 22))

#print(binary_upper(TESTS["bounds_case"]["arr"], 15))

#merge_sort
#- BASIC: Implement top-down merge sort + merge helper.
#- +1: Sort by absolute value.
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

TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 1, 4, 2, 8], [-3, 10, 0, -1, 7]], "merge_two_lists": {"a": [1, 5, 12, 19, 25], "b": [3, 6, 14, 18, 23, 28]}, "strings": ["Bob", "alice", "Carol"], "tuples": [[3, "c"], [1, "a"], [2, "b"]]}

#print(merge_sort(TESTS["lists"][0]))
#print(merge_sort(TESTS["lists"][1]))
##print(merge_sort(TESTS["lists"][2]))
#print(merge_sort(TESTS["lists"][2], key=abs))

#quick_sort_3way
#- BASIC: Implement 3-way partition quicksort (less/equal/greater).
#- +1: Case-insensitive strings.
def quicksort(arr, key=lambda x: x):
    n = len(arr)
    if n <= 1:
        return arr

    piv = key(arr[0])

    less = [x for x in arr if key(x) < piv]
    equal = [x for x in arr if key(x) == piv]
    more = [x for x in arr if key(x) > piv]

    return quicksort(less, key) + equal + quicksort(more, key)

TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 5, 5, 5], [9, 7, 5, 3, 1], [1]], "strings": ["Bob", "alice", "Carol"], "abs_list": [-10, -3, 1, 2, -2, 5]}

#print(quicksort(TESTS["lists"][0]))
#print(quicksort(TESTS["lists"][1]))
#print(quicksort(TESTS["lists"][2]))
#print(quicksort(TESTS["lists"][3]))
#print(quicksort(TESTS["strings"], key=str.lower))

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

#- +1: Insert one value into sorted list.
def insert_into_sorted(arr, value):
    arr.append(value)
    i = len(arr) - 2

    while i >= 0 and arr[i] > value:
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = value
    return arr

TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 2, 4, 6], [4, 1, 3, 2], [1, 2, 3, 4]], "subarray_case": {"arr": [9, 8, 1, 7, 3, 2, 6], "l": 2, "r": 5}, "insert_case": {"arr": [1, 2, 4, 5, 9, 12], "x": 3}}

#print(insertion_sort(TESTS["lists"][0]))
#print(insertion_sort(TESTS["lists"][1]))
#print(insertion_sort(TESTS["lists"][2]))
#print(insertion_sort(TESTS["lists"][3]))

#print(insert_into_sorted(TESTS["insert_case"]["arr"], 10))
#print(insert_into_sorted(TESTS["insert_case"]["arr"], 13))
#print(insert_into_sorted(TESTS["insert_case"]["arr"], -1))
