# Task 1
def sum_recursion(n):
    if n // 10 == 0:
        return n
    else:
        return n%10 + sum_recursion(n//10)


# Task 2
def power_to_recursion(n, m):
    if m == 0:
        return 1
    return n*power_to_recursion(n, m-1)


# Task 3
def sum_fraction_recursion(n):
    if n == 1:
        return 1/2
    return 1/(2*n) + sum_fraction_recursion(n-1)


# Task 4
def gdc(n, m):
    if n%m == 0:
        return m
    elif n%m == 1:
        return 1
    return gdc(m, n%m)
