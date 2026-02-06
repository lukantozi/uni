from math import pi
from random import randint

def circle_area(r):
    area = round(pi * r**2, 2)
    return area

def even_num(st, en):
    flag = True
    num = -1
    while flag: 
        num = randint(st, en)
        if num % 2 == 0:
            flag = False
    return num
