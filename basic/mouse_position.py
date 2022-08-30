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

    mousePosition = pygame.mouse.get_pos()
    x, y = mousePosition
    #print(mousePosition)

    if x + hello_game_size[0] > 800:
        x = 800 - hello_game_size[0]

    if y + hello_game_size[1] > 600:
        y = 600 - hello_game_size[1]
    
    pygame.display.update()