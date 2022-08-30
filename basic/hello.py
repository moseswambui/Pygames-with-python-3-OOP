import sys
import pygame

pygame.init()

windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)
myriadProFont = pygame.font.SysFont('Myriad Pro', 48)
hello_game = myriadProFont.render('Hello Game', 1, (255,0,255), (255,255,255))

hello_game_size = hello_game.get_size()

x,y = 0,0 
DIRECTION_X, DIRECTION_Y = 1, 1
clock = pygame.time.Clock()
while 1:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0,0,0))
    screen.blit(hello_game, (x,y))
    x += 7 * DIRECTION_X
    y += 7 * DIRECTION_Y

    if x + hello_game_size [0] > 800 or x <= 0:
        DIRECTION_X *= -1

    if y + hello_game_size [1] > 600 or y <= 0:
        DIRECTION_Y *= -1
    
    pygame.display.update()