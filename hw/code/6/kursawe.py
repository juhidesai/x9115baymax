'''
for model in [Schaffer, Osyczka2, Kursawe]:
  for optimizer in [sa, mws]:
     optimizer(model())
     
For the above loop to work, each model (e.g. Schaffer) has to be class that produces an instance via model(). That model defines:

the number of decisions;
the number of objectives;
the name of each decision/objective;
the min/max range of each decision/objective;
the any function that scores a candidate
the ok function that checks if a particular candidate is valid (for Schaffer and Kursawe, this returns True while for Osyczka2, this does some checking).
the eval function that computes the objective scores for each candidate
'''
import math
import random

class Kursawe:
    
    def __init__(self):
        
        self.n = 3
        
        self.decs = [0 for i in xrange(self.n)]
        self.objs = [0 for i in xrange(2)]
        self.dec_names = ['x1','x2','x3']
        self.obj_names = [self.f1,self.f2]
        
        self.minimum = 0
        self.maximum = 0
        
        self.a = 0.8
        self.b = 1
        
        self.bounds_min = -5
        self.bounds_max = 5
        
    def f1(self):
        res = 0
        
        for i in range(self.n-1):
            eqn = -10 * math.exp(-0.2*math.sqrt( (self.decs[i]*self.decs[i]) + (self.decs[i+1]*self.decs[i+1]) ))
            res+= eqn
            
        return res
        
    def f2(self):
        res = 0
        
        for i in range(self.n):
            eqn = math.fabs(self.decs[i])**self.a + 5*math.sin(self.decs[i]**self.b)
            res += eqn
        return res
        
    def check_bound(self):
        return True;
        
        
    def get_decs(self):
        for i in range(self.n):
            self.decs[i] = random.uniform(self.bounds_min,self.bounds_max)
        
    ## Score the candidate
    def any(self):
        self.get_decs()

    #check constraints
    def ok(self):
        return True
        
    #evals scores for all
    def eval(self):
        res = 0
        for i in range(len(self.objs)):
            self.objs[i] = self.obj_names[i]()
            res += self.objs[i]
        return res  
        
        
    def set_min_max(self):
        ## run model 100 times to get min and max values
        mini = 1000000000
        maxi = 0
        
        for _ in range(100):
            self.any()
            score = self.eval()
            
            if score < mini:
                mini = score
            if score > maxi:
                maxi = score
                
        return mini,maxi
       
       
k = Kursawe()

mini , maxi = k.set_min_max()

print("Min ",mini," Max ",maxi)

        
    
    
    
    
