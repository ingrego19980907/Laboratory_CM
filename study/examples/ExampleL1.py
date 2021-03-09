print(
    '___Читати дані з таблиці Excel і заноситиме їх у DataFrame, переводячи їх у числові. (шматок минулої проги)___ \n')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile(r'G:\GEXF\МКДС/3.xlsx')

cols = list("ABCDEFGHIJKLMNOPQRSTUVW")
names = []
for i in cols:
    names.append(i * 3)
print(names)


def stint(x):
    return ord(x) / 1000.0  # функція ord(x) надає ascii-код символа x


def stint1(x):
    return 1.0 if x == 'e' else 0.0  # перший стовпчик таблиці є цільовим атрибутом грибів, тому для нього визначається окрема функція


converters = {names[0]: stint1}
for i in names[1:]:
    converters.update({i: stint})

print('\n\n\n___Завдання №2 Створити з DataFrame за допомогою бібліотеки NumPy двовимірний масив.')

df = pd.read_excel(xlsx, usecols=','.join(cols), header=None, names=names, nrows=50, converters=converters)
print(df)
arr = df.to_numpy()
print(arr)

print(
    '\n\n\n___Завдання №3 Вибирати два стовпчики з масиву та за допомогою Matplotlib.pyplot та наноситиме крапки, горизонтальна координата яких буде визначатися значенням у першому стовпчину, а вертикальна - у другому. Точки позначитиме червоними колами..___ \n\n\n')

x = 1
y = 3
plt.scatter(arr[x], arr[y], marker='o', color='r')
plt.show()

print(
    '\n\n\n Завдання №4 За допомогою Matplotlib побудувати контурний графік, що відтворюватиме дані двовимірного масиву. Горизонтальна і вертикальна координати на рисунку визначатимуться двома вимірами масиву.___ \n\n\n')

plt.contour(arr)
plt.show()

print('___Завдання №5 За допомогою Matplotlib будуватиме поверхню, використовуючи дані DataFrame з пукнту 1.___ \n ')

ax = plt.axes(projection='3d')
X = np.arange(0, len(df['BBB']))
Y = np.arange(0, len(df.columns))
X, Y = np.meshgrid(X, Y)
Z = arr[X, Y]
ax.plot_surface(X, Y, Z)
plt.show()

print(
    '___Завдання №6 Перетворюватиме двовимірний масив з пункту 2 у двовимірний масив, в якому розміри обох вимірів співпадають. Розглянути додавання стовпчиків до кількості рядочків та урізання кількості стовпчиків до кількості рядочків.___ \n')

arr1 = []

m = len(arr)
n = len(arr[0])

for i in range(n):
    arr1.append(arr[i])

print(arr1)

arr2 = []
e = np.zeros((m, m - n))
arr2 = np.append(arr, e, axis=1)

print(arr2)

print("__7 Визначатиме власні значення і власні вектори квадратних масивів з пункту 6.")

print('___8 Формуватиме з координат власних векторів новий DataFrame. ___ \n')

print('___9 Рахуватиме скалярні і векторні добутки між двома будь-якими власними векторами пункту 7. ___ \n')

a1, v1 = np.linalg.eigh(arr1)
print(a1, v1)
dfv1 = pd.DataFrame(data=arr1)
s1 = np.dot(v1[0], v1[1])
print(s1)

vec1 = v1[0][0:2]
vec2 = v1[1][0:2]
vd1 = np.cross(vec1, vec2)

print(vd1)

a2, v2 = np.linalg.eigh(arr2)
print(a2, v2)
dfv2 = pd.DataFrame(data=arr2)
s2 = np.dot(v2[0], v2[1])
print(s2)

vec3 = v1[0][0:2]
vec3 = v1[1][0:2]
vd2 = np.cross(vec1, vec2)

print(vd2)

print(
    "___10 Перетворюватиме DataFrame з пункту 8 у двовимірний масив. За правилами добутку матриць множитиме цей масив на масив з пункту 6, з власних векторів якого було побудовано DataFrame у пункті 8. ___ \n")

mat = dfv1.to_numpy().dot(arr1)
print(mat)
