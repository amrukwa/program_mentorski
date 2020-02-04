import random as rd


def piv(n):
    c = 0
    for i in range(n):
        x = rd.uniform(-1, 1)
        y = rd.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            c += 1
    return 4*c/n


tc = int(input("Enter the number of points for calculations: "))
print(piv(tc))


