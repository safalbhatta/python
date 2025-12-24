import matplotlib.pyplot as plt 
import numpy as np
#Data values for the pie chart
a=[20,30,25,15,10]
#labels for the pie chart
b=['kathmandu', 'pokhara', 'bhaktapur', 'lalitpur', 'biratnagar']
#create a pie chart
plt.pie(a,labels=b)
#Add legend to show the color and the name of the place
plt.legend()
#Title of the pie chart
plt.title("Pie chart using Matplotlib")
#show the pie chart
plt.show()