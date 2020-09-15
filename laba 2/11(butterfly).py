import turtle as tr
tr.shape('turtle')
tr.left(90)
n=50
def butterfly(n):
		tr.circle(n)
		tr.circle(-n)
x=1
while x<=20:
	butterfly(n)
	n+=5
	x+=1
