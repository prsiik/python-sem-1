import turtle as tr
tr.shape('turtle')

def sq_sprl(n):
	for i in range(n):
		tr.forward(i)
		tr.left(90)
sq_sprl(100)
