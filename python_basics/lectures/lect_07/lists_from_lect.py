# task 1
def sum_of_elements_1():
    lst = [12, 32, 4354, 231, 123, 1]
    return sum(lst)
#print(sum_of_elements_1())


def sum_of_elements_2():
    sum = 0
    lst = [12, 32, 4354, 231, 123, 1]
    for num in lst:
        sum += num
    return sum
#print(sum_of_elements_2())


# task 2
def sum_max_min():
    lst = [12, 32, 4354, 231, 123, 1, -1, 12, 2323, 32, 2, -1, 2]
    return max(lst) + min(lst)
#print(sum_max_min())


# task 3
def first_to_last():
    lst = ["a", "b", "c"]
    first = lst.pop(0)
    lst.append(first)
    return lst
#print(first_to_last())


# task 4
def slice_list():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(f"a: {lista[7:10]}")
    print(f"b: {lista[:-2:3]}")
    print(f"c: {lista[-1:-8:-2]}")
    print(f"d: {lista[-1]}")
#slice_list()


# task 5
def remove_empty():
    lst = ["", "car", "boat", "", "", "cat"]
    for element in lst[:]:
        if element == "":
            lst.remove(element)
    return lst
#print(remove_empty())


# task 6
def strange_list():
    lst = [1, 2, [30, 40, [500, 600, 700], 80], 8]
    lst[2][2].append(800)
    return lst
#print(strange_list())


# task 7
def pal_len():
    lst = ["abc", "xyz", "aba", "1221", "13331"]
    count = 0
    for el in lst:
        if len(el) > 2 and el[0] == el[-1]:
            count += 1
    print(f"First and Last Character are same: {count}")
#pal_len()


# task 8
def count_sub_num(lst):
    count = 0
    counter_inner = 0
    for sub_list in lst:
        for el in sub_list:
            if isinstance(el, int):
                counter_inner += 1
            else:
                counter_inner = 0
                break
        count += counter_inner
    return count
#print(count_sub_num([[1, 2], [2], [2, 3, 4]]))
#print(count_sub_num([[1, 2, 2, 3, 4]]))
#print(count_sub_num([[1, 2], [2], [2, 3, "a"]]))
#print(count_sub_num([[1, 2, 2, 3, 4], [1, 3, "a"], [3, 4, 5]]))
