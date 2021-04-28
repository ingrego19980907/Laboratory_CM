# -------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      taras
#
# Created:     29.09.2020
# Copyright:   (c) taras 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import pandas as pd  # Щоб не використовувати довгу назву pandas, скорочуємо подальше посилання на бібліотеку
import math


# допоміжні функції для переведення символів з таблиці Excel у числа
def stint(x):
    return ord(x) / 1000.0  # функція ord(x) надає ascii-код символа x


def stint1(x):
    return 1.0 if x == 'e' else 0.0  # перший стовпчик таблиці є цільовим атрибутом грибів,
                                     # тому для нього визначається окрема функція


xlsx = pd.ExcelFile(r'C:\Python\Project\Study\Laboratory\Tasks\Task_1\Task_1.xlsx')
# вводиться змінна xlsx, яка має значення рядка, що є фізичною адресою файла Excel
"""Читаємо окремі стовпчики з файлу за адресою xlsx
#Параметр usecols='A,B' задає назви стовпчиків, які
читаються і заносяться у стовпчики DataFrame df
#Параметр header=None задає номер рядка у файлі xlsx,
з якого зчитуються назви стовпчиків у DataFrame df
#У нашому випадку ми не читаємо назв стовпчиків, щоб не
втратити даних з 'нульового' рядка, який у файлі Excel
є першим #Параметром-списком names=['PE','Diameter'] ми вручну
задаємо назви стовпчиків DataFrame df. Ці назви можна взяти
з якогось іншого файла, сформувавши список
#nrows=50 - кількість рядків, що читаються з xlsx
#converters={'PE':stint1,'Diameter':stint} -
конвертування даних стовпчиків"""
namescol = ['PE', 'Diameter']
df = pd.read_excel(xlsx, usecols='A,B', header=None, names=namescol, nrows=50,
                   converters={'PE': stint1, 'Diameter': stint})

# сортуємо дані за стовпчиком СС
sorted_df = df.sort_values(by='PE')

# записують результат сортування у файл Excel за допомогою функції to_excel
sorted_df.to_excel('C:/Python/Project/Study/Laboratory/Tasks/Task_1/result_1.xlsx', header=False, index=False)

df['CC'] = df['PE'] + df['Diameter']
df['FF'] = 10. * df['CC'] - df['Diameter']
print(df)

# порахуємо кількість рядків у PE з різними значеннями
elem_count = df.shape[0]
print('elem_count=', elem_count)
"""обчислимо ймовірності появи їстівних і отруйних грибів (частоти значень у першому стовпчику)
у батьківській групі і занесемо її до словника. Ключу "1"
відповідатиме ймовірність появи істівного гриба, а клчу
"0" - ймовірність появи отруйного"""
bb = {}
bb = df['PE'].value_counts() / elem_count
MainEntropy = -bb[0] * math.log(bb[0]) - bb[1] * math.log(bb[1])
print("Виводимо словник ймовірностей! \n", bb)
# # Створюємо словник, в якому ключами будуть значення, а елементами кількість об'єктів в кожній групі

duct_value_and_quant = df['Diameter'].value_counts()
print('cc =\n', duct_value_and_quant, )
# Створюємо список ключів словника сс
kl = []
for s in duct_value_and_quant.keys():
    kl.append(s)
print(kl)
# Кількість груп
ngroup = len(kl)
print(ngroup)
# # Створюємо список кількостей елементів у кожній групі
nig = []
for i in range(ngroup):
    nig.append(duct_value_and_quant[kl[i]])
print('nig=', nig)
av = 0.
for i in range(len(kl)):
    av += kl[i] * nig[i] / elem_count
print('average value', av)
vav = {"Diameter": av}
VaV = {}
for col in namescol:
    VaV.update({col: av})
print(VaV)
# # Створюємо список кількостей одиниць і нулів у кожній групі
# # Зовнішній вимір буде відповідати кількості груп, а внутрішній - дорівнює двом, тобто відповідає двом різним значенням
# # у першому стовпчику
sss = []
for i in range(ngroup):
    sss.append([])
    for j in range(2):
        sss[i].append(0.0)
print(sss)
# # Рахуємо кількість нулів та одиниць у першому стовпчику для кожної з груп
for i in range(elem_count):
    for j in range(ngroup):
        if df['Diameter'][i] == kl[j]:  # Вибираємо елемент j-ої групи
            if df['PE'][i] == 0.0:  # Якщо стовпчику PE для цільового атрибута стоїть значення нуль, то
                sss[j][0] += 1.  # рахуємо нулі і результат заносимо на першу позицію j-ої групи
            else:
                sss[j][1] += 1.
                # У іншому випадку рахуємо одиниці і результат заносимо на другу позицію j-ої групи
print(sss)
# # Рахуємо ентропії для кожної з груп
Entropies = []
for i in range(ngroup):
    EG = 0.
    if sss[i][0] != 0.:
        EG = EG - sss[i][0] / nig[i] * math.log(sss[i][0] / nig[i]) # Якщо кількість елементів в і-ій групі з
        # нульовими значеннями в першому стовпчику дорівнює нулю, то дія не виконується
    if sss[i][1] != 0.:
        EG = EG - sss[i][1] / nig[i] * math.log(sss[i][1] / nig[i])  # Якщо кількість елементів в і-ій групі зi
        # значеннями "одиниця" в першому стовпчику дорівнює нулю, то дія не виконується

    Entropies.append(EG)

print(Entropies)

# # Розрахунок приросту інформації для стовпчика Diameter
IG = MainEntropy
for i in range(ngroup):
    IG -= Entropies[i] * nig[i] / elem_count

print('MainEntropy=', MainEntropy)
print('InformationGrowth=', IG)
