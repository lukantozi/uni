# from math import *
'''
 above import is not recommended because it will import 
 all the methods and already make it accessible. there
 could be some issues with using functions as we may
 have used them as variables. 
'''
from math import pi, sqrt
'''
or -> 
import math

-> and then access it math.pi, math.sqrt

importing way above is intuitive and
clear, avoiding mistakes
'''

print(pi)
print(sqrt(16))

