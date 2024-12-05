import pygame

# initialize the pygame 
pygame.init()

# create the screen
screen=pygame.display.set_mode((800,600))


# Title and icon
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load("coolship.png")
pygame.display.set_icon(icon)

#PLAYER IMAGE 
playerimg=pygame.image.load("warship.png")
playerX=370
playerY=400


def player(x,y):
   screen.blit(playerimg,(x,y))
  


# Game loop
running=True
while running:
   #RGB
   screen.fill((0,0,0))
   for event in pygame.event.get():
         if event.type==pygame.QUIT:
            running=False

#INPUT CONTROL
         if event.type==pygame.KEYUP:
            if  event.type==pygame.K_RIGHT:
               print("left key is pressed")
            if event.type==pygame.K_RIGHT:
               print("right key is pressed")
             
         elif event.type==pygame.KEYDOWN:
            if event.type==pygame.K_RIGHT or event.type==pygame.K_RIGHT:
               print("key is released")
             
         player(playerX,playerY)
         pygame.display.update()
         
            
