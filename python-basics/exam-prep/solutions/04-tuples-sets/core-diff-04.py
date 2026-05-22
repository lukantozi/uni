def slice_tuple():
    tupl5 = (1, 2, 3, 4, 5)
    print(tupl5[0:3])
#slice_tuple()

def set_from_list():
    nums = [2, 5, 2, 3, 3, 4, 1]
    set_nums = set(nums)
    print(set_nums)
#set_from_list()

def tuple_immut():
    tpl = (1, 2, 3, 5)
    try:
        tpl[3] = 4
    except TypeError as e:
        print(f"tpl[3] = 4: {e}")
#tuple_immut()

def intersection():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(set1 & set2)
#intersection()

def tup_to_list():
    t = (1, 2, 3)
    l = [x for x in t]
    # lsp did not like l = list(t)
    l.append(4)
    l = tuple(l)
    print(l)
#tup_to_list()
