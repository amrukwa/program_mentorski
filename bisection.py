import math
import numpy as np

def check_interval(a, b):
    if a * b <= 0:
        return 1
    else:
        return 0


def check_border(a, b, formula):
    if formula(a) == 0:
        if formula(b) == 0:
            return a, b
        return a
    if formula(b) == 0:
        return b
    return (a+b)/2


def root(a, b, formula, err):
    y1 = formula(a)
    y2 = formula(b)
    if check_interval(y1, y2):
        c = check_border(a, b, formula)
        if type(c) == tuple:
            return c
        y = formula(c)
        while y != 0 and b-a > err:
            if y1 * y < 0:
                b = c
            else:
                a = c
                y1 = formula(a)
            c = (a + b) / 2
            y = formula(c)
        return c


# enter your variables:


x1 =
x2 =
error =

# initialize your function:


def foo(x):
    y =
    return y


print(root(x1, x2, foo, error))

