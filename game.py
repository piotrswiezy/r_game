import pygame

pygame.init()

SQUARE_SIZE = 25
SQUARES_NUM = 40
WIDTH = SQUARE_SIZE * SQUARES_NUM
screen = pygame.display.set_mode((WIDTH, WIDTH))
WHITE  = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (127, 127, 127)
screen.fill(GRAY)
pygame.display.update()
uruchom = True
while uruchom:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            uruchom = False
quit()
