import random
import sys
import math

def sa(modelClass):
    
    model = modelClass()
    
    # print "model", model.decs
    k = 1

    kmax = 50000.0

    emax = -1.0
    min1,max1=model.set_min_max()
    e = max1
    s = model.decs
    # print min1,max1
    # print s
    e = model.get_energy()
    # print e
    sb = s
    eb = e
    sn = s
    while k < kmax and  e > emax:
        # print "in while"
        mdl = neighbor(modelClass,min1,max1)
        sn = mdl.any()
        # print sn
        # print mdl.decs
        en = mdl.get_energy()
        if en < eb:
            # print sn
            sb = sn
            eb = en
            
        if en < e:
            s = sn
            e = en
            # say("+")
        elif P(e,en, k/kmax) < random.random():
            s = sn
            e = en
            # say("?")
            
        # say(".")
        k = k + 1    
    print "\n\nbest x: ",sb
    print "\n\nbest e (Normalized) :%s"%eb    
    
def say(x): 
  sys.stdout.write(str(x)); sys.stdout.flush()
  
def neighbor(model,mi,ma):
    # print model
    new_candidate = model(mi,ma)
    return new_candidate

def randValue():
    return random.random()
 
def P(old, new, t):
    
    jumpProb = math.exp(float((old-new)/float(t)))
    return jumpProb

