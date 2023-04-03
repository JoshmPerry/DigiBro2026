import pygame, sys
from pygame.locals import QUIT
from math import sin, cos
from util import getAngle


# from Thing import Thing
# from UFO import UFO
#depends on NOW_TIME being updated with the sytem time each loop cycle
#depends on second argument of player position function
from Charger import Charger
from Player import Player
from Laser import Laser
import images_lib

from time import time
# from math import sin, cos
XSIZE = 800
YSIZE = 600
DISPLAYSURF = pygame.display.set_mode((XSIZE, YSIZE))  # bro why so low res
screen = DISPLAYSURF
#create a library for every ship thing
#print("here1")
c_imgs = []
images_lib.fill_library(c_imgs, "Charger")  #name pls?
#print("here2")
#Player\0.png... etc... I love St. Mary's wifiP
p_imgs = []
images_lib.fill_library(p_imgs, "Player")

laser_img = pygame.Surface.convert(pygame.image.load("assets\\intro_ball.gif"))

bg = pygame.Surface.convert(pygame.image.load("assets\\space_background.jfif"))

NOW_TIME = time()

chargers = [
  Charger(c_imgs, [-8000, 0, 45]), 
  Charger(c_imgs, [-6000, 0, 450]), 
  Charger(c_imgs, [-4000, 0, 950]), 
  Charger(c_imgs, [-2000, 0, 5000]), 
  Charger(c_imgs, [-500, 0, 4500]), 
  Charger(c_imgs, [500, 0, -900]), 
  Charger(c_imgs, [1000, 0, -6000]), 
  Charger(c_imgs, [3000, 0, 450]), 
  Charger(c_imgs, [5000, 0, -3000]), 
  Charger(c_imgs, [6000, 0, 450]), 
  Charger(c_imgs, [8000, 0, 450]), 
  Charger(c_imgs, [1000, 0, 5])
  
  ]

rev = Player(p_imgs)

def endgame():
  i=1/0

pygame.init()
pygame.display.set_caption('Hello World!')
experation_date = time()
while True:
  if (time() > experation_date):
    # NOW_TIME = time()
    shoot = False
    for event in pygame.event.get():
      #code to deal with events goes here
      if event.type == pygame.MOUSEBUTTONDOWN:
        shoot = True
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    #code to do normal stuff goes here
    screen.blit(bg, (0, 0))
    rev.update(screen)
    if (shoot):
      x, y = pygame.mouse.get_pos()
      angle = getAngle(x,y)
      print(x,y,angle)
      x_vel = 2*rev.vel[0]#10 * cos(angle)
      y_vel = 2*rev.vel[1]#10 * sin(angle)
      print("PEW")
      chargers += [
        Laser(laser_img,x_vel, y_vel, (t := rev.getPosition())[0], t[1])
      ]
    for ship in chargers:
      # time, x_view, y_view, player_position, screen
      if(ship.who() == 0):
        ship.update(time(),2000 * XSIZE, 2000 * YSIZE, rev.getPosition(), screen)
        if ((s := ship.pos)[0] - 30) < (r := rev.getPosition(
        ))[0] < s[0] + 30 and s[1] - 30 < r[1] < s[1] + 30:
          print("ENDGAME")
          endgame()
      else:
        # print("UPDATE")
        ship.update(chargers,screen)

    # pygame.display.update()
    pygame.display.flip()
    experation_date = time() + 0.03  # seconds per frame
  else:
    pass
