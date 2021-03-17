
# coding: utf-8

# *Python Machine Learning 2nd Edition* by [Sebastian Raschka](https://sebastianraschka.com), Packt Publishing Ltd. 2017
#
# Code Repository: https://github.com/rasbt/python-machine-learning-book-2nd-edition
#
# Code License: [MIT License](https://github.com/rasbt/python-machine-learning-book-2nd-edition/blob/master/LICENSE.txt)

# # Python Machine Learning - Code Examples

# # Chapter 2 - Training Machine Learning Algorithms for Classification

# Note that the optional watermark extension is a small IPython notebook plugin that I developed to make the code reproducible. You can just skip the following line(s).

# In[1]:




# *The use of `watermark` is optional. You can install this IPython extension via "`pip install watermark`". For more information, please see: https://github.com/rasbt/watermark.*

# ### Overview
#

# - [Artificial neurons – a brief glimpse into the early history of machine learning](#Artificial-neurons-a-brief-glimpse-into-the-early-history-of-machine-learning)
#     - [The formal definition of an artificial neuron](#The-formal-definition-of-an-artificial-neuron)
#     - [The perceptron learning rule](#The-perceptron-learning-rule)
# - [Implementing a perceptron learning algorithm in Python](#Implementing-a-perceptron-learning-algorithm-in-Python)
#     - [An object-oriented perceptron API](#An-object-oriented-perceptron-API)
#     - [Training a perceptron model on the Iris dataset](#Training-a-perceptron-model-on-the-Iris-dataset)
# - [Adaptive linear neurons and the convergence of learning](#Adaptive-linear-neurons-and-the-convergence-of-learning)
#     - [Minimizing cost functions with gradient descent](#Minimizing-cost-functions-with-gradient-descent)
#     - [Implementing an Adaptive Linear Neuron in Python](#Implementing-an-Adaptive-Linear-Neuron-in-Python)
#     - [Improving gradient descent through feature scaling](#Improving-gradient-descent-through-feature-scaling)
#     - [Large scale machine learning and stochastic gradient descent](#Large-scale-machine-learning-and-stochastic-gradient-descent)
# - [Summary](#Summary)


# In[2]:


from IPython.display import Image


# # Artificial neurons - a brief glimpse into the early history of machine learning

# In[3]:




# ## The formal definition of an artificial neuron

# In[4]:




# ## The perceptron learning rule

# In[5]:




# In[6]:





# # Implementing a perceptron learning algorithm in Python

# ## An object-oriented perceptron API

# In[7]:


import numpy as np


class Perceptron(object):
    """Perceptron classifier.

    Parameters
    ------------
    eta : float
      Learning rate (between 0.0 and 1.0)
    n_iter : int
      Passes over the training dataset.
    random_state : int
      Random number generator seed for random weight
      initialization.

    Attributes
    -----------
    w_ : 1d-array
      Weights after fitting.
    errors_ : list
      Number of misclassifications (updates) in each epoch.

    """
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X : {array-like}, shape = [n_samples, n_features]
          Training vectors, where n_samples is the number of samples and
          n_features is the number of features.
        y : array-like, shape = [n_samples]
          Target values.

        Returns
        -------
        self : object

        """
        #Ініціалізації ваг випадковими числами
        #Спочатку створюємо одновимірний масив випадкових чисел
        rgen = np.random.RandomState(self.random_state)
        #З цього масиву з центром у loc=0.0 з дисперсією scale=0.01
        #створюємо масив розміру size=1 + X.shape[1] (X.shape[1]
        #дає кількість стовпчиків)
        self.w_=rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])

        #Змінимо спосіб ініціалізації ваг
        N=X.shape[1]
        nar=[]
        for i in range(N+1):
            nar.append(0.9)
        self.w_=np.array(nar)
        print(self.w_)
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


# In[8]:


v1 = np.array([1, 2, 3])
v2 = 0.5 * v1
np.arccos(v1.dot(v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))



# ## Training a perceptron model on the Iris dataset

# ...

# ### Reading-in the Iris data

# In[9]:


import pandas as pd
import math

def stint(x):
    return ord(x)/1000.0

df = pd.read_excel(r'G:\GEXF\МКДС/3.xlsx', usecols='A,B,C,D,E,F,G,J,M,K,W', header=None,names=[0,1,2,3,4,5,6,7,8,9,10],converters={1:stint, 2:stint,3:stint, 4:stint,5:stint, 6:stint,7:stint, 8:stint,9:stint, 10:stint})
print(df)
"""df = pd.read_csv('https://archive.ics.uci.edu/ml/'
         'machine-learning-databases/iris/iris.data', header=None)"""



# <hr>
#
# ### Note:
#
#
# You can find a copy of the Iris dataset (and all other datasets used in this book) in the code bundle of this book, which you can use if you are working offline or the UCI server at https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data is temporarily unavailable. For instance, to load the Iris dataset from a local directory, you can replace the line
#
#     df = pd.read_csv('https://archive.ics.uci.edu/ml/'
#         'machine-learning-databases/iris/iris.data', header=None)
#
# by
#
#     df = pd.read_csv('your/local/path/to/iris.data', header=None)
#

# In[10]:


#df = pd.read_excel('iris.data', header=None)
#df.tail()


# <hr>


# ### Plotting the Iris data

# In[11]:


import matplotlib.pyplot as plt
import numpy as np

# select setosa and versicolor
y = df.iloc[0:50, 0].values
y = np.where(y == 'p', -1, 1)

# extract sepal length and petal length
X = df.iloc[0:50, [1, 2]].values-df.iloc[0:50, [3, 4]].values+df.iloc[0:50, [5, 6]].values+1.1*df.iloc[0:50, [7, 8]].values-1.1*df.iloc[0:50, [9, 10]].values

# plot data
for i in range(50):
    if(y[i]==-1):
        plt.scatter(X[i, 0], X[i, 1],
            color='red', marker='o')
    else:
        plt.scatter(X[i, 0], X[i, 1],
            color='blue', marker='x')

plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

# plt.savefig('images/02_06.png', dpi=300)
plt.show()



# ### Training the perceptron model

# In[12]:


ppn = Perceptron(eta=0.1, n_iter=20)

ppn.fit(X, y)

plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')

# plt.savefig('images/02_07.png', dpi=300)
plt.show()



# ### A function for plotting decision regions

# In[13]:


from matplotlib.colors import ListedColormap


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



# In[14]:


plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')


# plt.savefig('images/02_08.png', dpi=300)
plt.show()

