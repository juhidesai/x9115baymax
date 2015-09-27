# baseline for schafer
import random

def getRandomX1X2():
    return random.randint(0,10)
    
def getRandomX3X5():
    return random.randint(1,5)
    
def getRandomX4():
    return random.randint(0,6)
    
def getRandomX6():
    return random.randint(0,10)

def getRandomXValues(var = 7):
    x1 = getRandomX1X2()
    
    x2 = getRandomX1X2()
    
    x3 = getRandomX3X5()
    
    x4 = getRandomX4()
    
    x5 = getRandomX3X5()
    
    x6 = getRandomX6()

    randomList = [x1,x2,x3,x4,x5,x6]
    
    if var == 7:
        return randomList

    return randomList[var]
 
def osyczka2F1(x1,x2,x3,x4,x5):
    return (-1*(25*(x1-2)**2+(x2-2)**2+(x3-1)**2*(x4-4)**2 + (x5-1)**2))

def osyczka2F2(x1,x2,x3,x4,x5,x6):
    return (x1**2+x2**2+x3**2+x4**2+x5**2+x6**2)

def getSolution():
    varlist = []

    #print x
    varlist = getRandomXValues()
    
    n1 = -1
    while checkConstraints(varlist) == False:
        #if n1 == -1:
        n1 = random.randint(0,5)
        #print var_list[n1]
        #newlist = varlist[:n1-1]
        #newlist.append(getRandomXValues(n1))
        #newlist.append(varlist[n1+1:])
        newlist = getRandomXValues()
        varlist[n1] = newlist[n1]
        #varlist = newlist

        #var_list = getRandomXValues()
    #print varlist
    x1,x2,x3,x4,x5,x6 = varlist
    
    f1 = osyczka2F1(x1,x2,x3,x4,x5)
    f2 = osyczka2F2(x1,x2,x3,x4,x5,x6)
    return (f1+f2),varlist
    
def getScore(var):
    f1 = osyczka2F1(var[0],var[1],var[2],var[3],var[4])
    f2 = osyczka2F2(var[0],var[1],var[2],var[3],var[4],var[5])
    return f1 + f2
    
def checkConstraints(var_list):
    if (var_list[0] + var_list[1] - 2) < 0:
        return False
        
    if (6 - var_list[0] - var_list[1] < 0):
        return False
        
    if (2 - var_list[1] + var_list[0]) < 0:
        return False
        
    if (2 - var_list[0] + 3*var_list[1]) < 0:
        return False
        
    if (4 - (var_list[2] - 3)**2 - var_list[3]) < 0:
        return False
        
    if( (var_list[4] - 3)**3 + var_list[5] - 4) < 0:
        return False
        
    return True
        
    
def getBaselineEnergy():
    min1 = 10000000
    max1 = -10000
    minvalues = []
    maxvalues = []
    for i in range(100):
        energy,values = getSolution()
        #print min1," ",max1," ",energy
        if energy < min1 :
            min1 = energy
            minvalues = values
        if energy > max1:
            max1 = energy
            maxvalues = values
    print "Min is ",min1," Max is ",max1
    print "Min values ",minvalues
    print "Max values ",maxvalues
    return min1,max1
    

#getBaselineEnergy()

#min is 3202
#max is 19987601924