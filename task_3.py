# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
from math import sqrt

def check_input(a: list):
    if len(a) != 2:
        print('У точки должно быть две координаты.')
        return False
    for i, el in enumerate(a):
        try:
            el = int(el)
        except ValueError:
            print('Координаты точки записываются числами')
            return False
        a[i] = el
    return tuple(a)

a = False
b = False
while not(a and b):
    if not a:
        a = list(input('Введите координаты точки а через запятую: ').split(','))
        a = check_input(a)
    if not b:
        b = list(input('Введите координаты точки b через запятую: ').split(','))
        b = check_input(b)

d = round(sqrt((b[1]-a[1])**2 + (b[0]-a[0])**2), 2)
print(f'A {a}; B {b} -> {d}')
