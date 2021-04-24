import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt

print(
    '\n\n\n\n\n___Завдання №1 Читати дані з таблиці Excel і заноситиме їх у DataFrame, переводячи їх у числові, '
    'та рахуватиме ентропію усієї сукупності грибів')


xlsx = pd.ExcelFile(r'C:\Python\Project\Study\Laboratory\Tasks\Task_1\Task_1.xlsx')


def stint(x):
    return ord(x) / 100.0


def stint1(x):
    return 1.0 if x == 'e' else 0.0


cols = list("ABCDEFGHIJKLMNOPQRSTUVW")

names = []
for i in cols:
    names.append(i * 2)

converters = {names[0]: stint1}
for i in names[1:]:
    converters.update({i: stint})

df = pd.read_excel(xlsx, usecols='A:W', header=None, names=names, nrows=50, converters=converters)
print(df)

sorted_df = df.sort_values(by='AA')

sorted_df.to_excel('C:/Python/Project/Study/Laboratory/Tasks/Task_1/result_1.xlsx', header=False, index=False)


print('\n\n\n\n\n___Завдання №2 Рахуватиме прирости інформації для усіх нецільових атрибутів грибів.')

print('\n\n\n\n\n___Завдання №3 За будь-якими 25 грибами таблиці будуватиме класифікаційні дерева для одного –двадцяти'
      'найбільш інформативних параметрів.')

print('\n\n\n\n\n___Завдання №4 Застосовуватиме класифікаційні дерева до решти 25 грибів. Для кожного класифікаційного'
      'дерева вираховуватиме кількість помилок класифікації решти 25 грибів та будуватиме'
      'залежність кількості помилок від розміру класифікаційного дерева. ')

print('\n\n\n\n\n___Завдання №5 Будуватиме класифікаційні моделі на основі перцептрона Розенблата.'
      'Застосувати модель для 25 грибів на двох атрибутах та двох алгебраїчних комбінаціях сукупності атрибутів. '
      'Перевірити роботу моделей на решті 25 грибах.')
