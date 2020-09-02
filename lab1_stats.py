#!/usr/bin/env python
# coding: utf-8

# # Lab 1 Significant Figures etc

# ## Please put your answers here by editing this box, and show your work below. 
# 1)
# 
# 2)
# 
# 3)
# 
# 4)
# 
# 5)
# 
# 6)
# 
# 7)
# 
# 8)
# 
# 9)
# 
# 10)
# 
# 11)
# 
# 12)
# 
# 13)

# In[2]:


# They // we would really like it if you comment every line please and thank you
x1 = 3  
x1u = 0.01
x2 = 4
x2u = 0.01
x3 = 2
x3u = 0.01

x = x1 + x2 + x3
xu = x1u + x2u + x3u

print("x = ", x, 'cm')
print("x uncertainty = ", xu, 'cm')


# In[3]:


import statistics as stat

x = [1,2,3,4,5]
mean = stat.mean(x)
stdev = stat.stdev(x)

print("Mean of x = ",mean)
print("Uncertainty in x = ", stdev)


# In[ ]:





# In[ ]:




