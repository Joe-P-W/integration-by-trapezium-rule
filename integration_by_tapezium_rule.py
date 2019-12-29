import time


def equation(x):
    return x**2+1


def trapz_area(top, bottom, height):
    return ((top+bottom)/2)*height


def integrate(equation, start, end,
              accuracy: float = 0.0001) -> float:

    top = start
    bottom = top + accuracy
    height = accuracy
    area = 0.0

    while bottom <= end:
        area += trapz_area(equation(top), equation(bottom), height)
        top += accuracy
        bottom += accuracy

    return area


t1 = time.time()
print(integrate(equation, 0.0, 10000.0))
print(time.time() - t1)