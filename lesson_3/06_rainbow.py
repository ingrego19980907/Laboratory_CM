# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
point_1 = sd.get_point(x=50,y=50)
point_2 = sd.get_point(x=350, y=450)
x1, y1, x2, y2 = 50, 50, 350, 450
for color in rainbow_colors:
    point_1 = sd.get_point(x1, y1)
    point_2 = sd.get_point(x2, y2)
    sd.line(start_point=point_1, end_point=point_2, color=color, width=1)
    x1 += 5
    x2 += 5
    y1 += 5
    y2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
for color in rainbow_colors:
    point = sd.get_point(500, -500)

    sd.circle(point, radiuse, color, 10)
    radiuse += 20

sd.pause()
