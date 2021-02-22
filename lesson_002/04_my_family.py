#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Mother', 'Father', 'Julia', 'Katia', 'Dima']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]

my_family_height = [['Father', 170], ['Mother', 155], ['Julia', 168], ['Katia', 160], ['Dima', 104]]

print(my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('height my father ', my_family_height[0][1], ' cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
general_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + \
                 my_family_height[4][1]
print('my family general height ', general_height, ' cm')
