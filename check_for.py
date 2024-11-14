"""Принипает переменную и возвращает является ли она числом"""
def check_for_number(data):
    if type(data) == int or type(data) == float:
        return True
    return False

"""Принимает число и возвращает является ли оно неотрицательным"""
def check_for_not_negative(data):
    if data >= 0:
        return True
    return 0