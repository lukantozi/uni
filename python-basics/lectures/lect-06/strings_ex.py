# task 1
def first_last_two(txt):
    if len(txt) < 2:
        return ""
    return txt[:2] + txt[-2:]
#print(first_last_two("house"))
#print(first_last_two("it"))
#print(first_last_two("x"))


# task 2
def return_cap_c(txt):
    if txt.startswith("C:"):
        return txt.upper()
    else:
        return "not on disk C"
#print(return_cap_c("C:/ssd/files"))


# task 3
def count_a(txt):
    to_add = txt.count("a")
    txt = txt + str(to_add)
    return txt
#print(count_a("banana"))


# task 4
def reverse_if_mult_3(txt):
    if len(txt)%3 == 0:
        return txt[::-1] 
    else:
        return "length not a multiple of 3"
#print(reverse_if_mult_3("abcb"))
