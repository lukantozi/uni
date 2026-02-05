def compare_three():
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    print(f"a < b < c: {a < b < c}")
#compare_three()

def check_emptiness(arr):
    return not arr
#print(check_emptiness([2, 3]))
#print(check_emptiness([]))

def or_short_circuit():
    print("" or False or 1)
    print(False or True or 1)
    print(False and True or False)
#or_short_circuit()
