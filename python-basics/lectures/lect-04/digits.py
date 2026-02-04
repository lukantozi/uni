def mult_digits(n):
    if n <= 10:
        return n
    else:
        return n%10 * mult_digits(n//10)
