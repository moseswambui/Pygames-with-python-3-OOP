import sys
import pygame

pygame.init() # INITIALIZE PYGAME MODULES AND DEPENDANCIES
pygame.mixer.init()

windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)

myImage =pygame.image.load('image.jpg')

imageSize = myImage.get_size()

sound = pygame.mixer.Sound('aud.mp3')

pygame.mouse.set_visible(0) # HIDE THE MOUSE-POINTER INSIDE SCREEN

x,y = 0,0 
DIRECTION_X, DIRECTION_Y = 1, 1
clock = pygame.time.Clock()
while 1:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 5

            if event.type == pygame.K_LEFT:
                x -= 5

            if event.key == pygame.K_DOWN:
                y += 5

            if event.type == pygame.K_UP:
                y -= 5

            

    screen.fill((0,0,0))
    screen.blit(myImage, (x,y))

 

    if x + imageSize[0] > 800:
        x = 800 - imageSize[0]
        sound.play()

    if y + imageSize[1] > 600:
        y = 600 - imageSize[1]
        sound.play()
    
    pygame.display.update()