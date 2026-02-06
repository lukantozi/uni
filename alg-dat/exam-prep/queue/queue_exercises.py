"""
QUEUE EXERCISES - Python Practice
Using collections.deque for FIFO operations
"""

from collections import deque


# ==============================================================================
# BASIC OPERATIONS
# ==============================================================================

def exercise_1_create_and_enqueue():
    """
    Create a queue and enqueue numbers 1-5, then print it.
    """
    pass


def exercise_2_dequeue_operation():
    """
    Implement dequeue operation and print all removed elements.
    Input: deque([10, 20, 30])
    Expected output: [10, 20, 30] (in order), queue should be empty after
    """
    pass


def exercise_3_check_empty(q: deque) -> bool:
    """
    Check if a queue is empty.
    """
    pass


def exercise_4_front(q: deque):
    """
    Return the first element without removing it.
    Return None if empty.
    """
    pass


def exercise_5_size(q: deque) -> int:
    """
    Return the number of elements in the queue.
    """
    pass


# ==============================================================================
# INTERMEDIATE OPERATIONS
# ==============================================================================

def exercise_6_reverse_queue(q: deque):
    """
    Reverse a queue using an auxiliary stack.
    Input: deque([1, 2, 3, 4])
    Expected output: deque([4, 3, 2, 1])
    Modifies the queue in-place.
    """
    pass


def exercise_7_copy_queue(q: deque) -> deque:
    """
    Copy a queue without modifying the original.
    """
    pass


def exercise_8_queues_equal(q1: deque, q2: deque) -> bool:
    """
    Compare two queues for equality without altering them.
    Input: q1 = deque([1, 2, 3]), q2 = deque([1, 2, 3])
    Expected: True
    """
    pass


def exercise_9_print_and_empty(q: deque):
    """
    Dequeue all elements and print them one by one.
    """
    pass


def exercise_10_max_in_queue(q: deque):
    """
    Find the maximum element in a queue without destroying it.
    """
    pass


# ==============================================================================
# ADVANCED OPERATIONS
# ==============================================================================

def exercise_11_rotate_left(q: deque, k: int):
    """
    Rotate a queue left by k steps (move front element to back, k times).
    Input: deque([1, 2, 3, 4, 5]), k=2
    Expected: deque([3, 4, 5, 1, 2])
    Modifies the queue in-place.
    """
    pass


def exercise_12_is_palindrome_sequence(seq: list) -> bool:
    """
    Check if a sequence is a palindrome using a queue and stack.
    Input: [1, 2, 3, 2, 1]
    Expected: True
    """
    pass


def exercise_13_merge_alternating(q1: deque, q2: deque) -> deque:
    """
    Merge two queues into one, alternating elements.
    Input: q1 = deque([1, 3, 5]), q2 = deque([2, 4, 6, 8])
    Expected: deque([1, 2, 3, 4, 5, 6, 8])
    """
    pass


def exercise_14_is_subsequence_queue(small: deque, big: deque) -> bool:
    """
    Check if one queue is a subsequence of another.
    Note: Subsequence means all elements of small appear in big in order,
    not necessarily contiguously.
    Input: small = deque([2, 5]), big = deque([1, 2, 3, 4, 5])
    Expected: True
    """
    pass


# ==============================================================================
# CHALLENGE PROBLEMS
# ==============================================================================

def exercise_15_supermarket_simulation(customers: list) -> float:
    """
    Given a list of (arrival_time, service_time), simulate a single cashier queue.
    Compute each customer's start time, finish time, and waiting time.
    Return the average waiting time.

    Example input: [(0, 5), (2, 3), (4, 2)]
    """
    pass


class TwoQueuesOneList:
    """
    Exercise 16: Implement two independent FIFO queues in a single array.
    One queue grows from the left, one from the right.
    """
    def __init__(self, capacity: int):
        pass

    def enqueue1(self, x):
        pass

    def enqueue2(self, x):
        pass

    def dequeue1(self):
        pass

    def dequeue2(self):
        pass


class QueueUsingTwoStacks:
    """
    Exercise 17: Implement a queue using two stacks.
    Hint: One stack for enqueue, one for dequeue operations.
    """
    def __init__(self):
        pass

    def enqueue(self, x):
        pass

    def dequeue(self):
        pass

    def is_empty(self) -> bool:
        pass


# ==============================================================================
# DEMO / TESTING
# ==============================================================================

if __name__ == "__main__":
    # Test your solutions here
    print("Queue exercises ready!")

    # Example:
    # q = deque([1, 2, 3])
    # print(exercise_5_size(q))
