# list comprehension
# task 1
def ret_cubes():
    return [x**3 for x in range(3, 13)]
#print(ret_cubes())


# task 2
def ret_pos():
    return [x for x in [2, -1, 3, -2, -3] if x >= 0]
#print(ret_pos())


# task 3
def ret_no_empt(lst):
    return [x for x in lst if x != ""]
#print(ret_no_empt(["car", "", "boat", "", "cat"]))


# task 4
def div_sing():
    return [x for x in range(1, 101) if [y for y in range(2, 10) if x%y==0]]
#print(div_sing())


# task 5
def div_five_three():
    return [x for x in range(100, 1001) if (x%3==0 or x%5 == 0) and x%15 != 0]
#print(div_five_three())


# task 6
def first_last(lst):
    return len([word for word in lst if len(word) >= 2 and word[0] == word[-1]])
#print(first_last(["abba", "banana", "aa", "w", "", "apple", "assa", "atta"]))
