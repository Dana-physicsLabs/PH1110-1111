#!/usr/bin/env python
# coding: utf-8

# # How to add error bars to a plot

# Sourced from https://pythonhealthcare.org/2018/04/13/51-matplotlib-adding-error-bars-to-charts/

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

# example data
x = np.arange(0.1, 10, 1)
y = x ** 2

# calculate example errors (could also be from list or NumPy array)
lower_y_error = y * 0.2
upper_y_error = y * 0.3
y_error = [lower_y_error, upper_y_error]
lower_x_error = x * 0.05
upper_x_error = x * 0.05
x_error = [lower_x_error, upper_x_error]

# To use only x or y errors simple omit the relevant argument

plt.errorbar(x, y, yerr = y_error, xerr = x_error, fmt='-o')

plt.show()


# In[ ]:




