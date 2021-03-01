# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
x1, y1, x2, y2 = 0, 0, 100, 50
for j in range(12):

    for i in range(15):
        lbotom = sd.get_point(x1, y1)
        r_top = sd.get_point(x2, y2)
        sd.rectangle(lbotom, r_top, sd.random_color(), width=5)
        x1 += 100
        x2 += 100
    x1 -= 1550
    x2 -= 1550
    y1 += 50
    y2 += 50



sd.pause()
