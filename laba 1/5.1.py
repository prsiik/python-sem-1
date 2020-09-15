import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
v, p = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(v)
z= np.arange(0, 7, 0.01)
plt.plot(x,y)
plt.plot(z, p_f(z))
plt.grid(True)
plt.show()

