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
    
    def __init__(self,mini=1000000,maxi=0):
        
        self.n = 3
        self.dec_count = 3;
        
        self.decs = [0 for i in xrange(self.n)]
        self.objs = [0 for i in xrange(2)]
        self.dec_names = ['x1','x2','x3']
        self.obj_names = [self.f1,self.f2]
        
        
        
        self.a = 0.8
        self.b = 1
        
        self.bounds_min = -5
        self.bounds_max = 5
        
        self.minimum, self.maximum = mini,maxi
        # self.minimum, self.maximum = self.set_min_max()
        
    def f1(self):
        res = 0
        # print self.decs
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
        
        
    def get_decs(self,number = 2):
        if number != 2:
            self.decs[number] = random.uniform(self.bounds_min,self.bounds_max)
            return self.decs
        
        for i in range(self.n):
            self.decs[i] = random.uniform(self.bounds_min,self.bounds_max)
        return self.decs
        
    ## Score the candidate
    def any(self,number = 2):
        if number == self.dec_count:
            return self.get_decs()
        
        self.get_decs(number)
        patience = 15
        while not self.ok() and patience > 0:
            # print "patience ",patience," ",self.ok() 
            c = random.randint(0,self.dec_count-1)
            self.get_decs(c)
            patience-=1
        if patience == 0:
            # give a new random solution
            self.get_decs()
        return self.decs
        

    #check constraints
    def ok(self):
        return True
        
    def normalize(self,res):
        # print "Min ",self.minimum," max ",self.maximum
        # print res," ",((res - self.minimum) / (self.maximum - self.minimum))
        return (res - self.minimum) / (self.maximum - self.minimum)
    
    #evals scores for all
    def eval(self):
        res = 0
        for i in range(len(self.objs)):
            self.objs[i] = self.obj_names[i]()
            res += self.objs[i]
        return res
        
    def get_energy(self):
        return self.normalize(self.eval())
        
    def get_maximum_bound(self,number):
        return self.bounds_max
        
    def get_minimum_bound(self,number):
        return self.bounds_min
        
    def set_min_max(self):
        ## run model 100 times to get min and max values
        mini = 1000000000
        maxi = -1
        
        for _ in range(100):
            self.any()
            score = self.eval()
            
            if score < mini:
                mini = score
            if score > maxi:
                maxi = score
                
        self.minimum = mini
        self.maximum = maxi
        # print "Min ",self.minimum," max ",self.maximum
        return mini,maxi
    
    
    
