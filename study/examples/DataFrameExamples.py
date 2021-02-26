# --'-----------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      taras
#
# Created:     30.09.2020
# Copyright:   (c) taras 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import \
    pandas as p  # Щоб не використовувати довгу назву pandas, скорочуємо подальше посилання на бібліотеку до однієї літери

# Приклад ініціалізації DataFrame через двовимірний список
data = [['Stepan', 10], ['Ryta', 18], ['Mark', 12], ['Yaroslava', 11]]
df = p.DataFrame(data, index=['1', '2', '3', '4'], columns=['Names', 'Ages'])
print(df)

# Приклад ініціалізації DataFrame через словник списків
data1 = {'Name': ['Stepan', 'Ryta', 'Mark', 'Yaroslava'], 'Age': [10, 18, 12, 11]}
df1 = p.DataFrame(data1, index=['AA', 'AB', 'BA', 'BB'])
print(df1)

# Приклад ініціалізації DataFrame зі списка словників
students = [{'Name': 'Stepan', 'Age': 10}, {'Name': 'Ryta', 'Age': 24}, {'Name': 'Mark', 'Age': 19},
            {'Name': 'Yaroslava', 'Age': 15}]
df2 = p.DataFrame(students, index=['2', '4', '6', '8'])
print(df2)

# Дії зі стовпчиками
df['Weight'] = 4.3 * df['Ages'] - df['Ages']
print(df)

# Виділення рядків
print(df.loc['1'])
print(df.loc['4'])

# Додавання рядків
df1 = df1.append(df2)
print(df1)

# Видалення стовпчика
del (df1['Name'])

print(df1)

ds = p.Series({'a': [0, 1, 2], 'b': [2, 1, 4], 'c': [3, 2, 1]})
print(ds)
df4 = p.DataFrame(ds, columns=['Numbers'])
print(df4)
