def next_greater(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (right + left) // 2
