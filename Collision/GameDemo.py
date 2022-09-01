import pygame,sys
from GameObject import GameObject

pygame.init()
pygame.mixer.init()

windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(0)

myImage = pygame.image.load('image.jpg')
sound = pygame.mixer.Sound('music.m4a')

myriadProFont = pygame.font.SysFont('Myriad Pro', 48)
intersectText = myriadProFont.render('Intersecting', 1, (255,0,255), (0,0,0))

imgSize = myImage.get_size()
myImage.fill((0,0,0), None, pygame.BLEND_RGB_MAX)

x,y = 0,0 
clock = pygame.time.Clock()
DIRECTION_X, DIRECTION_Y = 1, 1

def playSound():
    sound.stop()
    sound.play()

rectangle = GameObject(100, 100, 400, 400)
logo = GameObject(0,0 imgSize[0], imgSize[1])
    
