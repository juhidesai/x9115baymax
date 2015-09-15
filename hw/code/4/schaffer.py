# baseline for schafer
import random

min = 10000000
max = 0

def getRandomX():
    return random.randint(-100000, 100000)
 
def schaferF1(x):
    return x*x
    
def schaferF2(x):
    return (x-2)*(x-2)

def getMinMax():
    x = getRandomX()
    #print x
    f1 = schaferF1(x)
    f2 = schaferF2(x)
    return f1+f2
    
for i in range(100):
    energy = getMinMax()
    if energy < min :
        min = energy
    if energy > max:
        max = energy
print "Min is ",min," Max is ",max

#min is 3202
#max is 19987601924