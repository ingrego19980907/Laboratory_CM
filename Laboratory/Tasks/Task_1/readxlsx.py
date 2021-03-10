import pandas as pd
import numpy as np
import matplotlib.pyplot as mplt

print(
    '\n\n\n\n\n___Завдання №1 Прочитати з файлу Excel у DataFrame за допомогою бібліотеки Pandas, '
    'перетворююючи символи на числа')

xlsx = pd.ExcelFile(r'C:\Python\Project\Study\Laboratory\Tasks\Task_1\Task_1.xlsx')


def stint(x):
    return ord(x) / 100.0  #


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

# sorted_df.to_excel('C:/Python/Project/Study/Laboratory/Tasks/Task_1/result_1.xlsx', header=False, index=False)

# task_2
print('\n\n\n\n\n___Завдання №2 Створити з DataFrame за допомогою бібліотеки NumPy двовимірний масив.')

arr_main = np.array(sorted_df)
print(arr_main)

# task_3
print(
    '\n\n\n\n\n___Завдання №3 Вибирати два стовпчики з масиву та за допомогою Matplotlib.pyplot та наноситиме крапки,'
    'горизонтальна координата яких буде визначатися значенням у першому стовпчину, а вертикальна - у другому.'
    ' Точки позначитиме червоними колами..___ \n\n\n\n\n')

# ax1 = mplt.subplots()
# x = 6
# y = 5
# mplt.scatter()
# ax1.plot(x, y, marker='o', color='grey')
# mplt.show()
x_1 = 2
y_1 = 3
for i in range(0, len(arr_main)):
    mplt.scatter(arr_main[i][x_1], arr_main[i][y_1], label='task_3', marker='o', color='b')
mplt.show()

# task_4
print(
    '\n\n\nЗавдання №4 За допомогою Matplotlib побудувати контурний графік, що відтворюватиме дані двовимірного масиву.'
    ' Горизонтальна і вертикальна координати на рисунку визначатимуться двома вимірами масиву.___ \n\n\n')

mplt.contour(arr_main)
mplt.show()

# task_5
print(
    '___Завдання №5 За допомогою Matplotlib будуватиме поверхню, використовуючи дані DataFrame з пукнту 1.___ \n\n\n ')

given_axes = mplt.axes(projection='3d')
X = np.arange(0, len(df['AA']))
Y = np.arange(0, len(df.columns))
arr_x, arr_y = np.meshgrid(X, Y)
arr_x_and_y = arr_main[arr_x, arr_y]
given_axes.plot_surface(arr_x, arr_y, arr_x_and_y)
mplt.show()

# task_6
print(
    '___Завдання №6 Перетворюватиме двовимірний масив з пункту 2 у двовимірний масив,'
    ' в якому розміри обох вимірів співпадають. Розглянути додавання стовпчиків до кількості рядочків та'
    ' урізання кількості стовпчиків до кількості рядочків.___ \n')

# first way
arr_subtracted_1 = []

lines = len(arr_main)
pillars = len(arr_main[0])

for i in range(pillars):
    arr_subtracted_1.append(arr_main[i])

arr_subtracted_res = np.array(arr_subtracted_1)
print(arr_subtracted_res)

# second way
print('\n\n\n\n')

arr_subtracted_2 = []

lines_2 = 10
pillars_2 = 10

for i in range(pillars_2):
    arr_subtracted_2.append(arr_main[i][:lines_2])

arr_subtracted_res_2 = np.array(arr_subtracted_2)
print(arr_subtracted_res_2)


arr_add_zero = []
add_zero = np.zeros((lines, lines - pillars))
arr_add_zero = np.append(arr_main, add_zero, axis=1)

print(arr_add_zero)

# task_7
print("__7 Визначатиме власні значення і власні вектори квадратних масивів з пункту 6.")

eigenvalues_1, vector_1 = np.linalg.eigh(arr_subtracted_1)
print(eigenvalues_1, '\nВектор 1 \n', vector_1)
eigenvalues_2, vector_2 = np.linalg.eigh(arr_subtracted_2)
print(eigenvalues_2, '\nВектор 2 \n', vector_2)

# task_8
print('___8 Формуватиме з координат власних векторів новий DataFrame. ___ \n\n\n')

df_vector_1 = pd.DataFrame(data=vector_1, columns=None, index=None)
df_vector_2 = pd.DataFrame(data=vector_2, columns=None, index=None)
print('=======================================================================\n', df_vector_1,
      '=======================================================================\n', df_vector_2)
# task_9
print('___9 Рахуватиме скалярні і векторні добутки між двома будь-якими власними векторами пункту 7. ___ \n')

scal_mult_1 = np.dot(vector_1[0], vector_1[1])
print('Скалярний добуток вектора 1 = ', scal_mult_1)
scal_mult_2 = np.dot(vector_2[0], vector_2[1])
print('Скалярний добуток вектора 2 = ', scal_mult_2)

vector_1_until_2_value = vector_1[0][0:2]
vector_2_until_2_value = vector_1[1][0:2]
vectors_mlt_1 = np.cross(vector_1_until_2_value, vector_2_until_2_value)

print('Векторний добуток вектора 1 = ', vectors_mlt_1)


vector_3_until_2_value = vector_2[0][0:2]
vector_4_until_2_value = vector_2[1][0:2]
vectors_mlt_2 = np.cross(vector_3_until_2_value, vector_4_until_2_value)

print('Векторний добуток вектора 2 = ', vectors_mlt_2)

# task_10
print(
    "\n\n\n___10 Перетворюватиме DataFrame з пункту 8 у двовимірний масив."
    " За правилами добутку матриць множитиме цей масив на масив з пункту 6,"
    " з власних векторів якого було побудовано DataFrame у пункті 8. ___ \n")

mat = df_vector_2.to_numpy().dot(arr_subtracted_2)
print(mat)

