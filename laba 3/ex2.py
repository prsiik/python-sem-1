import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

# sky
rect(screen, (190, 190, 190), (0, 0, 600, 400))
rect(screen, (0, 0, 0), (0, 400, 600, 400))
# moon
circle(screen, (255, 255, 255), (500, 150), 70)
# clouds
ellipse(screen, (100, 100, 100), (350, 175, 400, 50))
ellipse(screen, (128, 128, 128), (300, 50, 200, 50))
ellipse(screen, (100, 100, 100), (100, 75, 300, 50))
# house
rect(screen, (0, 0, 0), (250, 95, 35, 55))
rect(screen, (128, 128, 0), (50, 200, 350, 500))
polygon(screen, (0, 0, 0), ((25, 200), (425, 200), (375, 150), (75, 150)))
rect(screen, (128, 128, 128), (25, 375, 400, 50))
rect(screen, (128, 0, 0), (75, 225, 300, 125))
rect(screen, (128, 0, 0), (75, 475, 80, 125))
rect(screen, (255, 255, 0), (275, 475, 80, 125))
rect(screen, (128, 0, 0), (175, 475, 80, 125))
rect(screen, (0, 0, 0), (150, 85, 20, 80))
rect(screen, (128, 128, 128), (30, 310, 390, 10))
for i in range(5):
    rect(screen, (128, 128, 128), (60 + 72 * i, 320, 40, 80))
# ghost
circle(screen, (211, 211, 211), (475, 650), 30)
circle(screen, (173, 216, 230), (463, 647), 7)
circle(screen, (0, 0, 0), (463, 647), 2)
circle(screen, (173, 216, 230), (482, 643), 7)
circle(screen, (0, 0, 0), (482, 643), 2)
polygon(screen, (211, 211, 211), ((475, 650), (450, 660), (445, 690), (460, 730), (440, 770),
                                  (480, 750), (500, 765), (525, 745), (540, 750),
                                  (560, 730), (540, 700), (520, 680), (505, 650)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
