"""
Task set for exam preparation (extracted from task-for-the-exam-preparation.pdf).

Rules from the sheet:
- For sorting tasks: return a NEW sorted list (do not modify input).
- For quick_sort_inplace: sort a COPY in-place, then return the sorted copy.
"""

# ============================================================
# Topic: Bubble Sort
# ============================================================
# Exercise 1:
#   Implement bubble sort to sort a list of integers in ascending order.
#   Return a NEW sorted list (do not modify the input list).

def bubble_sort_ascending(nums):
    """Return a new list with nums sorted ascending using Bubble Sort."""
    pass

# Exercise 2:
#   Optimize bubble sort: stop early if no swaps occurred in a pass (list already sorted).
#   Return a NEW sorted list.

def bubble_sort_optimized(nums):
    """Return a new list sorted with Bubble Sort; stop early when no swaps occur in a pass."""
    pass


# ============================================================
# Topic: Insertion Sort
# ============================================================
# Exercise 1:
#   Implement insertion sort in ascending order (non-destructive: return a new list).

def insertion_sort_ascending(nums):
    """Return a new list with nums sorted ascending using Insertion Sort."""
    pass

# Exercise 2:
#   Modify insertion sort to sort in DESCENDING order (return a new list).

def insertion_sort_descending(nums):
    """Return a new list with nums sorted descending using Insertion Sort."""
    pass


# ============================================================
# Topic: Merge Sort
# ============================================================
# Exercise 1:
#   Implement merge sort to sort a list of integers in ascending order.
#   Return a NEW sorted list.

def merge_sort(nums):
    """Return a new list with nums sorted ascending using Merge Sort (recursive)."""
    pass

# Exercise 2:
#   Write a function that MERGES two pre-sorted lists into one sorted list.

def merge_two_sorted_lists(a, b):
    """Merge two sorted lists a and b into one sorted list and return it."""
    pass


# ============================================================
# Topic: Binary Search
# ============================================================
# Exercise 1:
#   Implement iterative binary search that returns the index of the target
#   in a sorted list, or -1 if not found.

def binary_search(nums, target):
    """Return index of target in sorted nums using iterative Binary Search; -1 if absent."""
    pass

# Exercise 2:
#   Implement a function that returns the index of the FIRST occurrence
#   of a target in a sorted list that may contain duplicates.
#   If the target is absent, return the position where it should be inserted (lower bound).

def lower_bound(nums, target):
    """Return first index i such that nums[i] >= target (lower bound)."""
    pass


# ============================================================
# Topic: Stack
# ============================================================
# Exercise 1:
#   Implement a simple Stack class using Python's list with methods:
#   push, pop, peek, is_empty, size.

class Stack:
    """LIFO stack. Implement methods: push, pop, peek, is_empty, size."""
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

# Exercise 2:
#   Use a stack to check if a string has balanced parentheses/brackets/braces.
#   Return True if balanced, False otherwise.

def is_brackets_balanced(s):
    """Return True if s has balanced () [] {} using a stack; otherwise False."""
    pass


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
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def front(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

# Exercise 2:
# Implement a QueueUsingStacks class using two stacks (lists) to emulate FIFO.
# Methods: enqueue, dequeue, front, is_empty, size.

class QueueUsingStacks:
    """Queue implemented with two stacks. Implement enqueue, dequeue, front, is_empty, size."""
    def __init__(self):
        pass

    def enqueue(self, x):
        pass

    def dequeue(self):
        pass

    def front(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass


# ==============================================================================
# Topic: Quick Sort
# ==============================================================================
# Exercise 1:
# Implement quick sort (functional style) that returns a NEW sorted list
# using a pivot and list comprehensions (not in-place).

def quick_sort_functional(nums):
    """Return a new list sorted ascending using functional Quick Sort."""
    pass

# Exercise 2:
# Implement in-place quick sort using a partition scheme (e.g., Lomuto) but
# operate on a COPY of the input and return the sorted copy.

def quick_sort_inplace(nums):
    """Return a new sorted list produced by in-place Quick Sort on a copy of nums."""
    pass

