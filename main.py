import pygame
#initialize the pygame 
pygame.init()
#create the screen
screen=pygame.display.set_mode((800,600))
#Title and icon
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load("coolship.png")
pygame.display.set_icon(icon)
#game loop

running=True
while running:
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
            running=False
         screen.fill((255,10,190))
         pygame.display.update()
            
