from hash_maps import *

def test(num, func, expected=None, desc=""):
    """Helper to run a single test."""
    try:
        result = func()
        if expected is not None:
            assert result == expected, f"Expected {expected}, got {result}"
        print(f"✓ Test {num}: {desc}")
        return True
    except (AssertionError, Exception) as e:
        print(f"✗ Test {num} failed: {desc}")
        print(f"  Error: {e}")
        return False


def main():
    print("Running 30 hashmap exercise tests...\n")
    passed = 0
    total = 30
    
    # Test 1
    if test(1, lambda: ex1_dict_crud(), {'b': 20, 'c': 3}, "Dict CRUD"):
        passed += 1
    
    # Test 2
    if test(2, lambda: ex2_count_frequencies([1,2,2,3,3,3]), {1:1, 2:2, 3:3}, "Count frequencies"):
        passed += 1
    
    # Test 3
    if test(3, lambda: ex3_anagram("listen", "silent"), True, "Anagram check"):
        passed += 1
    
    # Test 4
    if test(4, lambda: ex4_two_sum([2,7,11,15], 9), [0,1], "Two Sum"):
        passed += 1
    
    # Test 5
    if test(5, lambda: ex5_dedup_keep_order([1,2,1,3,2,4]), [1,2,3,4], "Dedup keep order"):
        passed += 1
    
    # Test 6
    if test(6, lambda: ex6_first_unique_index("leetcode"), 0, "First unique index"):
        passed += 1
    
    # Test 7
    if test(7, lambda: ex7_group_by_length(["a","to","tea"]), {1:["a"], 2:["to"], 3:["tea"]}, "Group by length"):
        passed += 1
    
    # Test 8
    try:
        result = ex8_group_anagrams(["eat","tea","ate"])
        assert len(result) == 1 and len(result[0]) == 3
        print("✓ Test 8: Group anagrams")
        passed += 1
    except Exception as e:
        print(f"✗ Test 8 failed: Group anagrams - {e}")
    
    # Test 9
    try:
        result = ex9_invert({"a":1,"b":2,"c":1})
        assert result == {1:['a','c'], 2:['b']} or result == {1:['c','a'], 2:['b']}
        print("✓ Test 9: Invert dict")
        passed += 1
    except Exception as e:
        print(f"✗ Test 9 failed: Invert dict - {e}")
    
    # Test 10
    if test(10, lambda: ex10_merge_sum({"x":2,"y":3}, {"y":4,"z":5}), {'x':2,'y':7,'z':5}, "Merge sum"):
        passed += 1
    
    # Test 11
    try:
        result = ex11_most_frequent([1,2,2,3,3,3,2])
        assert result in (2, 3)
        print("✓ Test 11: Most frequent")
        passed += 1
    except Exception as e:
        print(f"✗ Test 11 failed: Most frequent - {e}")
    
    # Test 12
    if test(12, lambda: ex12_has_pair_sum([10,15,3,7], 17), True, "Has pair sum"):
        passed += 1
    
    # Test 13
    if test(13, lambda: ex13_subarray_sum([1,1,1], 2), 2, "Subarray sum"):
        passed += 1
    
    # Test 14
    if test(14, lambda: ex14_length_of_longest_substring("abcabcbb"), 3, "Longest substring"):
        passed += 1
    
    # Test 15
    if test(15, lambda: ex15_can_construct("aab", "baa"), True, "Ransom note"):
        passed += 1
    
    # Test 16
    try:
        result = ex16_top_k([1,1,1,2,2,3], 2)
        assert sorted(result) == [1,2]
        print("✓ Test 16: Top K")
        passed += 1
    except Exception as e:
        print(f"✗ Test 16 failed: Top K - {e}")
    
    # Test 17
    try:
        result = ex17_intersect([1,2,2,1], [2,2])
        assert sorted(result) == [2,2]
        print("✓ Test 17: Intersection")
        passed += 1
    except Exception as e:
        print(f"✗ Test 17 failed: Intersection - {e}")
    
    # Test 18
    try:
        result = ex18_dedup_by_id([{"id":1},{"id":2},{"id":1}])
        assert len(result) == 2 and result[0]["id"] == 1 and result[1]["id"] == 2
        print("✓ Test 18: Dedup by id")
        passed += 1
    except Exception as e:
        print(f"✗ Test 18 failed: Dedup by id - {e}")
    
    # Test 19
    if test(19, lambda: ex19_adjacency_list([(1,2),(1,3),(2,3)]), {1:[2,3], 2:[3]}, "Adjacency list"):
        passed += 1
    
    # Test 20
    if test(20, lambda: ex20_first_recurring("ABCDEAF"), 'A', "First recurring"):
        passed += 1
    
    # Test 21
    try:
        result = ex21_word_freq("Hello, hello! HELLO? world.")
        assert result['hello'] == 3
        print("✓ Test 21: Word freq")
        passed += 1
    except Exception as e:
        print(f"✗ Test 21 failed: Word freq - {e}")
    
    # Test 22
    if test(22, lambda: ex22_first_index_map([5,3,5,2,3,9]), {5:0, 3:1, 2:3, 9:5}, "First index map"):
        passed += 1
    
    # Test 23
    try:
        pb = PhoneBook()
        pb.add("Alice", "123")
        assert pb.find("Alice") == "123"
        pb.delete("Alice")
        assert pb.find("Alice") == None
        print("✓ Test 23: Phonebook")
        passed += 1
    except Exception as e:
        print(f"✗ Test 23 failed: Phonebook - {e}")
    
    # Test 24
    try:
        result = ex24_group_by_first_letter(["ant","apple","banana"])
        assert result.get('a') == ["ant","apple"]
        print("✓ Test 24: Group by first letter")
        passed += 1
    except Exception as e:
        print(f"✗ Test 24 failed: Group by first letter - {e}")
    
    # Test 25
    if test(25, lambda: ex25_fib(10), 55, "Fibonacci"):
        passed += 1
    
    # Test 26
    if test(26, lambda: ex26_contains_duplicate([1,2,3,1]), True, "Contains duplicate"):
        passed += 1
    
    # Test 27
    if test(27, lambda: ex27_missing_number([3,0,1]), 2, "Missing number"):
        passed += 1
    
    # Test 28
    if test(28, lambda: ex28_roman_to_int("MCMXCIV"), 1994, "Roman to int"):
        passed += 1
    
    # Test 29
    if test(29, lambda: ex29_longest_consecutive([100,4,200,1,3,2]), 4, "Longest consecutive"):
        passed += 1
    
    # Test 30
    try:
        mm = MiniMap()
        mm.set("a", 1)
        mm.set("b", 2)
        mm.set("a", 10)
        assert mm.get("a") == 10
        print("✓ Test 30: MiniMap")
        passed += 1
    except Exception as e:
        print(f"✗ Test 30 failed: MiniMap - {e}")
    
    print(f"\n{'='*60}")
    print(f"Results: {passed}/{total} tests passed")
    if passed == total:
        print("All tests passed!")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
