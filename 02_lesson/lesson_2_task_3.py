import math


def square(side):
    return math.ceil(side * side)


side = 2.5  # пример не целого числа
area = square(side)
print(f"Площадь квадрата со стороной {side} равна {area}")
