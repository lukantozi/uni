def use_math():
    # not a good convention but for this task it's ok
    import math

    print(math.sqrt(16))
    print(math.floor(4.1))
    print(math.ceil(4.3))
    print(round((math.pi), 2))
#use_math()

def use_sqrt():
    from math import sqrt
    for i in range(1, 50, 3):
        print(f"square root of {i}: {round(sqrt(i), 2)}")
#use_sqrt()

def use_random():
    import random
    for _ in range(1000):
        print(round(random.random()*99 + 1, 2), end=", ")
#use_random()

def math_shorter():
    import math as m
    print(round(m.pi, 2))

#math_shorter()

def math_mult():
    from math import pi, floor, ceil, sqrt, fabs
