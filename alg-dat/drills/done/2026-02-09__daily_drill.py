from collections import deque
# Daily drill: implement BASIC + 1 variant per topic (no sorted()).

#bubble_sort
#- BASIC: Implement bubble sort ascending (early-exit swapped flag).
#- +1: Stop after k passes.
def bubble_sort(arr, k=None):
    n = len(arr)
    if k is None:
        k = n
    for i in range(k):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            return arr
    return arr
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 2, 1, 2, 1]]}

#print(bubble_sort(TESTS["lists"][0], 1))
#print(bubble_sort(TESTS["lists"][1]))
#print(bubble_sort(TESTS["lists"][2]))
#print(bubble_sort(TESTS["lists"][3]))

#insertion_sort
#- BASIC: Implement insertion sort ascending (key + shifting).
#- +1: Count shifts.
def insertion_sort(arr):
    n = len(arr)
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return arr, shifts

TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 2, 4, 6], [4, 1, 3, 2], [1, 2, 3, 4]], "subarray_case": {"arr": [9, 8, 1, 7, 3, 2, 6], "l": 2, "r": 5}, "insert_case": {"arr": [1, 2, 4, 5], "x": 3}}

#print(insertion_sort(TESTS["lists"][0])[0])
#print(insertion_sort(TESTS["lists"][1])[1])

#merge_sort
#- BASIC: Implement top-down merge sort + merge helper.
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(arr, left, right)
    
    return arr

def merge(arr, left, right):
    i, j, k = 0, 0, 0
    size_l = len(left)
    size_r = len(right)

    while i < size_l and j < size_r:
        if left[i] < right[j]:
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



#- +1: Merge two sorted lists helper (standalone).
def merge_two(arr1, arr2):
    size_1 = len(arr1)
    size_2 = len(arr2)
    arr = [None] * (size_1 + size_2)

    i, j, k = 0, 0, 0

    while i < size_1 and j < size_2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < size_1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < size_2:
        arr[k] = arr2[j]
        j += 1
        k += 1

    return arr

TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 1, 4, 2, 8], [-3, 10, 0, -1, 7]], "merge_two_lists": {"a": [1, 5, 12, 19, 25], "b": [3, 6, 14, 18, 23, 28]}, "strings": ["Bob", "alice", "Carol"], "tuples": [[3, "c"], [1, "a"], [2, "b"]]}

#print(merge_sort(TESTS["lists"][0]))
#print(merge_sort(TESTS["lists"][1]))
#print(merge_sort(TESTS["lists"][2]))

#print(merge_two(TESTS["merge_two_lists"]["a"], TESTS["merge_two_lists"]["b"]))

#quick_sort_3way
#- BASIC: Implement 3-way partition quicksort (less/equal/greater).
#- +1: Absolute value key.
def quicksort(arr, key=lambda x: x):
    if len(arr) <= 1:
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
#print(quicksort(TESTS["abs_list"], key=abs))

#stack
#- BASIC: Valid brackets: (), {}, [].
def valid_brackets(seq):
    stack = []
    match = {'(': ')', '[': ']', '{': '}'}

    for br in seq:
        if br in match:
            stack.append(br)
        else:
            if not stack:
                return False
            if br != match[stack.pop()]:
                return False

    return len(stack) == 0

#- +1: Remove adjacent duplicates.
TESTS = {"reverse": ["ainom", "hello"], "paren": ["(())", "(()", "(())()"], "brackets": ["()", "([])", "([{}])", "{[(])}", "((())"], "decimal": [13, 156, 0], "palindrome": ["madam", "racecar", "12321", "hello"], "adj_dupes": ["abbaca", "abba", "azxxzy"], "rpn": ["23+", "23*54-+", "52-", "5"], "stack_sort": [[4, 3, 2, 1]]} # ))))}}}}]]]]

#print(valid_brackets(TESTS["brackets"][0]))
#print(valid_brackets(TESTS["brackets"][1]))
#print(valid_brackets(TESTS["brackets"][2]))
#print(valid_brackets(TESTS["brackets"][3]))
#print(valid_brackets(TESTS["brackets"][4]))
#print(valid_brackets("as(()a)))"))
#print(valid_brackets("as(())"))


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

#- +1: Last occurrence in duplicates.
def binary_last(arr, target, low=0, high=None):
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

TESTS = {"basic_case": {"arr": [11, 12, 22, 25, 34, 64, 90], "target": 25}, "not_found_case": {"arr": [10, 20, 30, 40, 60], "target": 50}, "dupes_case": {"arr": [1, 2, 2, 2, 3], "target": 2}, "bounds_case": {"arr": [3, 3, 4, 12, 12, 12, 14], "target": 12}, "insert_middle": {"arr": [1, 5, 10], "target": 7}}

#print(binary_search(TESTS["basic_case"]["arr"], 22))
#print(binary_search(TESTS["basic_case"]["arr"], 2))
#print(binary_last(TESTS["dupes_case"]["arr"], 2))

#queue
#- BASIC: Implement queue using deque: enqueue, dequeue, front, is_empty, size.
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        raise ValueError("dequeue from empty queue")

    def front(self):
        if self.queue:
            return self.queue[0]
        raise ValueError("accessing an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
        

#- +1: Rotate left by k steps.
q_rot = Queue()
q_rot.enqueue(10)
q_rot.enqueue(20)
q_rot.enqueue(30)
q_rot.enqueue(40)
q_rot.enqueue(50)

def rotate_left(q_rot, k):
    while k > 0:
        q_rot.enqueue(q_rot.dequeue())
        k -= 1
    return q_rot.queue

#print(rotate_left(q_rot, 2))

TESTS = {"basic_ops": {"enqueue": [1, 2, 3, 4, 5], "dequeue_from": [10, 20, 30]}, "reverse": [1, 2, 3, 4], "compare": {"q1": [1, 2, 3], "q2": [1, 2, 3], "q3": [1, 3, 2]}, "max": [2, 9, 4, 7], "rotate": {"arr": [1, 2, 3, 4, 5], "k": 2}, "palindrome": {"valid": [1, 2, 3, 2, 1], "invalid": [1, 2, 3]}, "merge": {"q1": [1, 3, 5], "q2": [2, 4, 6, 8]}, "subsequence": {"small": [2, 5], "big": [1, 2, 3, 4, 5], "not_sub": [2, 6]}}

#q = Queue()
#q.enqueue(1)
#q.enqueue(2)
#q.enqueue(3)
#q.enqueue(4)
#q.enqueue(5)
#print(list(q.queue))

#q.enqueue(10)
#q.enqueue(20)
#q.enqueue(30)
#q.dequeue()
#print(list(q.queue))
#print(q.front())

#hashmaps
#- BASIC: Implement frequency counter using dict.
#- +1: Longest substring without repeating characters.
TESTS = {"frequency": [[1, 2, 2, 3, 3, 3], "hello", "mississippi"], "two_sum": [{"nums": [2, 7, 11, 15], "target": 9}, {"nums": [3, 2, 4], "target": 6}], "anagrams": [["eat", "tea", "tan", "ate", "nat", "bat"]], "longest_substring": ["abcabcbb", "bbbbb", "pwwkew"], "subarray_sum": [{"nums": [1, 1, 1], "k": 2}, {"nums": [1, 2, 3], "k": 3}], "first_non_repeat": ["leetcode", "loveleetcode", "aabb"], "anagram_check": [{"a": "listen", "b": "silent"}, {"a": "hello", "b": "world"}], "top_k": {"nums": [1, 1, 1, 2, 2, 3], "k": 2}, "intersect": [{"a": [1, 2, 2, 1], "b": [2, 2]}, {"a": [4, 9, 5], "b": [9, 4, 9, 8, 4]}], "duplicates": [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1, 2]], "missing": [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1]]}
