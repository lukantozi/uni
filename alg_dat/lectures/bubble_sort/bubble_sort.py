from typing import List, TypeVar

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def print_examples():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted array:", bubble_sort(numbers))

    nums = [5, 1, 4, 2, 8]
    print("Sorted numbers:", bubble_sort(nums))

    words = ["banana", "apple", "cherry"]
    print("Sorted words:", bubble_sort(words))

    pairs = [(3, "c"), (1, "a"), (2, "b")]
    print("Sorted pairs:", bubble_sort(pairs))

T = TypeVar('T')


def bubble_sort_basic(a: List[T]) -> List[T]:
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a
#print(bubble_sort_basic([2, 4, 1, 19, 3]))


def cocktail_shaker_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped == True:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if swapped == False:
            break
        end -= 1

        for i in range(end-1, start-1, -1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        start += 1
    return a
#print(cocktail_shaker_sort([5, 1, 4, 2, 8]))


people = [("John", "Smith"), ("Alice", "Brown"), ("Bob", "Smith"), ("Charlie", "Adams")]
def bubble_sort_two_keys(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            elif arr[j][1] == arr[j+1][1]: 
                if arr[j][0] > arr[j+1][0]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
        if not swapped:
            break
    return arr
#print(bubble_sort_two_keys(people))


def bubble_sort_count_comparison(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                count += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return count
#print(bubble_sort_count_comparison([3, 2, 1]))


def bubble_sort_k_passes(arr, k):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        k -= 1
        if k == 0:
            return arr
        if not swapped:
            break
    return arr
#print(bubble_sort_k_passes([5, 4, 3, 2, 1], 3))


def bubble_sort_with_log(arr):
    n = len(arr)
    log = []
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                log.append((arr[j], arr[j+1]))
                swapped = True
        if not swapped:
            break
    return arr, log


def bubble_sort_with_log_init():
    sorted_a, swap_log = bubble_sort_with_log([4,3,2,1])

    print(sorted_a)
    for log in swap_log:
        print(log)
    print("#swaps: ", len(swap_log))
#bubble_sort_with_log_init()

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#print(bubble_sort_desc([3,1,4,1,5]))


def bubble_pass_count(arr): 
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        count += 1
        if not swapped:
            break
    return count

#print(bubble_pass_count([1,2,3,4]))
#print(bubble_pass_count([3,2,1]))


def bubble_front_m_smallest(arr, m):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                m -= 1
        if m == 0:
            return arr
        if not swapped:
            break
    return arr
#print(bubble_front_m_smallest([7,3,5,2,9,1], 3))


def bubble_sort_key_tuple(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if abs(arr[j]) > abs(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            elif arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#print(bubble_sort_key_tuple([-10,-3,1,2,-2,5]))


#from functools import cmp_to_key

def cmp_len_desc_then_lex(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        return 1
    elif len_a == len_b:
        if a > b:
            return -1
    else:
        return 0


def bubble_sort_cmp(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if cmp_len_desc_then_lex(arr[j], arr[j+1]) == 1:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            elif cmp_len_desc_then_lex(arr[j], arr[j+1]) == -1:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#print(bubble_sort_cmp(["pear", "apple", "banana", "fig"]))


import math

def bubble_sort_eps(arr, eps=1e-9):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1] and abs(arr[j] - arr[j+1]) >= eps:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
                swapped = True
        if not swapped:
            break
    return arr, count
#print(bubble_sort_eps([1.0, 1.0+1e-10, 0.999999999])[0])
#print(bubble_sort_eps([1.0, 1.0+1e-10, 0.999999999])[1])


def cmp_len_then_lex(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        return 1
    elif len_a == len_b:
        if a > b:
            return -1
    else:
        return 0


def bubble_sort_len_then_lex(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if cmp_len_then_lex(arr[j], arr[j+1]) == 1:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            elif cmp_len_then_lex(arr[j], arr[j+1]) == -1:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#print(bubble_sort_len_then_lex(["kiwi","apple","pear","ban"]))


def count_inversions(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
    return count
#print(count_inversions([3,2,1,0]))
#print(count_inversions([1,1,1,1]))


def is_stable_after_bubble(arr):
    n = len(arr)
    indices = []
    for i in range(n):
        indices.append(i)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                indices[j], indices[j+1] = indices[j+1], indices[j]
                swapped = True
        if not swapped:
            break
    return arr, indices 
#print(is_stable_after_bubble([2,1,2,1,2,1])[0])
#print(is_stable_after_bubble([2,1,2,1,2,1])[1])


def bubble_sort_linked_list(head):
    while head != None:
        swapped = False
        head_cmp = head.next
        while head_cmp != None:
            if head.value > head_cmp.value:
                tmp = head.value
                head.value = head_cmp.value
                head_cmp.value = tmp
                swapped = True
            head_cmp = head_cmp.next
        head = head.next
        if not swapped:
            break


def to_list(head):
    nodes = []
    while head != None:
        nodes.append(head.value)
        head = head.next
    return nodes


def bubble_sort_linked_list_init():
    class Node:
        def __init__(self, x):
            self.value = x
            self.next = None

    h = Node(5)
    h.next = Node(1)
    h.next.next = Node(2)
    h.next.next.next = Node(4)

    bubble_sort_linked_list(h)
    print(to_list(h))
#bubble_sort_linked_list_init()


def bubble_sort_rows_by_sum(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            sum_1 = arr[j][0] + arr[j][1]
            sum_2 = arr[j+1][0] + arr[j+1][1]
            print(f"{sum_1} compare to {sum_2}")
            print(sum_1 > sum_2)
            if sum_1 > sum_2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#print(bubble_sort_rows_by_sum([[3,1],[2,2],[0,5]]))
#print(bubble_sort_rows_by_sum([[3,1],[2,2],[0,5],[1,0]]))


def bubble_sort_evens_only(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            el_1 = arr[j]
            if el_1 % 2 != 0:
                el_2 = arr[j+1]
                if el_1 % 2 != 0 and el_2 % 2 != 0 and el_1 > el_2:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort_evens_only([5,8,3,2,9,6]))
