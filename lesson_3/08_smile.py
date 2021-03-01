# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
import random
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
for i in range(10):
    x = random.randint(100, 700)
    y = random.randint(100, 700)
    point = simple_draw.get_point(x, y)
    point_2 = simple_draw.get_point(x - 30, y + 50)
    point_3 = simple_draw.get_point(x + 30, y + 50)
    point_4 = simple_draw.get_point(x - 40, y - 30)
    point_5 = simple_draw.get_point(x + 40, y - 30)
    simple_draw.circle(point, radius=100, width=10)
    simple_draw.circle(point, radius=10, width=10)
    simple_draw.circle(point_2, radius=20, width=10)
    simple_draw.circle(point_3, radius=20, width=10)
    simple_draw.line(point_4, point_5, width=10)

simple_draw.pause()
