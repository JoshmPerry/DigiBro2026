from UFO import UFO
import pygame
from math import sin, cos, pi, sqrt
from util import getAngle


class Player(UFO):

  def __init__(self, img_lib1, position=[10, 10, 0]):
    self.pos = position
    self.img_library = img_lib1
    self.velocity = [0,0]
    
  
  def update_pos(self, angular_speed = 10):
    #face the mouse
    self.pos[2] = getAngle((c:=((pygame.mouse.get_pos()))[0]-self.pos[0]), (b:=((pygame.mouse.get_pos())[1]) - self.pos[1]) )
    speed = sqrt(b**2 + c**2) / 100
    #set the velocities x and y using speed and angle
    self.vel[0] = speed * cos(self.pos[2] * 2*pi/360)
    self.vel[1] = speed * sin(self.pos[2] * 2*pi/360)
    #move in that direction
    self.pos[0] += self.vel[0]
    self.pos[1] += self.vel[1]

  
  def render(self, screen):
    rotation = self.pos[2]
    x = self.pos[0]
    y = self.pos[1] 
    correct_image = self.img_library[(((-90-int(rotation)))+2*360)%360]
    # print(screen)
    screen.blit(correct_image, (int(x), int(y)))
    return 0

  #This is the function that will be called from the outside
  def update(self, screen):
    '''time, x_view, y_view, player_position, screen'''
    self.update_pos()
    self.render(screen)

  #for use by other things
  def getPosition(self):
    return self.pos  #I see you've made a lot of progress in 2 hours

    