import os
from timeit import Timer
import random

true = True
false = False

def clear():
    os.system("cls")

def execTime(cmd):
    t = Timer(cmd)
    print("Finished in [{0}]s".format(t.timeit(1)))

def random_x_digits(x,leading_zeroes=true):
    if not leading_zeroes:
        return random.randint(10**(x-1),10**x-1)
    else:
        return "{0:0{x}d}".format(random.randint(0,10**x-1),x=x)
