# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      taras
#
# Created:     23.11.2020
# Copyright:   (c) taras 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import numpy as np

# Створюється пара масивів з першої і другої координат сітки
xx1, xx2 = np.meshgrid(np.arange(0., 1., 0.2), np.arange(0., 1., 0.2))
print('xx1=', xx1)
print('xx2=', xx2)
# Створюється масив двовимірних точок сітки
xx3 = np.array([xx1.ravel(), xx2.ravel()]).T
print('xx3=', xx3)
