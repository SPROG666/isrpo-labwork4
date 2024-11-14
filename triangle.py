from check_for import check_for_number
from check_for import check_for_not_negative

"""Принимает длины основания и высоты треугольника, возвращает его площадь"""
def area(a, h):
    """Проверка на корректность типов аргументов"""
    if not check_for_number(a) or not check_for_number(h):
        raise TypeError("arguments must be numbers")

    """Проверка на корректность значений аргументов"""
    if not check_for_not_negative(a) or not check_for_not_negative(h):
        raise ValueError("agruments must be not negative")

    return a * h / 2 

"""Принимает длины всех сторон треугольника, возвращает его периметр"""
def perimeter(a, b, c):
    """Проверка на корректность типов аргументов"""
    if not check_for_number(a) or not check_for_number(b) or not check_for_number(c):
        raise TypeError("arguments must be numbers")

    """Проверка на корректность значений аргументов"""
    if not check_for_not_negative(a) or not check_for_not_negative(b) or not check_for_not_negative(c):
        raise ValueError("agruments must be not negative")

    return a + b + c 

"""Принимает три числа и проверяет на неравенство треугольника"""
def is_correct_triangle(a, b, c):
    """Проверка на корректность типов аргументов"""
    if not check_for_number(a) or not check_for_number(b) or not check_for_number(c):
        raise TypeError("arguments must be numbers")

    """Проверка на корректность значений аргументов"""
    if not check_for_not_negative(a) or not check_for_not_negative(b) or not check_for_not_negative(c):
        raise ValueError("agruments must be not negative")

    return max(a, b, c) < a + b + c - max(a, b, c)