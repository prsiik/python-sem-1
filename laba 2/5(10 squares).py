import turtle as tr
tr.shape('turtle')

def drw_sq(n):
	for i in range (n):
		tr.penup()
		tr.goto(x=10*i,y=10*i)
		tr.pendown()
		tr.right(90)
		tr.forward(20*i)
		tr.right(90)
		tr.forward(20*i)
		tr.right(90)
		tr.forward(20*i)
		tr.right(90)
		tr.forward(20*i)
		
drw_sq(10)
