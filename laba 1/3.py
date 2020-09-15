import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
a=((x**2+1)*np.exp((-np.abs(x))/(10)))
c=np.log(a)
b=(np.log((1+np.tan(1/(1+(np.sin(x)**2))))))
k=c/b
plt.plot(x,k)
plt.show()


