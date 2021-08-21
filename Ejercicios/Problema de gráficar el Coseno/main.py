import matplotlib.pyplot as plt
import numpy as np


x = np.arrange(0, 10, 0.1)
y = x*np.cos(x**2)*1

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Plot")
plt.show()
