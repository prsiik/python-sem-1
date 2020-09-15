import turtle as tr
import numpy as np

tr.goto(0,0)
def sprl(n,k):
	for v in range(0,360/n):
		v_r=(v*np.pi)/180
		l=(k/2)*(v_r*((1+v_r)**(0.5))+np.log(v+(1+v_r)**(0.5)))
		tr.forward(l)
		tr.left(1)

sprl(15,0.03)
