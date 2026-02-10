from collections import Counter, defaultdict
"""
Hash Maps & Sets - 30 Practice Exercises
Complete each function following the description.
"""

# ============================================================================
# PART 1: BASIC DICT OPERATIONS (1-5)
# ============================================================================

def ex1_dict_crud():
    """
    Create dict d = {'a': 1, 'b': 2}
    Update 'b' to 20, add 'c': 3, delete 'a'
    Return: {'b': 20, 'c': 3}
    """
    d = {'a': 1, 'b': 2}
    d['b'] = 20
    d['c'] = 3
    del d['a']
    return d


def ex2_count_frequencies(arr):
    """
    Count how many times each element appears.
    Example: [1,2,2,3,3,3] -> {1:1, 2:2, 3:3}
    """
    elements = defaultdict(int)
    for num in arr:
        elements[num] += 1

    return elements


def ex3_anagram(a, b):
    """
    Return True if two strings are anagrams.
    Example: "listen" and "silent" -> True
    """
    if len(a) != len(b):
        return False

    freq_a = defaultdict(int)
    freq_b = defaultdict(int)
    for let_a, let_b in zip(a, b):
        freq_a[let_a] += 1
        freq_b[let_b] += 1

    return freq_a == freq_b

#print(ex3_anagram("listen", "silent"))


def ex4_two_sum(nums, target):
    """
    Find two indices where nums[i] + nums[j] == target.
    Example: [2,7,11,15], 9 -> [0,1]
    Return None if no solution.
    """
    n = len(nums)
    diff = {}
    diff[nums[0]] = target - nums[0]
    for i in range(1, n):
        if nums[i] in diff.values():
            return [nums.index(target-nums[i]), i]
        else:
            diff[nums[i]] = target
    return None
         
#print(ex4_two_sum([2,7,11,5], 9))


def ex5_dedup_keep_order(arr):
    """
    Remove duplicates while preserving first occurrence order.
    Example: [1,2,1,3,2,4] -> [1,2,3,4]
    """
    dedup = defaultdict()
    for token in arr:
        dedup[token] = True
    return list(dedup) 

#print(ex5_dedup_keep_order([1,2,1,3,2,4]))

# ============================================================================
# PART 2: INTERMEDIATE PATTERNS (6-13)
# ============================================================================

def ex6_first_unique_index(s):
    """
    Return index of first non-repeating character.
    Example: "leetcode" -> 0 (character 'l')
    Return -1 if none.
    """
    n = len(s)
    rep = defaultdict(int)
    for i in range(n-1):
        rep[s[i]] += 1
        if rep[s[i]] == 1 and s[i] != s[i+1]:
            return i
        if s[i] != s[i+1]:
            rep[s[i]] = 0
    return -1 if s[-1] == s[-2] else n-1

#print(ex6_first_unique_index("lleerrttrrccoodde"))


def ex7_group_by_length(words):
    """
    Group words by their length.
    Example: ["a","to","tea"] -> {1:["a"], 2:["to"], 3:["tea"]}
    """
    len_word = defaultdict(list)
    for word in words:
        len_word[len(word)].append(word) # -> not sure why put words in lists, i could just put words there but okay
    return len_word

#print(ex7_group_by_length(["a", "to", "tea"]))

def ex8_group_anagrams(words):
    """
    Group anagrams together.
    Example: ["eat","tea","ate","bat"] -> [["eat","tea","ate"], ["bat"]]
    """
    anagrams = defaultdict(list)
    for word in words:
        freq = tuple(sorted(word))
        anagrams[freq].append(word)

    return list(anagrams.values())
            
#print(ex8_group_anagrams(["eat", "tea", "ate", "bat"]))



def ex9_invert(d):
    """
    Invert dictionary (swap keys/values). Handle duplicate values.
    Example: {"a":1, "b":2, "c":1} -> {1:['a','c'], 2:['b']}
    """
    new_d = defaultdict(list)
    for key in d:
        new_d[d[key]].append(key)
    return dict(new_d)

#print(ex9_invert({"a":1, "b":2, "c":1}))

def ex10_merge_sum(a, b):
    """
    Merge two dicts, summing values for common keys.
    Example: {"x":2,"y":3}, {"y":4,"z":5} -> {'x':2,'y':7,'z':5}
    """
    for key in b:
        if key in a:
            a[key] += b[key]
        else:
            a[key] = b[key]
    return a

#print(ex10_merge_sum({"x":2,"y":3}, {"y":4,"z":5}))

def ex11_most_frequent(arr):
    """
    Return the most frequent element.
    Example: [1,2,2,3,3,3,2] -> could be 2 or 3 depending on implementation
    """
    return Counter(arr).most_common(1)[0][0]

#print(ex11_most_frequent([1,2,2,3,3,2,2,3,4,4,4,4,4]))

def ex12_has_pair_sum(nums, k):
    """
    Check if any two numbers sum to k.
    Example: [10,15,3,7], 17 -> True (10+7)
    """
    num_sums = {}
    for n in nums:
        if n in num_sums.values():
            return True
        num_sums[n] = k - n
    return False

#print(ex12_has_pair_sum([10,15,3,7], 25))


def ex13_subarray_sum(nums, k):
    """
    Count subarrays with sum equal to k (prefix sum technique).
    Example: [1,1,1], k=2 -> 2 (subarrays: [1,1] twice)
    """
    pass


# ============================================================================
# PART 3: ADVANCED PATTERNS (14-22)
# ============================================================================

def ex14_length_of_longest_substring(s):
    """
    Length of longest substring without repeating characters.
    Example: "abcabcbb" -> 3 ("abc")
    """
    pass


def ex15_can_construct(note, magazine):
    """
    Can you construct 'note' using letters from 'magazine'?
    Example: "aab", "baa" -> True
    """
    pass


def ex16_top_k(nums, k):
    """
    Return k most frequent elements.
    Example: [1,1,1,2,2,3], k=2 -> [1,2]
    """
    pass


def ex17_intersect(a, b):
    """
    Intersection with counts (duplicates allowed).
    Example: [1,2,2,1], [2,2] -> [2,2]
    """
    pass


def ex18_dedup_by_id(items):
    """
    Remove duplicate dicts based on 'id' key (keep first).
    Example: [{"id":1}, {"id":2}, {"id":1}] -> [{"id":1}, {"id":2}]
    """
    pass


def ex19_adjacency_list(edges):
    """
    Build graph adjacency list from edge list.
    Example: [(1,2),(1,3),(2,3)] -> {1:[2,3], 2:[3]}
    """
    pass


def ex20_first_recurring(s):
    """
    First character that appears twice.
    Example: "ABCDEAF" -> 'A'
    """
    pass


def ex21_word_freq(text):
    """
    Word frequency counter (case-insensitive).
    Example: "Hello, hello! HELLO?" -> {'hello': 3, ...}
    """
    pass


def ex22_first_index_map(arr):
    """
    Map each unique value to its first index.
    Example: [5,3,5,2,3,9] -> {5:0, 3:1, 2:3, 9:5}
    """
    pass


# ============================================================================
# PART 4: CLASSES & SPECIAL PATTERNS (23-30)
# ============================================================================

class PhoneBook:
    """
    Simple phonebook supporting add/find/delete operations.
    """
    def __init__(self):
        pass
    
    def add(self, name, number):
        pass
    
    def find(self, name):
        pass
    
    def delete(self, name):
        pass


def ex24_group_by_first_letter(words):
    """
    Group words by first letter using setdefault.
    Example: ["ant","apple","banana"] -> {'a':["ant","apple"], 'b':["banana"]}
    """
    pass


def ex25_fib(n, memo=None):
    """
    Fibonacci with memoization (dict cache).
    Initialize memo with {0:0, 1:1} if None.
    """
    pass


def ex26_contains_duplicate(nums):
    """
    Return True if array contains any duplicates.
    Example: [1,2,3,1] -> True
    """
    pass


def ex27_missing_number(nums):
    """
    Find missing number in range [0..n].
    Example: [3,0,1] -> 2
    Hint: Use set or math (sum formula)
    """
    pass


def ex28_roman_to_int(s):
    """
    Convert Roman numeral to integer.
    Example: "MCMXCIV" -> 1994
    Mapping: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
    """
    pass


def ex29_longest_consecutive(nums):
    """
    Length of longest consecutive sequence.
    Example: [100,4,200,1,3,2] -> 4 (sequence: 1,2,3,4)
    """
    pass


class MiniMap:
    """
    Simple hash map with buckets (chaining for collisions).
    """
    def __init__(self, capacity=8):
        pass
    
    def _idx(self, key):
        """Return bucket index for key."""
        pass
    
    def set(self, key, value):
        """Insert or update key-value pair."""
        pass
    
    def get(self, key, default=None):
        """Retrieve value for key."""
        pass
    
    def delete(self, key):
        """Remove key. Return True if found, False otherwise."""
        pass
