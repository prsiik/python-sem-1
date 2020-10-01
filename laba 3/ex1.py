import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (125, 150), 40)
circle(screen, (255, 0, 0), (275, 150), 30)
circle(screen, (0, 0, 0), (125, 150), 15)
circle(screen, (0, 0, 0), (275, 150), 15)
rect(screen, (0, 0, 0), (120, 275, 150, 40))
line(screen, (0, 0, 0), (50, 50), (175, 150), 20)
line(screen, (0, 0, 0), (350, 50), (225, 150), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
