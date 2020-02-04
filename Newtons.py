import sympy as sym
import numpy as np
import math


x = sym.Symbol('x')

# define the function:


def foo(x):
    y =
    return y


DerivativeOfFoo = sym.lambdify(x, sym.diff(foo(x)), "numpy")


def root(formula, der, cur, mistake):
    after = cur - formula(cur)/der(cur)
    while formula(after) != 0 and np.absolute(cur-after) > mistake:
        cur = after
        after = cur - formula(cur) / der(cur)
    return after

# add the starting point


stpoint =

# add the tolerance:
tolerance =

print(root(foo, DerivativeOfFoo, stpoint, tolerance))


