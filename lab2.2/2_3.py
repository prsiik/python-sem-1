import turtle as tr
tr.shape('turtle')


def draw_number_file(n):
    if n == '0':
        for line in zero:
            eval(line.rstrip())            
    if n == '1':
        for line in one:
            eval(line.rstrip())        
    if n == '4':
        for line in four:
            eval(line.rstrip())
    if n == '7':
        for line in seven:
            eval(line.rstrip())

with open('0.txt') as file:
    zero = file.readlines()
with open('1.txt') as file:
    one = file.readlines()    
with open('4.txt') as file:
    four = file.readlines()
with open('7.txt') as file:
    seven = file.readlines()   

nums = list('141700')
for x in nums:
    tr.pendown()    
    draw_number_file(x)
    
