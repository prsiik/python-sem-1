import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
x = np.arange(-10, 10.01, 0.01)
a=input()
eval("plt.plot(x,{})".format(a))
plt.show()
