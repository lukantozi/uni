"""
QUEUE EXERCISES - Python Practice
Using collections.deque for FIFO operations
"""

from collections import deque
from sys import exception
from typing import TextIO


# ==============================================================================
# BASIC OPERATIONS
# ==============================================================================

def exercise_1_create_and_enqueue():
    """
    Create a queue and enqueue numbers 1-5, then print it.
    """
    q = deque()
    for i in range(1, 6):
        q.append(i)
    print(q)


def exercise_2_dequeue_operation(q):
    """
    Implement dequeue operation and print all removed elements.
    Input: deque([10, 20, 30])
    Expected output: [10, 20, 30] (in order), queue should be empty after
    """
    out = []
    while q:
        out.append(q.popleft())
    return out

def exercise_3_check_empty(q: deque) -> bool:
    """
    Check if a queue is empty.
    """
    return len(q) == 0
    


def exercise_4_front(q: deque):
    """
    Return the first element without removing it.
    Return None if empty.
    """
    return None if len(q) == 0 else q[0]


def exercise_5_size(q: deque) -> int:
    """
    Return the number of elements in the queue.
    """
    return len(q)



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
    q.reverse()
    return q


def exercise_7_copy_queue(q: deque) -> deque:
    """
    Copy a queue without modifying the original.
    """
    cp = q.copy()
    return cp


def exercise_8_queues_equal(q1: deque, q2: deque) -> bool:
    """
    Compare two queues for equality without altering them.
    Input: q1 = deque([1, 2, 3]), q2 = deque([1, 2, 3])
    Expected: True
    """
    return True if q1 == q2 else False


def exercise_9_print_and_empty(q: deque):
    """
    Dequeue all elements and print them one by one.
    """
    while q:
        print(q.popleft())


def exercise_10_max_in_queue(q: deque):
    """
    Find the maximum element in a queue without destroying it.
    """
    return max(q)


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
    q.rotate(-k)
    return q

def exercise_12_is_palindrome_sequence(seq: list) -> bool:
    """
    Check if a sequence is a palindrome using a queue and stack.
    Input: [1, 2, 3, 2, 1]
    Expected: True
    """
    q = deque(seq)
    while q and seq:
        if seq.pop() != q.popleft():
            return False

    return len(q) == len(seq) == 0


def exercise_13_merge_alternating(q1: deque, q2: deque) -> deque:
    """
    Merge two queues into one, alternating elements.
    Input: q1 = deque([1, 3, 5]), q2 = deque([2, 4, 6, 8])
    Expected: deque([1, 2, 3, 4, 5, 6, 8])
    """
    size_1 = len(q1)
    size_2 = len(q2)
    merged = deque()
    i, j = 0, 0

    while i < size_1 and j < size_2:
        merged.append(q1.popleft())
        merged.append(q2.popleft())
        i += 1
        j += 1
    while i < size_1:
        merged.append(q1.popleft())
        i += 1
    while j < size_2:
        merged.append(q2.popleft())
        j += 1
    return merged

    


def exercise_14_is_subsequence_queue(small: deque, big: deque) -> bool:
    """
    Check if one queue is a subsequence of another.
    Note: Subsequence means all elements of small appear in big in order,
    not necessarily contiguously.
    Input: small = deque([2, 5]), big = deque([1, 2, 3, 4, 5])
    Expected: True
    """
    for token in big:
        if token in small:
            small.remove(token)
    return len(small) == 0

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
    finish = customers[0][0]
    for n, cust in enumerate(customers):
        start = max(finish, cust[0])
        wait = start - cust[0]
        finish = start + cust[1]
        print(f"Customer {n+1}:\n{10*'='}\nStarted at: {start}\nWaited for: {wait}\nFinished at: {finish}\n")


class TwoQueuesOneList:
    """
    Exercise 16: Implement two independent FIFO queues in a single array.
    One queue grows from the left, one from the right.
    """
    def __init__(self, capacity: int):
        self.q = deque([0])
        self.capacity = capacity
        self.left_count = 0
        self.right_count = 0


    def enqueue1(self, x):
        if self.capacity > 0:
            self.q.appendleft(x)
            self.left_count += 1
            self.capacity -= 1 
        else:
            print("Not enough space")

    def enqueue2(self, x):
        if self.capacity > 0:
            self.q.append(x)
            self.right_count += 1
            self.capacity -= 1 
        else:
            print("Not enough space")

    def dequeue1(self):
        if self.left_count > 0:
            self.q.popleft()
            self.left_count -= 1
            self.capacity += 1
        else:
            print("Nothing in the left array")


    def dequeue2(self):
        if self.right_count > 0:
            self.q.pop()
            self.right_count -= 1
            self.capacity += 1
        else:
            print("Nothing in the right array")


class QueueUsingTwoStacks:
    """
    Exercise 17: Implement a queue using two stacks.
    Hint: One stack for enqueue, one for dequeue operations.
    """
    def __init__(self):
        self.stack_e = []
        self.stack_d = []

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

#    exercise_1_create_and_enqueue()    

#    q = deque([10, 20, 30])
#    print(exercise_2_dequeue_operation(q))
#    print(q)

    q = deque([10, 20, 30])
    q_1 = deque([10, 20, 30]) 
    q_2 = deque([10, 20])
    q_n = deque([10, 20, 30, 40, 50, 60, 70])
    e = deque()
#    print(exercise_3_check_empty(q))
#    print(exercise_3_check_empty(e))
    

#    print(exercise_4_front(q))
#    print(exercise_4_front(e))

#    print(exercise_5_size(q))
#    print(exercise_5_size(e))

#    print(exercise_6_reverse_queue(q))
#    print(exercise_7_copy_queue(q))
#    print(exercise_8_queues_equal(q, q_2))
#    exercise_9_print_and_empty(q)

#    print(exercise_10_max_in_queue(q))
#    print(exercise_10_max_in_queue(q_2))

#    print(exercise_11_rotate_left(q_n, 2))
#    print(exercise_12_is_palindrome_sequence([1, 2, 3, 2, 1]))
#    print(exercise_12_is_palindrome_sequence([1, 2, 3, 2, 1, 1]))
#    print(exercise_13_merge_alternating(deque([1, 3, 5, 7]), deque([2, 4, 6, 8])))
#    print(exercise_14_is_subsequence_queue(deque([2, 5]), deque([1, 2, 3, 5])))

    exercise_15_supermarket_simulation([(0, 5), (2, 3), (4, 2)])

#    two_q = TwoQueuesOneList(10)
#    two_q.enqueue1(1)
#    two_q.enqueue2(2)
#    two_q.enqueue2(1)
#    two_q.enqueue1(10)
#    print(two_q.q)


    pass
