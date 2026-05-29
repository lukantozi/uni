import numpy as np


"""
============================================================
Layer A
============================================================
"""
def layer_a():
    def task_1():
        arr = np.arange(0, 10)
        print(arr[1::2])

    def task_2():
        arr = np.zeros((3, 3), dtype="i")
        for i in range(3):
            arr[i,i] = 1
        print(arr)
    
    def task_3():
        a = [1, 2, 3]
        b = [4, 5, 6]
        ab_vert = np.vstack((a, b))
        ab_hor = np.hstack((a, b))
        print(ab_vert)
        print(ab_hor)

    def task_4():
        arr = np.random.randint(1, 100, 10)
        print(arr)
        print(arr[arr > 50])

    def task_5():
        arr = np.array([5, 3, 8, 1, 9, 2, 7])
        sorted_arr = np.sort(arr)
        print(f"Sorted: {sorted_arr}")
        print(f"Max: {arr.max()}") # could also just sorted_arr[-1]
        print(f"Min: {arr.min()}") # same here sorted_arr[0]
        print(f"Mean: {arr.mean()}")


"""
============================================================
Layer B
============================================================
"""
def layer_b():
    def task_1():
        arr = np.eye(3, dtype=int) * 5
        print(arr)

    def task_2():
        arr = np.arange(16).reshape(4, 4)
        arr_22 = arr[2:, 2:]
        arr_22[0, 1] = 111
        print(arr_22)

    def task_3():
        arr_1 = np.array([1, 3, 5, 6, 1, 2]).reshape(2,3)
        arr_2 = np.array([2, 4, 5, 2, 3, 4]).reshape(3,2)
        mult = np.dot(arr_1, arr_2)
        print(mult, '\n', mult.shape)

    def task_4():
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(np.where(arr % 2 == 0, -1, arr))
