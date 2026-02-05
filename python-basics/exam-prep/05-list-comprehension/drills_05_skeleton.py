def cubes_of_range(low, high):
    return [x**3 for x in range(low, high)]

#cubes = cubes_of_range(3, 12)
#print(f"reversed:       {cubes}\ncubes reversed: {cubes[::-1]}")

def remove_negative(arr):
    return [x for x in arr if x > 0]

#print(remove_negative([2, -1, 3, -2, -3]))

def remove_empty(arr):
    return [x for x in arr if x != ""]

#print(remove_empty(["", "car", "boat", "", "", "cat"]))

def fizzbuzz():
    return [x for x in range(100, 1000) if (x % 5 == 0 or x % 3 == 0) and x % 15 != 0]

#print(fizzbuzz())

def len_fir_las(arr):
    return [x for x in arr if x[0] == x[-1] if len(x) > 2]

#print(len_fir_las(['abc', 'xyz', 'aba', '1221']))
