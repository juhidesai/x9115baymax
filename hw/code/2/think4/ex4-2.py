from swampy.TurtleWorld import *
import math

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
        
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    ''' A small direction correction to make the arc smoother.
        Reference: http://www.greenteapress.com/thinkpython/code/polygon.py
    '''
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def single(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def shape(n,r,angle):
    for i in range(n):
        single(t,r,angle)
        lt(t,360.0/n)

world=TurtleWorld()
t = Turtle()
# Call shape function with the desired number of petals 'n', radius 'r' and angle 'angle'
shape(7,r=60,angle=60)
#shape(10,r=60,angle=60) 
#shape(20,r=140,angle=20)

wait_for_user()
