from UFO import UFO
from math import sin, cos, pi
from util import getAngle

class Charger(UFO):

  def __init__(self,
               input_img_library,
               input_start_pos=[200,200,135],
               start_time1=0,
               init_charge_speed=2,
               init_normal_speed=1,
               init_attack_delay=4,
               init_attack_time=1,
              master_list = []):
    self.img_library = input_img_library
    self.charge_speed = init_charge_speed
    self.normal_speed = init_normal_speed
    self.attack_delay = init_attack_delay
    self.attack_time = init_attack_time
    self.attack_time = start_time1 + self.attack_delay
    self.pos = input_start_pos
    self.master_list = master_list
    # self.vel = self.vel
    # return self

  # this is updated by a function,
  # the position where the charger thinks the player is
  player_pos = [100, 100, 100]
  
  normal_angular_speed = 2
  charging_angular_speed = 0
  #some constant number of seconds
  attack_delay = 5
  #time to charge for
  charge_duration = 2
  #time of next shot, set to time+attack_delay each attack

  def getPlayerPos(self):
    return self.player_pos
  def setPlayerPos(self, input_pos_list):
    self.player_pos = input_pos_list
  
  def update_pos(self, speed, target_angle, angular_speed):
    if ((target_angle - self.pos[2] + 2 * 360) % 360 >
        (self.pos[2] - target_angle + 2 * 360) % 360):
      self.pos[2] += angular_speed
    else:
      self.pos[2] -= angular_speed
    self.vel[0] = speed * cos(self.pos[2] * 2*pi/360)
    self.vel[1] = speed * sin(self.pos[2] * 2*pi/360)
    self.pos[0] -= self.vel[0]
    self.pos[1] -= self.vel[1]

  #move each frame
  def move(self, now_time, detection_x, detection_y):
    player_pos = self.getPlayerPos()
    if (abs(player_pos[0] - self.pos[0]) > detection_x
        or abs(player_pos[1] - self.pos[1]) > detection_y):
      return 0
    target_angle = getAngle((player_pos[0] - self.pos[0]), (player_pos[1] - self.pos[1]))
    #if currently charging
    if (now_time < self.attack_time -
        (self.attack_delay - self.charge_duration)):
      self.update_pos(self.normal_speed, target_angle,
                      self.normal_angular_speed)
    #if not charging but it is time to charge
    elif (self.attack_time - 0.1 < now_time < self.attack_time + 0.1):
      self.attack_time = now_time + self.attack_delay
      self.update_pos(self.charge_speed, target_angle,
                      self.charging_angular_speed)
    #if just normally moving
    else:
      self.update_pos(self.normal_speed, target_angle, self.normal_angular_speed)

  def render(self, screen):
    rotation = self.pos[2]
    x = self.pos[0]
    y = self.pos[1]
    #print(int(x), int(y), int(rotation))#Naw, even for debugging, you should just add a toString def nice try sir. fast make code go zoom bbbbrrrrrrrrrrrrrrrrrrrrrrrrrrr. but thank you for the suggestion. :) 
    correct_image = self.img_library[(((-90-rotation+180))+2*360)%360]
    # print(screen)
    screen.blit(correct_image, (int(x), int(y)))
    return 0

    #This is the function that will be called from the outside
  def update(self, time, x_view, y_view, player_position, screen):
    '''time, x_view, y_view, player_position, screen'''
    self.setPlayerPos(player_position)
    self.move(time, x_view, y_view)
    self.render(screen)

  def kill1(self, master_list):
    master_list.remove(self)
    del self

  def who(self):
    return 0