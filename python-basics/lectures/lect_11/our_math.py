def sum_of_digits(number):
    if number < 1:
        return number
    else:
        return number%10 + sum_of_digits(number//10)
