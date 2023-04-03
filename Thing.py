class Thing(object):
  pos = [0, 0, 0] #x, y, rotation 
  img = 'imgFileFolder' #image folder for the thing
  siz = 10 #the scale of the image (not the hitbox)
  
  def __init__(self,init_pos=[0,0,0],init_image_folder='intro_ball',init_size=10):
    self.pos = init_pos #pos = [x,y,rotation]
    self.img = init_image_folder #folder to draw the rotation images from
    self.siz = init_size #the size/scale of the object


  def getImage(self): 
    #returns the file path to the specific image for the rotation
    return self.img + "\\" + str(int(self.pos[2]))+".png"
