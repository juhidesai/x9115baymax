import random
import sys
import math

min1 = 3202.0
max1 = 19987601924.0
s = 77
e = 19987601924 + 10000000
sb = s
eb = e
k = 0

kmax = 1000.0

emax = -2.0

def say(x): 
  sys.stdout.write(str(x)); sys.stdout.flush()
  
def neighbor(n):
    return random.randint(-100000,100000)
    if n*2 > 100000 or n*2 < -100000:
        return n/2
    return n*2

def schaferF1(x):
    return x*x
    
def schaferF2(x):
    return (x-2)*(x-2)

def E(x):
    f1=schaferF1(x)
    f2= schaferF2(x)
    #print "x, F ",x,f1,f2
    #print (((f1 + f2) - min1) / (max1 - min1))
    return ((f1 + f2) - min1) / (max1 - min1)

def randValue():
    return random.random()
 
def P(old, new, t):
    #print "P ",e**(-1*(old-new)/t)
    #return math.exp(float(1*float(old-new)/t))
    ''' Credit to: Akond - https://github.com/akondrahman/59115ASE/blob/master/hw/code/4/randomGeneration.py
    '''
    equation = float(1*(old-new)/float(t))
    accepProbToret = math.exp(equation)
    return accepProbToret
    
while k < kmax and  e > emax:
    sn = neighbor(s)
    en = E(sn)
    if k%25 == 0:
        
        say("\n")
        # say(sb)
        say(", ")
        print "%04d"%k,
        say(", ")
        print "%.2f"%en,
        say(", ")
    #print "\n",sn,"\t",s,"\t",eb
    #print "\n Energy: ",en,"\t",e,"\t",eb
    if en < eb:
        sb = sn
        eb = en
        say("!")
        
    if en < e:
        s = sn
        e = en
        say("+")
    elif P(e,en, k/kmax) > (k+100)/kmax:
        s = sn
        e = en
        say("?")
        
    say(".")
    k = k + 1
    
    #break
    
print "\n\nbest x: ",sb
print "\n\nbest e (Normalized) :%s"%eb
