# Daily drill: implement BASIC + 1 variant per topic (no sorted()).

#bubble_sort
#- BASIC: Implement bubble sort ascending (early-exit swapped flag).
#- +1: Stop after k passes.
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 2, 1, 2, 1]]}

#insertion_sort
#- BASIC: Implement insertion sort ascending (key + shifting).
#- +1: Count shifts.
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 2, 4, 6], [4, 1, 3, 2], [1, 2, 3, 4]], "subarray_case": {"arr": [9, 8, 1, 7, 3, 2, 6], "l": 2, "r": 5}, "insert_case": {"arr": [1, 2, 4, 5], "x": 3}}

#merge_sort
#- BASIC: Implement top-down merge sort + merge helper.
#- +1: Merge two sorted lists helper (standalone).
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 1, 4, 2, 8], [-3, 10, 0, -1, 7]], "merge_two_lists": {"a": [1, 5, 12, 19, 25], "b": [3, 6, 14, 18, 23, 28]}, "strings": ["Bob", "alice", "Carol"], "tuples": [[3, "c"], [1, "a"], [2, "b"]]}

#quick_sort_3way
#- BASIC: Implement 3-way partition quicksort (less/equal/greater).
#- +1: Absolute value key.
TESTS = {"lists": [[64, 34, 25, 12, 22, 11, 90], [5, 5, 5, 5], [9, 7, 5, 3, 1], [1]], "strings": ["Bob", "alice", "Carol"], "abs_list": [-10, -3, 1, 2, -2, 5]}

#stack
#- BASIC: Valid brackets: (), {}, [].
#- +1: Remove adjacent duplicates.
TESTS = {"reverse": ["ainom", "hello"], "paren": ["(())", "(()", "(())()"], "brackets": ["()", "([])", "([{}])", "{[(])}", "((())"], "decimal": [13, 156, 0], "palindrome": ["madam", "racecar", "12321", "hello"], "adj_dupes": ["abbaca", "abba", "azxxzy"], "rpn": ["23+", "23*54-+", "52-", "5"], "stack_sort": [[4, 3, 2, 1]]}

#binary_search
#- BASIC: Binary search (iterative) -> index or -1.
#- +1: Last occurrence in duplicates.
TESTS = {"basic_case": {"arr": [11, 12, 22, 25, 34, 64, 90], "target": 25}, "not_found_case": {"arr": [10, 20, 30, 40, 60], "target": 50}, "dupes_case": {"arr": [1, 2, 2, 2, 3], "target": 2}, "bounds_case": {"arr": [3, 3, 4, 12, 12, 12, 14], "target": 12}, "insert_middle": {"arr": [1, 5, 10], "target": 7}}

#queue
#- BASIC: Implement queue using deque: enqueue, dequeue, front, is_empty, size.
#- +1: Rotate left by k steps.
TESTS = {"basic_ops": {"enqueue": [1, 2, 3, 4, 5], "dequeue_from": [10, 20, 30]}, "reverse": [1, 2, 3, 4], "compare": {"q1": [1, 2, 3], "q2": [1, 2, 3], "q3": [1, 3, 2]}, "max": [2, 9, 4, 7], "rotate": {"arr": [1, 2, 3, 4, 5], "k": 2}, "palindrome": {"valid": [1, 2, 3, 2, 1], "invalid": [1, 2, 3]}, "merge": {"q1": [1, 3, 5], "q2": [2, 4, 6, 8]}, "subsequence": {"small": [2, 5], "big": [1, 2, 3, 4, 5], "not_sub": [2, 6]}}

#hashmaps
#- BASIC: Implement frequency counter using dict.
#- +1: Longest substring without repeating characters.
TESTS = {"frequency": [[1, 2, 2, 3, 3, 3], "hello", "mississippi"], "two_sum": [{"nums": [2, 7, 11, 15], "target": 9}, {"nums": [3, 2, 4], "target": 6}], "anagrams": [["eat", "tea", "tan", "ate", "nat", "bat"]], "longest_substring": ["abcabcbb", "bbbbb", "pwwkew"], "subarray_sum": [{"nums": [1, 1, 1], "k": 2}, {"nums": [1, 2, 3], "k": 3}], "first_non_repeat": ["leetcode", "loveleetcode", "aabb"], "anagram_check": [{"a": "listen", "b": "silent"}, {"a": "hello", "b": "world"}], "top_k": {"nums": [1, 1, 1, 2, 2, 3], "k": 2}, "intersect": [{"a": [1, 2, 2, 1], "b": [2, 2]}, {"a": [4, 9, 5], "b": [9, 4, 9, 8, 4]}], "duplicates": [[4, 3, 2, 7, 8, 2, 3, 1], [1, 1, 2]], "missing": [[3, 0, 1], [0, 1], [9, 6, 4, 2, 3, 5, 7, 0, 1]]}
