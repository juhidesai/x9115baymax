from swampy.TurtleWorld import *
import math
def triangle(t,length,angle):
    ag = (180 - angle) /2
    side = math.fabs(2*length*(math.sin(math.pi/n)))
    fd(t,length)
    lt(t,180-ag)
    fd(t,side)
    lt(t,180-ag)
    fd(t,length)
    lt(t,180)

def shapes(t,n,length):
    for i in range(n):
        triangle(t,length,360.0/n)
n = 7 #Change n to the number of sides of the figure (5,6,7)
world = TurtleWorld()
t = Turtle()
shapes(t,n,100)
wait_for_user()