# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      taras
#
# Created:     17.11.2020
# Copyright:   (c) taras 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

lst = [[1, 2, 3], [4, 5, 6]]
ar2d = np.array(lst)
print(ar2d)
float32_ar2d = ar2d.astype(np.float32)
print(float32_ar2d)
number_elements = ar2d.size
print('number_elements=', number_elements)
number_dimensions = ar2d.ndim
print('number_dimensions=', number_dimensions)
shapes = ar2d.shape
print('shapes=', shapes)
shape1 = ar2d.shape[0]
print('shape1=', shape1)

generator_expression = (i for i in range(10) if i % 3)
ar1d = np.fromiter(generator_expression, dtype=int)
print(ar1d)
ar3d = np.zeros((3, 3, 3))
print(ar3d)
ar5d = np.ones((3, 3, 3, 3, 3))
print(ar5d)
arE = np.eye(4)
print(arE)
print(arE[:2][:2])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.show()  # Вивід результату на монітор

import math

x = np.linspace(0, 2, 100)
generator_expression = (math.sin(x[i]) for i in range(100))
y = np.fromiter(generator_expression, dtype=np.float32)
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig1, ax1 = plt.subplots()  # Create a figure and an axes.
ax1.plot(x, x, label='linear', marker='x', color='blue')  # Plot some data on the axes.
ax1.plot(x, x ** 2, label='quadratic', marker='*', color='green')  # Plot more data on the axes...
ax1.plot(x, x ** 3, label='cubic', marker='+', color='black')  # ... and some more.
ax1.plot(x, y, label='sin', marker='o', color='grey')  # ... and some more.
ax1.set_xlabel('x Axis')  # Add an x-label to the axes.
ax1.set_ylabel('y Axis')  # Add a y-label to the axes.
ax1.set_title("Simple Plot")  # Add a title to the axes.
ax1.legend()  # Add a legend.
ax1.axes.set_xlim(0.5, 1.5)
ax1.axes.set_ylim(-1., 5.)
plt.show()

fig2, ax2 = plt.subplots()
ax2.plot(x, x, y, label='linear', marker='x', color='blue')
plt.show()
