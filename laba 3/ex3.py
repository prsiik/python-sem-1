import pygame
from pygame.draw import *


def house(canvas, x, y, size: {(0, 1)}):
    rect(canvas, (0, 0, 0), (x + 250*size, y + 95*size, 35*size, 55*size))
    rect(canvas, (128, 128, 0), (x + 50*size, y + 200*size, 350*size, 500*size))
    polygon(canvas, (0, 0, 0), ((x + 25*size, y + 200*size),
                                (x + 425*size, y + 200*size),
                                (x + 375*size, y + 150*size),
                                (x + 75*size, y + 150*size)))
    rect(canvas, (128, 128, 128), (x + 25*size, y + 375*size, 400*size, 50*size))
    rect(canvas, (128, 0, 0), (x + 75*size, y + 225*size, 300*size, 125*size))
    rect(canvas, (128, 0, 0), (x + 75*size, y + 475*size, 80*size, 125*size))
    rect(canvas, (255, 255, 0), (x + 275*size, y + 475*size, 80*size, 125*size))
    rect(canvas, (128, 0, 0), (x + 175*size, y + 475*size, 80*size, 125*size))
    rect(canvas, (0, 0, 0), (x + 150*size, y + 85*size, 20*size, 80*size))
    rect(canvas, (128, 128, 128), (x + 30*size, y + 310*size, 390*size, 10*size))
    for i in range(5):
        rect(canvas, (128, 128, 128), (x + 60*size + 72*size * i, y + 320*size, 40*size, 80*size))
    return


def ghost(canvas, x, y, size: {(0, 1)}):
    circle(canvas, (211, 211, 211), (x + 75*size, y + 50*size), 30*size)
    circle(canvas, (173, 216, 230), (x + 63*size, y + 47*size), 7*size)
    circle(canvas, (0, 0, 0), (x + 63*size, y + 47*size), 2*size)
    circle(canvas, (173, 216, 230), (x + 82*size, y + 43*size), 7*size)
    circle(canvas, (0, 0, 0), (x + 82*size, y + 43*size), 2*size)
    polygon(canvas, (211, 211, 211), ((x + 75*size, y + 50*size), (x + 50*size, y + 60*size),
                                      (x + 45*size, y + 90*size), (x + 60*size, y + 130*size),
                                      (x + 40*size, y + 170*size), (x + 80*size, y + 150*size),
                                      (x + 100*size, y + 165*size), (x + 125*size, y + 145*size),
                                      (x + 140*size, y + 150*size), (x + 160*size, y + 130*size),
                                      (x + 140*size, y + 100*size), (x + 120*size, y + 80*size),
                                      (x + 105*size, y + 50*size)))
    return


def reverse_ghost(canvas, x, y, size):
    circle(canvas, (211, 211, 211), (x - 75*size, y + 50*size), 30*size)
    circle(canvas, (173, 216, 230), (x - 63*size, y + 47*size), 7*size)
    circle(canvas, (0, 0, 0), (x - 63*size, y + 47*size), 2*size)
    circle(canvas, (173, 216, 230), (x - 82*size, y + 43*size), 7*size)
    circle(canvas, (0, 0, 0), (x - 82*size, y + 43*size), 2*size)
    polygon(canvas, (211, 211, 211), ((x - 75*size, y + 50*size), (x - 50*size, y + 60*size),
                                      (x - 45*size, y + 90*size), (x - 60*size, y + 130*size),
                                      (x - 40*size, y + 170*size), (x - 80*size, y + 150*size),
                                      (x - 100*size, y + 165*size), (x - 125*size, y + 145*size),
                                      (x - 140*size, y + 150*size), (x - 160*size, y + 130*size),
                                      (x - 140*size, y + 100*size), (x - 120*size, y + 80*size),
                                      (x - 105*size, y + 50*size)))
    return


pygame.init()

FPS = 30
screen = pygame.display.set_mode((720, 1080))
# sky 
rect(screen, (190, 190, 190), (0, 0, 720, 540))
rect(screen, (0, 0, 0), (0, 540, 720, 540))
# moon
circle(screen, (255, 255, 255), (600, 150), 70)
# clouds
ellipse(screen, (100, 100, 100), (250, 175, 500, 100))
ellipse(screen, (128, 128, 128), (100, 220, 600, 75))
ellipse(screen, (140, 140, 140), (500, 100, 600, 75))
house(screen, 250, 520, 0.4)

# fog
surf_5 = pygame.Surface((600, 150))
surf_5.set_colorkey((0, 0, 0))
surf_5.set_alpha(200)
ellipse(surf_5, (105, 105, 105), (0, 0, 600, 100))
screen.blit(surf_5, (50, 700))

house(screen, 500, 275, 0.5)

surf_0 = pygame.Surface((400, 600))
surf_0.set_colorkey((0, 0, 0))
surf_0.set_alpha(255)
house(surf_0, 0, 0, 0.6)
screen.blit(surf_0, (0, 600))

surf_6 = pygame.Surface((600, 150))
surf_6.set_colorkey((0, 0, 0))
surf_6.set_alpha(200)
ellipse(surf_6, (105, 105, 105), (0, 0, 600, 100))
screen.blit(surf_6, (300, 550))

surf_1 = pygame.Surface((200, 200))
surf_1.set_colorkey((0, 0, 0))
surf_1.set_alpha(100)
ghost(surf_1, 0, 0, 1)
screen.blit(surf_1, (500, 600))

surf_2 = pygame.Surface((200, 200))
surf_2.set_colorkey((0, 0, 0))
surf_2.set_alpha(200)
ghost(surf_2, 0, 0, 1)
screen.blit(surf_2, (450, 650))

surf_3 = pygame.Surface((300, 300))
surf_3.set_colorkey((0, 0, 0))
surf_3.set_alpha(100)
reverse_ghost(surf_3, 200, 0, 1)
screen.blit(surf_3, (150, 900))

surf_4 = pygame.Surface((400, 400))
surf_4.set_colorkey((0, 0, 0))
surf_4.set_alpha(200)
reverse_ghost(surf_4, 400, 0, 2)
screen.blit(surf_4, (200, 800))

surf_7 = pygame.Surface((600, 150))
surf_7.set_colorkey((0, 0, 0))
surf_7.set_alpha(150)
ellipse(surf_7, (90, 90, 90), (0, 0, 500, 75))
screen.blit(surf_7, (200, 330))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
