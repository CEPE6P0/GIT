# 2. Определите функцию вычисление_объема_цилиндра(), которая
# принимает радиус основания и высоту цилиндра в качестве аргументов и
# возвращает его объем. Затем вызовите функцию с несколькими значениями
# радиуса и высоты.

import math
def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

print(calculate_cylinder_volume(2, 5))
print(calculate_cylinder_volume(4, 10))
print(calculate_cylinder_volume(6, 15))
