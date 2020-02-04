import numpy as np


def approximation(variable, apr, operations):
    value = 0
    for i in range(operations):
        if np.absolute(np.log(1+variable) - value) > apr:
            value = value + ((-1)**i * variable**(i+1))/(i+1)
    return value


number = float(input("Enter the number to compute natural logarithm of it incremented by 1:"))
approx = float(input("Enter the rank of approximation: "))
length = int(input("Enter the number of operations: "))
print(approximation(number, approx, length))
