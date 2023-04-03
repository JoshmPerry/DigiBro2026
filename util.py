from math import atan, pi
def getAngle(x,y):
    if x > 0:
        return (atan(y/x)*180/pi+2*360)%360
    if x < 0:
        return ((atan(y/x)*180/pi+180)+2*360)%360
    else:
        if y >= 0:
            return 90
        else:
            return 270
