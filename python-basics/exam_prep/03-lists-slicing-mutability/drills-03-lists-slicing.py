def slice_arr(arr):
    print(arr[7:10])
    print(arr[::3])
    print(arr[-1:-9:-2])
    print(arr[-1:])

#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#slice_arr(nums)

#nums = [12, 32, 4354, 231, 123, 1]
#print(sum(nums))

def max_min_diff(arr):
    return max(arr) - min(arr)

#nums = [12, 32, 4354, 231, 123, 1, -1, 12, 2323, 32, 2, -1, 2]
#print(max_min_diff(nums))

def first_to_last(arr):
    arr.append(arr.pop(0))
    return arr

#nums = [12, 32, 4354, 231, 123, 1, -1, 12, 2323, 32, 2, -1, 2]
#print(first_to_last(nums))

def remove_space(arr):
    res = [token for token in arr if token != ""]
    return res
print(remove_space(["", "car", "boat", "", "", "cat"]))
