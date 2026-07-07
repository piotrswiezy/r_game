import pygame, os
from position import Position

os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h

print(f"Screen size: {screen_width} x {screen_height}")


SQUARE_SIZE = 20
SQUARES_NUM = 40
WIDTH = SQUARE_SIZE * SQUARES_NUM
screen = pygame.display.set_mode((800, 600))
WHITE  = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (127, 127, 127)
print(f"My screen size: {screen_width / SQUARE_SIZE} x {screen_height / SQUARE_SIZE}")

def draw_food(pos):
    food_color = RED
    radius = float(SQUARE_SIZE) / 2
    position = (pos.x * SQUARE_SIZE + radius,
                pos.y * SQUARE_SIZE + radius)
    pygame.draw.circle(screen, food_color, position,radius)
    pygame.display.update()


def fill_screen(color = GRAY):
    screen.fill(color)
    pygame.display.update()
fill_screen()

run = True
fullscreen = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Toggle fullscreen when F11 is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.SCALED)
                    fill_screen()
                    draw_food(Position(1, 2))
                else:
                    screen = pygame.display.set_mode((800, 600))
                    fill_screen()
                    draw_food(Position(1, 2))

quit()
