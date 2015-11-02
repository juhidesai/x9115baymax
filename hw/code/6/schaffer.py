# baseline for schafer
import random
import math

min = 10000000
max = 0


class Schaffer:
    
    def __init__(self,mini=1000000,maxi=0):
        self.n = 1
        self.dec_count = 1
        
        self.decs = [0 for i in xrange(self.n)]
        self.objs = [0 for i in xrange(2)]
        self.dec_names = ['x1']
        self.obj_names = [self.f1,self.f2]
        self.bounds_min = -100000
        self.bounds_max = 100000
        
        self.minimum, self.maximum = mini,maxi
        # self.minimum, self.maximum = self.set_min_max()
        
    def get_decs(self,number=1):
        self.decs[0] = random.randint(self.bounds_min,self.bounds_max)
        return self.decs
    
    def any(self,number=1):
        return self.get_decs(number)
    
    def ok(self):
        return True
    
    def eval(self):
        res = 0
        for i in range(len(self.objs)):
            self.objs[i] = self.obj_names[i]()
            res += self.objs[i]
        # print "decs ",self.decs
        # print res
        return res
 
    def f1(self):
        return float(self.decs[0]*self.decs[0])
        
    def f2(self):
        return float((self.decs[0]-2)*(self.decs[0]-2))

    # def getMinMax(self):
    #     x = self.getRandomX()
    #     #print x
    #     f1 = self.f1()
    #     f2 = self.f2()
    #     return f1+f2
    
    def set_min_max(self):
        mini = 1000000000
        maxi = -1
        for i in range(10000):
            self.any()
            energy = self.eval()
            if energy < mini :
                mini = energy
            if energy > maxi:
                maxi = energy
        self.minimum = mini
        self.maximum = maxi
        # print "Min is ",mini," Max is ",maxi
        return mini,maxi
    
    def get_energy(self):
        return (self.normalize(self.eval()))
        
    def get_maximum_bound(self,number):
        return self.bounds_max
        
    def get_minimum_bound(self,number):
        return self.bounds_min
    
    def normalize(self,res):
        return float(res - float(self.minimum)) / float(self.maximum - self.minimum)
#min is 3202
#max is 19987601924
# s=Schaffer()