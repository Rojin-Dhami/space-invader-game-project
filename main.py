import pygame
import random

# initialize the pygame 
pygame.init()

# create the screen
screen=pygame.display.set_mode((800,600))


# Title and icon
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load("coolship.png")
pygame.display.set_icon(icon)


#BACKGROUND
background=pygame.image.load("back.png")

#PLAYER IMAGE 
playerimg=pygame.image.load("warship.png")
playerX=370
playerY=400
playerX_change=0


def player(x,y):
   screen.blit(playerimg,(x,y))
  

#Enemy IMAGE 
enemyimg=pygame.image.load("space invaders.png")
enemyX=random.randint(0,800)
enemyY=random.randint(0,600)
enemyX_change=0.25
enemyY_change=20

def enemy(x,y):
   screen.blit(enemyimg,(x,y))


# Game loop
running=True
while running:
   #RGB
   screen.fill((0,0,0))
   screen.blit(background,(0,0))
   #EVENT LOOP
   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         running=False

#INPUT CONTROL
      if event.type==pygame.KEYDOWN:
      
         if  event.key==pygame.K_RIGHT:
            playerX_change=0.25
         if event.key==pygame.K_LEFT:
            playerX_change=-0.25
               
             
      if event.type==pygame.KEYUP:
            
         if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
            playerX_change=0
   
   #UPDATE PLAYER POSITION           
   playerX+=playerX_change

   #BOUNDARY CHECK
   if playerX<=0:
      playerX=0
   elif playerX>=736:
      playerX=736

  #ENEMY MOVEMENT CONTROL
   enemyX+=enemyX_change
   if enemyX<=0:
      enemyX_change=0.25
      enemyY+=enemyY_change
   elif enemyX>=736:
      enemyX_change=-0.25
      enemyY+=enemyY_change


   #DRAWS PLAYER
   player(playerX,playerY)

   #DRAWS enemy
   enemy(enemyX,enemyY)

   #UPDATE DISPLAYY
   pygame.display.update()
         
            
