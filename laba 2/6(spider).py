import turtle as tr
tr.shape('turtle')

def drw_ln(n):
	for i in range(n):
		tr.penup()
		tr.goto(x=0,y=0)
		tr.pendown()
		tr.right(360/n)
		tr.forward(100)
		tr.stamp()
drw_ln(12)
	

