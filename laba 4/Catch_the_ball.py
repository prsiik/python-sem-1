import pygame
from pygame.draw import *
from random import randint
from random import choice
pygame.init()


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
AQUA = (0,255,255)
LIGHTBLUE = (191,239,255)
COLOURS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, AQUA, LIGHTBLUE]
lightpink = (255,182,193)
square_colour = (154,50,205)

FPS = 150
width=1200
height=600
g=0.09

Score = 0
balls = []
squares = []
screen = pygame.display.set_mode((width,height))


txt_x, txt_y = 300, 10
scr_font = pygame.font.SysFont('Arial Black', 22)
scr = scr_font.render("You scored: " + str(Score), 5, lightpink) # score
screen.blit(scr, (width - txt_x, txt_y)) # where to


def new_ball():
    '''
    This creates a new ball
    
    return None
    '''
    x = randint(100, width - 100)
    y = randint(100, height - 100)
    r = randint(10, 100)
    ball_colour = randint(0, 7)
    vx = choice([-2, -1, 1, 2])
    vy = choice([-2, -1, 1, 2])
    return(x, y, r, ball_colour, vx, vy)


def draw_ball(x, y, r, ball_colour):
    '''
    this draws a ball
    Parameters
    x, y : center of the ball
    r : radius
    ball_colour : parameter that defines the color
    return None
    '''
    circle(screen, COLOURS[ball_colour], (x, y), r)

    
def move_ball(x, y, r, vx, vy):
    '''
    this returns new coordinates of ball's center
    Parameters
    x, y : coordinates of the center
    r : radius
    vx : x-velocity
    vy : y-velocity
    return None
    '''
    if x + r > width:
        vx = 0 - vx
        x = width - r
    
    if x - r < 0:
        vx = 0 - vx
        x = r
        
    
    if y + r > height:
        vy = 0 - vy
        y = height - r
    
    if y - r < 0:
        vy = 0 - vy
        y = r

    x, y = x + vx, y + vy
    return(x, y, vx, vy)    


def ball_caught(x_m, y_m, x_bl, y_bl, r_bl):
    '''
    Checks if the ball's been caught
    Parameters
    ----------
    x_m, y_m : coordinates of mouse
    x_bl, y_bl : coordinates of the center of the ball
    r_bl : radius of the ball
    Return 
    -------
    caught : bool.
    '''
    R = ((x_bl - x_m) ** 2 + (y_bl - y_m) ** 2) ** (1/2)
    if(R <= r_bl):
        caught = True
    else:
        caught = False
    return caught

def new_square():
    '''
    Creates a new square
    Parameters
    a : length of a side of the square 
    xc, yc : coordinates of upper left corner
    vyc : y-velocity
    Returns
    -------
    None.
    '''
    a = randint(50, 70)
    xc = randint(100, width - 100)
    yc = -a
    vyc = 0
    print(xc, yc, a, vyc)
    return(xc, yc, a, vyc)
 
 
def draw_square(xc, yc, a):
    '''
    Draws the square
    Parameters
    ----------
    xc, yc : current coordinates of upper left corner
    a : length of a side.
    Returns
    -------
    None.
    '''
    rect(screen, square_colour, (xc, yc, a, a))

def move_square(h, v):
    '''
    Changes y coordinate of the square
    Parameters
    h : y coordinate
    v : y velocity
    '''
    v -= g
    h -= v
    return(h, v)


def square_caught(x_m, y_m, x_sq, y_sq, a_sq):
    '''
    Checks if the square has been caught
    Parameters
    ----------
    x_m, y_m : coordinates of mouse
    x_sq, y_sq : coordinates of the upper left corner
    a_sq : length of a side
    Return 
    -------
    caught : bool.
    '''
    if abs(x_m-x_sq) < a_sq and abs(y_m-y_sq) < a_sq:
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False

x, y, r, ball_colour, vx, vy = new_ball()
alive = 1
balls.append([x, y, r, ball_colour, vx, vy, alive])

xc, yc, a, vyc = new_square()
squares.append([xc, yc, a, vyc])
draw_square(xc, yc, a)

while not finished:
    clock.tick(FPS)
    for b in balls:
        b[0], b[1], b[4], b[5] = move_ball(b[0], b[1], b[2], b[4], b[5])
        draw_ball(b[0], b[1], b[2], b[3])
        
        
    for s in squares:
        s[1], s[3] = move_square(s[1], s[3])
        if(s[1] > height):
            squares.remove(s)
        else:
            draw_square(s[0], s[1], s[2])
            
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for b in balls:
                x_m, y_m = event.pos
                caught = ball_caught(x_m, y_m, b[0], b[1], b[2])
                if caught:
                    Score += 10
                    balls.remove(b)
                    break
            for s in squares:
                x_m, y_m = event.pos
                caught = square_caught(x_m, y_m, s[0], s[1], s[2])
                if caught:
                    Score += 30
                    squares.remove(s)
                    break
                
                
    scr = scr_font.render("Your score: " + str(Score), 5, lightpink) # score 
    screen.blit(scr, (width - txt_x, txt_y))
    
    
    if len(balls) < 10:
        x, y, r, ball_colour, vx, vy = new_ball()
        alive = 1
        balls.append([x, y, r, ball_colour, vx, vy, alive])
    
    if len(squares) < 5:
        xc, yc, a, vyc = new_square()
        squares.append([xc, yc, a, vyc])
        
    pygame.display.update()
    screen.fill(BLACK)

pygame.display.quit()
print(Score)
