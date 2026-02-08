from collections import deque
# Daily drill: implement BASIC + 1 variant per topic (no sorted()).

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

#- +1: Sort tuples by second element.
TESTS = {"lists": [[64, 34, 25, 12, 12, 22, 11, 90], [5, 1, 4, 2, 8], [-3, 10, 0, -1, 7]], "merge_two_lists": {"a": [1, 5, 12, 19, 25], "b": [3, 6, 14, 18, 23, 28]}, "strings": ["Bob", "alice", "Carol"], "tuples": [[3, "c"], [1, "b"], [2, "a"]]}

#print(merge_sort(TESTS["lists"][0]))
#print(merge_sort(TESTS["lists"][1]))
#print(merge_sort(TESTS["lists"][2]))
#print(merge_sort(TESTS["tuples"], key=lambda x: x[1]))

#stack
#- BASIC: Valid brackets: (), {}, [].
def valid_brack(seq):
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}

    if seq[0] not in match:
        return False
    stack.append(seq[0])

    for br in seq[1:]:
        if br in match:
            stack.append(br)
        elif br in match.values() and br != match[stack.pop()]:
            return False
    return len(stack) == 0

#- +1: Remove adjacent duplicates.
def rem_adj(seq):
    if not seq:
        return "" # add for safety
    stack = []
    stack.append(seq[0])
    for tok in seq[1:]:
        if not stack or (stack and tok != stack[-1]):
            stack.append(tok)
        elif stack and tok == stack[-1]:
            stack.pop()
    return "".join(stack)

TESTS = {"reverse": ["ainom", "hello"], "paren": ["(())", "(()", "(())()"], "brackets": ["()", "([])", "([{}])", "{[(])}", "((())"], "decimal": [13, 156, 0], "palindrome": ["madam", "racecar", "12321", "hello"], "adj_dupes": ["abbaca", "abba", "azxxzy"], "rpn": ["23+", "23*54-+", "52-", "5"], "stack_sort": [4, 3, 2, 1]} # }}}}]]]))))

#print(valid_brack(TESTS["brackets"][0]))
#print(valid_brack(TESTS["brackets"][1]))
#print(valid_brack(TESTS["brackets"][2]))
#print(valid_brack(TESTS["brackets"][3]))
#print(valid_brack(TESTS["brackets"][4]))

#print(rem_adj(TESTS["adj_dupes"][0]))
#print(rem_adj(TESTS["adj_dupes"][1]))
#print(rem_adj(TESTS["adj_dupes"][2]))


#binary_search
#- BASIC: Binary search (iterative) -> index or -1.
def binary_search(arr, target):
    high = len(arr) - 1
    low = 0
    
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
def upper_bound(arr, target):
    high = len(arr)
    low = 0
    
    while high > low:
        mid = low + (high - low) // 2
        
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid # was writing "mid - 1", but need to assign mid
    return low

TESTS = {"basic_case": {"arr": [11, 12, 22, 25, 34, 64, 90], "target": 25}, "not_found_case": {"arr": [10, 20, 30, 40, 60], "target": 50}, "dupes_case": {"arr": [1, 2, 2, 2, 3], "target": 2}, "bounds_case": {"arr": [3, 3, 4, 12, 12, 12, 14], "target": 12}, "insert_middle": {"arr": [1, 5, 10], "target": 7}}

#print(binary_search(TESTS["basic_case"]["arr"], 90))
#print(binary_search(TESTS["basic_case"]["arr"], 11))
#print(upper_bound(TESTS["bounds_case"]["arr"], 3))
#print(upper_bound(TESTS["bounds_case"]["arr"], 4)) # i am not sure why this gives 2, it is supposedly a correct solution

#queue
#- BASIC: Implement queue using deque: enqueue, dequeue, front, is_empty, size.
class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.q.popleft()
        raise ValueError("can't deque, queue is empty")

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.q)

    def front(self):
        if not self.is_empty():
            return self.q[0]

#- +1: Reverse queue using stack. (I don't understand significance of this exercise, what skill of mine are we checking exactly?)
def reverse_queue_with_stack(q):
    dq = deque(q)
    stack = []
    while dq:
        stack.append(dq.pop())
    return stack



TESTS = {"basic_ops": {"enqueue": [1, 2, 3, 4, 5], "dequeue_from": [10, 20, 30]}, "reverse": [1, 2, 3, 4], "compare": {"q1": [1, 2, 3], "q2": [1, 2, 3], "q3": [1, 3, 2]}, "max": [2, 9, 4, 7], "rotate": {"arr": [1, 2, 3, 4, 5], "k": 2}, "palindrome": {"valid": [1, 2, 3, 2, 1], "invalid": [1, 2, 3]}, "merge": {"q1": [1, 3, 5], "q2": [2, 4, 6, 8]}, "subsequence": {"small": [2, 5], "big": [1, 2, 3, 4, 5], "not_sub": [2, 6]}}

#q = Queue()
#q.enqueue(10)
#q.enqueue(11)
#q.enqueue(12)
#q.enqueue(13)
#print(q.q)
#q.dequeue()
#print(q.q)
#q.dequeue()
#print(q.q)

#print(reverse_queue_with_stack(TESTS["reverse"]))

#bubble_sort
#- BASIC: Implement bubble sort ascending (early-exit swapped flag).
def bubble_sort(arr):
    n = len(arr)
    comp = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr, comp
    return arr, comp

#- +1: Count comparisons.
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 2, 1, 2, 1]]}

#print(bubble_sort(TESTS["lists"][0])[1])
#print(bubble_sort(TESTS["lists"][1])[1])
#print(bubble_sort(TESTS["lists"][2])[1])
#print(bubble_sort(TESTS["lists"][3])[1])
#print(TESTS["lists"][0])
#print(TESTS["lists"][1])
#print(TESTS["lists"][2])
#print(TESTS["lists"][3])

#quick_sort_3way
#- BASIC: Implement 3-way partition quicksort (less/equal/greater).
def quicksort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    piv = key(arr[0])
    less = [x for x in arr if key(x) < piv]
    equal = [x for x in arr if key(x) == piv]
    more  = [x for x in arr if key(x) > piv]
    return quicksort(less, key) + equal + quicksort(more, key)

#- +1: Case-insensitive strings.
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 5, 5, 5], [9, 7, 5, 3, 1], [1]], "strings": ["Bob", "alice", "Carol"], "abs_list": [-10, -3, 1, 2, -2, 5]}

#print(quicksort(TESTS["lists"][0]))
#print(quicksort(TESTS["lists"][1]))
#print(quicksort(TESTS["lists"][2]))
#print(quicksort(TESTS["lists"][3]))
#print(quicksort(TESTS["strings"], key=str.lower))

#insertion_sort
#- BASIC: Implement insertion sort ascending (key + shifting).
def insertion_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    for i in range(1, high+1):
        key = arr[i]
        j = i - 1

        while j >= low and arr[j] > key:
           arr[j+1] = arr[j] 
           j -= 1
        arr[j+1] = key
    return arr
#- +1: Sort subarray l..r.
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 2, 4, 6], [4, 1, 3, 2], [1, 2, 3, 4]], "subarray_case": {"arr": [9, 8, 1, 7, 3, 2, 6], "l": 2, "r": 5}, "insert_case": {"arr": [1, 2, 4, 5], "x": 3}}

#print(insertion_sort(TESTS["lists"][0]))
#print(insertion_sort(TESTS["lists"][1]))
#print(insertion_sort(TESTS["lists"][2]))
#print(insertion_sort(TESTS["lists"][3]))
#print(insertion_sort(TESTS["subarray_case"]["arr"], 2, 5))
