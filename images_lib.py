import pygame
import os.path
def fill_library(list, folder, num = 360, size=1):
  for i in range(0,num,1):
    list+=[pygame.Surface.convert(pygame.image.load(os.path.join("assets\\"+folder,str(i)+".png")))]



  