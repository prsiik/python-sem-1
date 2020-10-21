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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, AQUA, LIGHTBLUE]
lightpink = (255,182,193)

FPS = 150
width=1200
height=600

Score = 0
balls = []
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
    ball_color = randint(0, 7)
    vx = choice([-2, -1, 1, 2])
    vy = choice([-2, -1, 1, 2])
    return(x, y, r, ball_color, vx, vy)

def draw_ball(x, y, r, ball_color):
    '''
    this draws a ball
    Parameters
    x, y : center of the ball
    r : radius
    ball_color : parameter that defines the color
    return None
    '''
    circle(screen, COLORS[ball_color], (x, y), r)
    
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

def ball_caught(x_mouse, y_mouse, x_ball, y_ball, r_ball):
    '''
    Checks if the ball's been caught
    Parameters
    ----------
    x_mouse, y_mouse : coordinates of mouse
    x_ball, y_ball : coordinates of the center of the ball
    r_ball : radius of the ball
    Return 
    -------
    caught : bool.
    '''
    R = ((x_ball - x_mouse) ** 2 + (y_ball - y_mouse) ** 2) ** (1/2)
    if(R <= r_ball):
        caught = True
    else:
        caught = False
    return caught




pygame.display.update()
clock = pygame.time.Clock()
finished = False

x, y, r, ball_color, vx, vy = new_ball()
alive = 1
balls.append([x, y, r, ball_color, vx, vy, alive])


while not finished:
    clock.tick(FPS)
    for b in balls:
        b[0], b[1], b[4], b[5] = move_ball(b[0], b[1], b[2], b[4], b[5])
        draw_ball(b[0], b[1], b[2], b[3])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for b in balls:
                x_mouse, y_mouse = event.pos
                caught = ball_caught(x_mouse, y_mouse, b[0], b[1], b[2])
                if caught:
                    Score += 10
                    balls.remove(b)
                    break
                
    scr = scr_font.render("Your score: " + str(Score), 5, lightpink) # score 
    screen.blit(scr, (width - txt_x, txt_y))

    for b in balls:
        if b[6] == 0:
            balls.remove(b)
            print('removed')
    
    if len(balls) < 10:
        x, y, r, ball_color, vx, vy = new_ball()
        alive = 1
        balls.append([x, y, r, ball_color, vx, vy, alive])
        
    
    pygame.display.update()
    screen.fill(BLACK)

pygame.display.quit()
print(Score)
