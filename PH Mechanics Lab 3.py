#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy 


# In[2]:


ball = pd.read_csv("bouncing_ball.csv")
#print(ball)
ball.plot('t')


# In[3]:


line = numpy.polyfit(ball.t, ball.y, 9) #notice that it's t (time) then x (position). 1 refers to linear here. 
#numpy.polyfit? #Uncomment this line if you wish to look a bit closer to the polyfit command
p = numpy.poly1d(line) #Do this to convert it into a usable form for plotting


# In[4]:


fig=plt.figure() #initiate the figure
ax=fig.add_subplot(111) #So we can add multiple lines

ax.plot(ball.t,ball.y, c='b',marker="^",ls='--',label='y',fillstyle='none') #Data is horizontial axis, then vertical axis
#ax.plot(ball.t,ball.y,c='g',marker=(8,2,0),ls='--',label='y') #Saving time versus vertical position for later
ax.plot(ball.t, p(ball.t), c = 'r', ls = '--', label= p) #plotting the linear formula

#plt.text(2, 0.65, 'y = {} x + {}'.format(m, b)

plt.legend(loc=2) #Legends are very useful
plt.draw()
plt.title("Linear trend versus horizontial position")
ax.set_xlabel('time (s)')
ax.set_ylabel('position (m)')
print(p) #So you can see the form of the polynomial that was fitted. In this case it is y = mx + b

#plt.text? #another way to add annotations to a plot


# #### Really though I want to look at the bounces independantly from each other. So I'd rather break it up from the bottom of the first bounce to the beginning of the second bounce. To do that I need to break up the data and then analyze it. I could add the polyfit and up the number of degree's it would look at, but that's quite a bit harder and does not really capture the movement. As you can see above the red line aka the poly fit, does not hit the bottom position. 

# In[5]:


tt = range(11, 20)
y_bounce1 = ball.loc[tt,'y' ]
t_bounce1 = ball.loc[tt,'t']
plt.plot(t_bounce1, y_bounce1)


# In[6]:


fit_bounce1 = numpy.polyfit(t_bounce1, y_bounce1, 2) #notice that it's t (time) then x (position). 1 refers to linear here. 
p = numpy.poly1d(fit_bounce1) #Do this to convert it into a usable form for plotting


# In[7]:


fig=plt.figure() #initiate the figure
ax=fig.add_subplot(111) #So we can add multiple lines

ax.plot(t_bounce1, y_bounce1, c='b',marker="^",ls='--',label='y',fillstyle='none') #Data is horizontial axis, then vertical axis
#ax.plot(ball.t,ball.y,c='g',marker=(8,2,0),ls='--',label='y') #Saving time versus vertical position for later
ax.plot(t_bounce1, p(t_bounce1), c = 'r', ls = '--', label= p) #plotting the linear formula

#plt.text(2, 0.65, 'y = {} x + {}'.format(m, b)

plt.legend(loc=2) #Legends are very useful
plt.draw()
plt.title("Polynomial trend versus vertical position")
ax.set_xlabel('time (s)')
ax.set_ylabel('position (m)')
print(p) #So you can see the form of the polynomial that was fitted. In this case it is y = mx + b
#plt.text? #another way to add annotations to a plot


# In[8]:


vel_y = numpy.diff(y_bounce1) 
acc = numpy.diff(vel_y)

#fit_bounce1 = numpy.polyfit(t_bounce1, vel_y, 1) #notice that it's t (time) then x (position). 1 refers to linear here. 
#p = numpy.poly1d(fit_bounce1) #Do this to convert it into a usable form for plotting


# In[9]:


plt.plot(vel_y)
vel_y


# In[10]:


vel_y


# In[ ]:




