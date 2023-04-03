from UFO import UFO
from time import time
import pygame
# from util import getAngle


class Laser(UFO):
  def __init__(self, img1, x_vel1, y_vel1, x_pos1, y_pos1):
    # print("LASER")
    self.expire = time() + 5
    self.pos = [x_pos1+25, y_pos1+25, 0]
    self.vel = [x_vel1, y_vel1, 0]
    self.img = img1

  def render(self, screen):
    # print("RENDER")
    x = self.pos[0]
    y = self.pos[1]
    screen.blit(pygame.transform.scale(self.img,((10,10))), (int(x), int(y)))
    
    
  def update(self, chargers_list, screen):
    if(time() > self.expire):
      chargers_list.remove(self)
      del self
      return 0
    for ship in chargers_list:
      if self.pos[0]-(r:=25) < ship.pos[0] < self.pos[0]+r and self.pos[1]-r < ship.pos[1] < self.pos[1]+r and ship.who()==0:
        ship.kill1(chargers_list)
        chargers_list.remove(self)
        # print("kileld")
        del self
        return 0
    #if no colision:
    # print("here")
    self.pos[0] += self.vel[0]
    self.pos[1] += self.vel[1]
    self.render(screen)

  def who(self):
    return 1

  def kill1(self, list):
    None