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

import \
    pandas as pd  # Щоб не використовувати довгу назву pandas, скорочуємо подальше посилання на бібліотеку до двох літер


# допоміжні функції для переведення символів з таблиці Excel у числа
def stint(x):
    return ord(x) / 1000.0  # функція ord(x) надає ascii-код символа x


def stint1(x):
    return 1.0 if x == 'e' else 0.0
    # перший стовпчик таблиці є цільовим атрибутом грибів, тому для нього визначається окрема функція


xlsx = pd.ExcelFile(r'G:\GEXF\МКДС\3.xlsx')
# вводиться змінна xlsx, яка має значення рядка, що є фізичною адресою файла Excel

# Читаємо окремі стовпчики з файлу за адресою xlsx
# Параметр usecols='A,C,F' задає назви стовпчиків, які читаються і заносяться у стовпчики DataFrame df
# Параметр header=None задає номер рядка у файлі xlsx, з якого зчитуються назви стовпчиків у DataFrame df
# У нашому випадку ми не читаємо назв стовпчиків, щоб не втратити даних з 'нульового' рядка, який у файлі Excel є першим
# Параметром-списком names=['AA','CC','FF'] ми вручну задаємо назви стовпчиків DataFrame df. Ці назви можна взяти з якогось іншого файла, сформувавши список
# nrows=50 - кількість рядків, що читаються з xlsx
# converters={'AA':stint1,'CC':stint,'FF':stint} - конвертування даних стовпчиків
df = pd.read_excel(xlsx, usecols='A,C,F', header=None, names=['AA', 'CC', 'FF'], nrows=50,
                   converters={'AA': stint1, 'CC': stint, 'FF': stint})
print(df)

# сортуємо дані за стовпчиком СС
sorted_df = df.sort_values(by='CC')

# записують результат сортування у файл Excel за допомогою функції to_excel
sorted_df.to_excel('G:/GEXF/МКДС/31.xlsx', header=False, index=False)

# порахуємо кількість рядків у СС з різними значеннями
aa = df['CC'].value_counts()
print(aa)

with pd.ExcelWriter('G:/GEXF/МКДС/3n.xlsx') as writer:
    df.to_excel(writer)
