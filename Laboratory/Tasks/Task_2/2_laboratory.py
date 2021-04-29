from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.colors import ListedColormap

print(
    '\n\n\n\n\n___Завдання №1 Читати дані з таблиці Excel і заноситиме їх у DataFrame, переводячи їх у числові, '
    'та рахуватиме ентропію усієї сукупності грибів')

xlsx = pd.ExcelFile(r'C:\Python\Project\Study\Laboratory\Tasks\Task_1\Task_1.xlsx')


def stint(x):
    return ord(x) / 1000.0


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

sorted_df = df.sort_values(by='AA')

sorted_df.to_excel('C:/Python/Project/Study/Laboratory/Tasks/Task_1/result_1.xlsx', header=False, index=False)

print(sorted_df)

# порахуємо кількість рядків у PE з різними значеннями
elem_count = df.shape[0]
print('elem_count=', elem_count, end='\n\n')

"""обчислимо ймовірності появи їстівних і отруйних грибів (частоти значень у першому стовпчику)
у батьківській групі і занесемо її до словника. Ключу "1"
відповідатиме ймовірність появи істівного гриба, а клчу
"0" - ймовірність появи отруйного"""

dict_probability = df['AA'].value_counts() / elem_count
MainEntropy = -dict_probability[0] * math.log(dict_probability[0]) - dict_probability[1] * math.log(dict_probability[1])
print('MainEntropy', MainEntropy)
print("Виводимо словник ймовірностей! \n", dict_probability, end='\n\n')

# # Створюємо словник вловників, в якому ключами будуть значення, а елементами кількість об'єктів в кожній групі
list_of_dicts_val_and_qunt = []
for i in sorted_df:
    dict_value_and_quant = df[i].value_counts()
    list_of_dicts_val_and_qunt.append(dict_value_and_quant)

print('список словників, list_of_dicts_val_and_qunt\n', list_of_dicts_val_and_qunt, end='\n\n')

# Створюємо список списків ключів словників
list_of_lists_keys_of_dicts = []
for dict in list_of_dicts_val_and_qunt:
    keys_list = []
    for key in dict.keys():
        keys_list.append(key)
    list_of_lists_keys_of_dicts.append(keys_list)

print('list_of_lists_keys_of_dicts\n', list_of_lists_keys_of_dicts, end='\n\n')

# list Кількості груп
list_of_ngroup = []
for list_keys in list_of_lists_keys_of_dicts:
    ngroup = len(list_keys)
    list_of_ngroup.append(ngroup)
print('list_of_ngroup\n', list_of_ngroup, end='\n\n')

# # Створюємо список кількостей елементів у кожній групі

list_of_lists_nig = []
for dict in list_of_dicts_val_and_qunt:
    value_list = []
    for key in dict.keys():
        value_list.append(dict[key])
    list_of_lists_nig.append(value_list)

print('list_of_lists_nig\n', list_of_lists_nig, end='\n\n')

# Середнє значення
list_average_values = []
for k in range(len(list_of_lists_keys_of_dicts)):
    average_value = 0.
    for i in range(len(list_of_lists_keys_of_dicts[k])):
        average_value += list_of_lists_keys_of_dicts[k][i] * list_of_lists_nig[k][i] / elem_count
    list_average_values.append(round(average_value, 3))
print('average value\n', list_average_values, end='\n\n')

list_of_dicts_namecol_aver_val = []
for av in list_average_values:
    VaV = {}
    for col in names:
        VaV.update({col: av})
    list_of_dicts_namecol_aver_val.append(VaV)
print('list_of_dicts_namecol_aver_val')
for dict in list_of_dicts_namecol_aver_val:
    print(dict)

# # Створюємо список кількостей одиниць і нулів у кожній групі
# # Зовнішній вимір буде відповідати кількості груп, а внутрішній - дорівнює двом,
# тобто відповідає двом різним значенням у першому стовпчику

list_of_lists_sss = []

for n_group in list_of_ngroup:
    sss = []
    for i in range(n_group):
        sss.append([])
        for j in range(2):
            sss[i].append(0.0)
    list_of_lists_sss.append(sss)
print('list_sss\n', list_of_lists_sss)

# # Рахуємо кількість нулів та одиниць у першому стовпчику для кожної з груп

k = -1
for key in sorted_df:
    k += 1
    for i in range(elem_count):
        for j in range(list_of_ngroup[k]):
            if sorted_df[key][i] == list_of_lists_keys_of_dicts[k][j]:  # Вибираємо елемент j-ої групи
                if sorted_df['AA'][i] == 0.0:  # Якщо стовпчику PE для цільового атрибута стоїть значення нуль, то
                    list_of_lists_sss[k][j][0] += 1.  # рахуємо нулі і результат заносимо на першу позицію j-ої групи
                else:
                    list_of_lists_sss[k][j][1] += 1.
                    # У іншому випадку рахуємо одиниці і результат заносимо на другу позицію j-ої групи

print('list_sss\n', list_of_lists_sss)

# # Рахуємо ентропії для кожної з груп

list_Entropy = []

k = 0
for list_sss in list_of_lists_sss[1:]:
    entropy = []
    k += 1
    for i in range(len(list_sss)):
        EG = 0.
        if list_sss[i][0] != 0.:
            EG = EG - list_sss[i][0] / list_of_lists_nig[k][i] * math.log(
                list_sss[i][0] / list_of_lists_nig[k][i])  # Якщо кількість елементів в і-ій групі з
            # нульовими значеннями в першому стовпчику дорівнює нулю, то дія не виконується
        if list_sss[i][1] != 0.:
            EG = EG - list_sss[i][1] / list_of_lists_nig[k][i] * math.log(
                list_sss[i][1] / list_of_lists_nig[k][i])  # Якщо кількість елементів в і-ій групі зi
            # значеннями "одиниця" в першому стовпчику дорівнює нулю, то дія не виконується
        entropy.append(EG)
    list_Entropy.append(entropy)

print('list of Entropy')

for entropy in list_Entropy:
    print(entropy)

print('\n\n\n\n\n___Завдання №2 Рахуватиме прирости інформації для усіх нецільових атрибутів грибів.')

IG_list = []
k = 0
for entropy in list_Entropy:
    IG = MainEntropy
    k += 1
    for i in range(len(entropy)):
        IG -= entropy[i] * list_of_lists_nig[k][i] / elem_count
    IG_list.append(IG)

IG_dict = {}
k = 0
for val in IG_list:
    k += 1
    IG_dict[names[k]] = val

print('MainEntropy=', MainEntropy)
print('InformationGrowth:', )
pprint(IG_dict)


print('\n\n\n\n\n___Завдання №5 Будуватиме класифікаційні моделі на основі перцептрона Розенблата.'
      'Застосувати модель для 25 грибів на двох атрибутах та двох алгебраїчних комбінаціях сукупності атрибутів. '
      'Перевірити роботу моделей на решті 25 грибах.')



class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):

        rgen = np.random.RandomState(self.random_state)
        self.w_= rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)


def plot_decision_regions(X, y, classifier, resolution=0.02):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for (idx,cl) in enumerate(np.unique(y)):
        print(type(idx))
        print(type(cl))
        print(type((idx,cl)))
        plt.scatter(X[y == cl,0],
                    X[y == cl,1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolor='black')


QUANT_DATA = 25

df_2 = pd.read_excel(r'C:\Python\Project\Study\Laboratory\Tasks\Task_1\Task_1.xlsx', usecols='A,B,C',
                     header=None, names=['A', 'B', 'C'], converters={1: stint, 2: stint}, nrows=QUANT_DATA)

sorted_df_2 = df_2.sort_values('A')
print(sorted_df_2)
y = df_2.iloc[0:50, 0].values
y = np.where(y == 'p', -1, 1)

print('y\n', y)
# extract sepal length and petal length
X = df_2.iloc[0:50, [1, 2]].values
print('X\n', X)


# plot data

for i in range(QUANT_DATA):
    if y[i] == -1:
        plt.scatter(X[i, 0], X[i, 1], color='red', marker='o')
    else:
        plt.scatter(X[i, 0], X[i, 1], color='blue', marker='x')


plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()


ppn = Perceptron(eta=0.1, n_iter=5000)

ppn.fit(X, y)

plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.show()


plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()


# Оскільки класи отруйних і їстівних грибів не можна розділити прямою
# то ми не зможеммо досконально навчити наш перцептрон.
# У даній лабораторній я зозумів основну концепцію машиного навчання,
# Використав данні ірисів, там отримались гарні результати.
# А з грибами які б параметри не брав, нормальних результатів не отримав.
# Висновок можу зробити, що треба більше данних для якісного навчання.
