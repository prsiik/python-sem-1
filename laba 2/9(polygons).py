import turtle                                         
import math                                           
t = turtle.Turtle()                                   
t.shape('turtle')                                     
R = 30                                                
x = 1                                                 
n = 3                                                 
t.up()                                                
t.goto(R, 0)                                          
t.down()                                              
def polygon(x):                                       
    while x <= n:                                     
        t.left((180 - 360 / n) / 2)                   
        t.left(360 / n)                               
        t.forward(2 * R * math.sin(math.pi/n))        
        x += 1                                        
        t.right((180 - 360 / n) / 2)                  
while n <= 11:                                        
    polygon(x)                                        
    n += 1                                            
    R += 18                                           
    t.up()                                            
    t.goto(R, 0)                                      
    t.down()  
