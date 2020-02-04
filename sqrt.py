def foo(square, near):
    y0 = square / 2
    y1 = 0.0
    while near < y0 - y1 or y0 - y1 < - near:
        if y1 == 0:
            y1 = (y0 + square / y0) / 2
        else:
            y0 = y1
            y1 = 0.5 * (y0 + square / y0)

    return y1


number = float(input("Enter the number you want to have square root of:"))
approx = float(input("Enter the rank of approximation: "))
print(foo(number, approx))
