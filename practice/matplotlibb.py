import matplotlib.pyplot as plt
import numpy as np

a=np.array([0,23])
b=np.array([0,100])
plt.plot(a,b,marker='o')
#labels
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Basic line plot using Matplotlib")
plt.grid(True)
plt.show()
