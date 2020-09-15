import turtle as tr
tr.shape('turtle')
def stars(n):
	for i in range(1,n+1):
		tr.left(180-(180/n))
		tr.forward(200)
stars(11)
