import turtle as tr
tr.shape('turtle')


def flower(n):
	for i in range(1,n+1,1):
		tr.circle(50)
		tr.left(360/n)
flower(6)
