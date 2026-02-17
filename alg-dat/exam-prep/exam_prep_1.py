"""
Task set for exam preparation (extracted from task-for-the-exam-preparation.pdf).

Rules from the sheet:
- For sorting tasks: return a NEW sorted list (do not modify input).
- For quick_sort_inplace: sort a COPY in-place, then return the sorted copy.
"""

from typing import BinaryIO

# ============================================================
# Topic: Bubble Sort
# ============================================================
# Exercise 1:
#   Implement bubble sort to sort a list of integers in ascending order.
#   Return a NEW sorted list (do not modify the input list).

def bubble_sort_ascending(nums):
    arr = nums[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
        if swapped == False:
            return arr
    return arr

SORT_CASES = [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [64, 34, 25, 12, 22, 11, 90],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [2, 1, 2, 1, 2, 1],
    [0, -1, 5, -10, 3],
]

#print(bubble_sort_ascending(SORT_CASES[0]))
#print(bubble_sort_ascending(SORT_CASES[1]))
#print(bubble_sort_ascending(SORT_CASES[2]))
#print(bubble_sort_ascending(SORT_CASES[3]))
#print(bubble_sort_ascending(SORT_CASES[4]))

# Exercise 2:
#   Optimize bubble sort: stop early if no swaps occurred in a pass (list already sorted).
#   Return a NEW sorted list.

def bubble_sort_optimized(nums):
    """Return a new list sorted with Bubble Sort; stop early when no swaps occur in a pass."""
    # implemented above
    pass


# ============================================================
# Topic: Insertion Sort
# ============================================================
# Exercise 1:
#   Implement insertion sort in ascending order (non-destructive: return a new list).

def insertion_sort_ascending(nums):
    """Return a new list with nums sorted ascending using Insertion Sort."""
    n = len(nums)
    arr = nums[:]
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#print(insertion_sort_ascending(SORT_CASES[4]))

# Exercise 2:
#   Modify insertion sort to sort in DESCENDING order (return a new list).

def insertion_sort_descending(nums):
    """Return a new list with nums sorted descending using Insertion Sort."""
    n = len(nums)
    arr = nums[:]
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

#print(insertion_sort_descending(SORT_CASES[3]))
#print(insertion_sort_descending(SORT_CASES[4]))


# ============================================================
# Topic: Merge Sort
# ============================================================
# Exercise 1:
#   Implement merge sort to sort a list of integers in ascending order.
#   Return a NEW sorted list.

def merge_sort(nums):
    """Return a new list with nums sorted ascending using Merge Sort (recursive)."""
    n = len(nums)
    if n <= 1:
        return nums

    mid = n // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(nums, left, right)
    return nums

def merge(nums, left, right):
    i, j, k = 0, 0, 0
    size_l = len(left)
    size_r = len(right)

    while i < size_l and j < size_r:
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < size_l:
        nums[k] = left[i]
        i += 1
        k += 1

    while j < size_r:
        nums[k] = right[j]
        j += 1
        k += 1

MERGE_CASES = [
    ([1, 5, 12, 19, 25], [3, 6, 14, 18, 23, 28]),
    ([], []),
    ([1, 2, 2], [2, 3]),
    ([-5, 0, 7], [-10, -1, 8]),
]

#print(merge_sort(SORT_CASES[4]))
#print(merge_sort(SORT_CASES[3]))
#print(merge_sort(SORT_CASES[5]))

# Exercise 2:
#   Write a function that MERGES two pre-sorted lists into one sorted list.

def merge_two_sorted_lists(a, b):
    """Merge two sorted lists a and b into one sorted list and return it."""
    size_a = len(a)
    size_b = len(b)
    arr = [None] * (size_a + size_b)
    i, j, k = 0, 0, 0

    while i < size_a and j < size_b:
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < size_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < size_b:
        arr[k] = b[j]
        j += 1
        k += 1

    return arr

#print(merge_two_sorted_lists(MERGE_CASES[0][0], MERGE_CASES[0][1]))

# ============================================================
# Topic: Binary Search
# ============================================================
# Exercise 1:
#   Implement iterative binary search that returns the index of the target
#   in a sorted list, or -1 if not found.

def binary_search(nums, target):
    """Return index of target in sorted nums using iterative Binary Search; -1 if absent."""
    low, high = 0, len(nums) - 1 

    while high >= low:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

BINARY_SEARCH_CASES = [
    # (nums, target, expected_index)
    ([11, 12, 22, 25, 34, 64, 90], 11, 0),
    ([11, 12, 22, 25, 34, 64, 90], 25, 3),
    ([11, 12, 22, 25, 34, 64, 90], 90, 6),
    ([11, 12, 22, 25, 34, 64, 90], 13, -1),
    ([], 1, -1),
]

#print(binary_search(BINARY_SEARCH_CASES[0][0], BINARY_SEARCH_CASES[0][1]))
#print(binary_search(BINARY_SEARCH_CASES[0][0], BINARY_SEARCH_CASES[0][2]))
#print(binary_search(BINARY_SEARCH_CASES[1][0], BINARY_SEARCH_CASES[1][1]))
#print(binary_search(BINARY_SEARCH_CASES[1][0], BINARY_SEARCH_CASES[1][2]))
#print(binary_search(BINARY_SEARCH_CASES[4][0], BINARY_SEARCH_CASES[4][1]))

# Exercise 2:
#   Implement a function that returns the index of the FIRST occurrence
#   of a target in a sorted list that may contain duplicates.
#   If the target is absent, return the position where it should be inserted (lower bound).

def lower_bound(nums, target):
    """Return first index i such that nums[i] >= target (lower bound)."""
    low, high = 0, len(nums)

    while high > low:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

LOWER_BOUND_CASES = [
    # (nums, target, expected_index)
    ([1, 2, 2, 2, 3], 0, 0),
    ([1, 2, 2, 2, 3], 1, 0),
    ([1, 2, 2, 2, 3], 2, 1),
    ([1, 2, 2, 2, 3], 3, 4),
    ([1, 2, 2, 2, 3], 4, 5),
    ([], 10, 0),
]

#print(lower_bound(LOWER_BOUND_CASES[0][0], 0))
#print(lower_bound(LOWER_BOUND_CASES[1][0], 1))
#print(lower_bound(LOWER_BOUND_CASES[2][0], 2))
#print(lower_bound(LOWER_BOUND_CASES[3][0], 3))

# ============================================================
# Topic: Stack
# ============================================================
# Exercise 1:
#   Implement a simple Stack class using Python's list with methods:
#   push, pop, peek, is_empty, size.

class Stack:
    """LIFO stack. Implement methods: push, pop, peek, is_empty, size."""
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise ValueError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise ValueError("peek from empty stack")

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)


STACK_OPS = [
    # ops: ("push", x) or ("pop", None) or ("peek", None)
    # expected outputs only for pop/peek in order
    ([("push", 10), ("push", 20), ("peek", None), ("pop", None), ("pop", None)], [20, 20, 10]),
]

#s = Stack()
#s.push(10)
#print(s.stack)
#s.push(22)
#print(s.stack)
#print(s.peek())

# Exercise 2:
    #   Use a stack to check if a string has balanced parentheses/brackets/braces.
    #   Return True if balanced, False otherwise.
def is_brackets_balanced(s):
    """Return True if s has balanced () [] {} using a stack; otherwise False."""
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}

    for br in s:
        if br in match:
            stack.append(br)
        else:
            if not stack:
                return False
            if br != match[stack.pop()]:
                return False
    return len(stack) == 0

BRACKETS_CASES = [
    ("()", True),
    ("([])", True),
    ("([{}])", True),
    ("{[(])}", False),
    ("((())", False),
    ("", True),
] # )))))]]]]]]}]}}}}

#print(is_brackets_balanced(BRACKETS_CASES[0][0]))
#print(is_brackets_balanced(BRACKETS_CASES[1][0]))
#print(is_brackets_balanced(BRACKETS_CASES[2][0]))
#print(is_brackets_balanced(BRACKETS_CASES[3][0]))
#print(is_brackets_balanced(BRACKETS_CASES[4][0]))
#print(is_brackets_balanced(BRACKETS_CASES[5][0]))

# ==============================================================================
# Topic: Queue
# ==============================================================================
# Exercise 1:
# Implement a simple Queue class (FIFO). Suggested: use collections.deque.
# Methods: enqueue, dequeue, front, is_empty, size.

from collections import deque

class Queue:
    """FIFO queue. Implement methods: enqueue, dequeue, front, is_empty, size."""
    def __init__(self):
        self.q = deque()

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.q.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.q[0]
        return None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.q)

QUEUE_OPS = [
    # ops: ("enq", x) ("deq", None) ("front", None)
    # expected outputs only for deq/front in order
    ([("enq", 1), ("enq", 2), ("enq", 3), ("front", None), ("deq", None), ("front", None), ("deq", None), ("deq", None)],
     [1, 1, 2, 2, 3]),
]

#q = Queue()
#q.enqueue(1)
#print(q.q)
#q.enqueue(2)
#print(q.q)
#print(q.front())
#print(q.q)
#print(q.dequeue())
#print(q.q)
#print(q.dequeue())
#print(q.dequeue())

# Exercise 2:
# Implement a QueueUsingStacks class using two stacks (lists) to emulate FIFO.
# Methods: enqueue, dequeue, front, is_empty, size.

class QueueUsingStacks:
    """Queue implemented with two stacks. Implement enqueue, dequeue, front, is_empty, size."""
    def __init__(self):
        self.stack_in = []
        self.stack_ou = []

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        if not self.stack_ou:
            while self.stack_in:
                self.stack_ou.append(self.stack_in.pop())
        return self.stack_ou.pop()

    def front(self):
        if not self.stack_ou:
            while self.stack_in:
                self.stack_ou.append(self.stack_in.pop())
        return self.stack_ou[-1]

    def is_empty(self):
        return self.size() == 0


    def size(self):
        return len(self.stack_in) + len(self.stack_ou)

QUEUE_STACKS_OPS = [
    ([("enq", 1), ("enq", 2), ("enq", 3), ("front", None), ("deq", None), ("front", None), ("deq", None), ("deq", None)],
     [1, 1, 2, 2, 3]),
]

#q = QueueUsingStacks()
#for i in range(1, 4):
#    q.enqueue(i*10)
#print(q.stack_in)
#print(q.dequeue())
#print(q.stack_in)
#print(q.stack_ou)
#print(q.dequeue())
#print(q.stack_ou)

# ==============================================================================
# Topic: Quick Sort
# ==============================================================================
# Exercise 1:
# Implement quick sort (functional style) that returns a NEW sorted list
# using a pivot and list comprehensions (not in-place).

def quick_sort_functional(nums):
    """Return a new list sorted ascending using functional Quick Sort."""
    if len(nums) <= 1:
        return nums
    
    piv = nums[0]
    less = [x for x in nums if x < piv]
    equal = [x for x in nums if x == piv]
    more = [x for x in nums if x > piv]

    return quick_sort_functional(less) + equal + quick_sort_functional(more)

SORT_CASES = [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [64, 34, 25, 12, 22, 11, 90],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [2, 1, 2, 1, 2, 1],
    [0, -1, 5, -10, 3],
]

#print(quick_sort_functional(SORT_CASES[0]))
#print(quick_sort_functional(SORT_CASES[1]))
#print(quick_sort_functional(SORT_CASES[2]))
#print(quick_sort_functional(SORT_CASES[3]))
#print(quick_sort_functional(SORT_CASES[4]))
#print(quick_sort_functional(SORT_CASES[5]))
#print(quick_sort_functional(SORT_CASES[6]))
#print(quick_sort_functional(SORT_CASES[7]))
#print(quick_sort_functional(SORT_CASES[8]))

# Exercise 2:
# Implement in-place quick sort using a partition scheme (e.g., Lomuto) but
# operate on a COPY of the input and return the sorted copy.

def quick_sort_inplace(nums, low=0, high=None):
    """Return a new sorted list produced by in-place Quick Sort on a copy of nums."""
    if high is None:
        high = len(nums) - 1

    if high > low:
        pi = partition(nums, low, high)
        quick_sort_inplace(nums, low, pi - 1)
        quick_sort_inplace(nums, pi + 1, high)

    return nums

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if pivot > arr[j]:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
#print(quick_sort_inplace(SORT_CASES[0]))
#print(quick_sort_inplace(SORT_CASES[1]))
#print(quick_sort_inplace(SORT_CASES[2]))
#print(quick_sort_inplace(SORT_CASES[3]))
#print(quick_sort_inplace(SORT_CASES[4]))
