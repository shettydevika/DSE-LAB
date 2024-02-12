#Python program to display multiple types of charts using Matplotlib package

import matplotlib.pyplot as plt
import numpy as np

#LINE CHART
x=np.linspace(0,10,100)
y=np.sin(x)
plt.figure()
plt.plot(x,y)
plt.title("LINE CHART")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#BAR CHART
categories=['A', 'B', 'C', 'D']
values=[20,35,30,25]
plt.figure()
plt.bar(categories, values)
plt.title("BAR CHART")
plt.xlabel("CATEGORIES")
plt.ylabel("VALUES")

#SCATTER PLOT
x=np.random.randn(100)
y=np.random.randn(100)
colors=np.random.rand(100)
sizes=100*np.random.rand(100)
plt.figure()
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5)
plt.title("SCATTER PLOT")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#PIE CHART
sizes=[30,20,25,15,10]
labels=['A', 'B', 'C', 'D', 'E']
plt.figure()
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("PIE CHART")

#SHOW ALL THE CHARTS
plt.show()
