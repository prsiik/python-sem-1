import turtle as tr
tr.shape('turtle')

def zero():
	tr.left(90)
	tr.forward(50)
	tr.left(90)
	tr.forward(25)
	tr.left(90)
	tr.forward(50)
	tr.left(90)
	tr.forward(25)
	tr.penup()
	tr.forward(40)
	tr.pendown()

def four():
	tr.penup()
	tr.forward(20)
	tr.pendown()
	tr.left(90)
	tr.forward(50)
	tr.penup()
	tr.backward(25)
	tr.pendown()
	tr.left(90)
	tr.forward(25)
	tr.right(90)
	tr.forward(25)
	tr.penup()
	tr.right(90)
	tr.forward(65)
	tr.right(90)
	tr.forward(50)
	tr.left(90)
	tr.pendown()

def seven():
	tr.left(90)
	tr.forward(25)
	tr.right(45)
	tr.forward(25*((2)**(0.5)))
	tr.left(135)
	tr.forward(25)
	tr.penup()
	tr.left(180)
	tr.forward(65)
	tr.right(90)
	tr.forward(50)
	tr.left(90)
	tr.pendown()

def one():
	tr.left(90)
	tr.forward(50)
	tr.left(135)
	tr.forward(25*(2**(0.5)))
	tr.penup()
	tr.left(135)
	tr.forward(40)
	tr.right(90)
	tr.forward(25)
	tr.left(90)
	tr.pendown()

def draw(x):
	for i in x:
		if i=='1':
			one()
		if i=='4':
			four()
		if i=='7':
			seven()
		if i=='0':
			zero()
x='141700'
draw(x)


