import random

class Osyczka2:
    def __init__(self,mini=1000000,maxi=0):
        self.n=6
        self.dec_count = 6
        self.decs = [0 for i in xrange(self.n)]
        self.objs = [0 for i in xrange(2)]
        self.dec_names = ['x1','x2','x3','x4','x5','x6']
        self.obj_names = [self.f1,self.f2]
        self.minBound = [0,0,1,0,1,0]
        self.maxBound = [10,10,5,6,5,10]
        self.minimum,self.maximum = mini,maxi
        
    
    def f1(self):
        return (-1*(25*(self.decs[0]-2)**2+(self.decs[1]-2)**2+(self.decs[2]-1)**2*(self.decs[3]-4)**2 + (self.decs[4]-1)**2))
    
    def f2(self):
        return (self.decs[0]**2+self.decs[1]**2+self.decs[2]**2+self.decs[3]**2+self.decs[4]**2+self.decs[5]**2)

    def get_maximum_bound(self,number):
        return self.maxBound[number]
        
    def get_minimum_bound(self,number):
        return self.minBound[number]
    
    def get_decs(self,number=6):
        if number != 6:
            self.decs[number] = random.uniform(self.get_minimum_bound(number),self.get_maximum_bound(number))
            return self.decs
        
        for i in range(self.n):
            self.decs[i] = random.uniform(self.get_minimum_bound(i),self.get_maximum_bound(i))
        return self.decs
        
    def ok(self):
        if (self.decs[0] + self.decs[1] - 2) < 0:
            return False
            
        if (6 - self.decs[0] - self.decs[1] < 0):
            return False
            
        if (2 - self.decs[1] + self.decs[0]) < 0:
            return False
            
        if (2 - self.decs[0] + 3*self.decs[1]) < 0:
            return False
            
        if (4 - (self.decs[2] - 3)**2 - self.decs[3]) < 0:
            return False
            
        if( (self.decs[4] - 3)**3 + self.decs[5] - 4) < 0:
            return False
            
        return True
    
    def any(self,number=6):
        if number == self.dec_count:
            return self.get_decs()
            
        self.get_decs(number)
        patience = 15
        while not self.ok() and patience > 0:
            #do something to satisfy values
            # print "patience ",patience," ",self.ok() 
            c = random.randint(0,self.dec_count-1)
            self.get_decs(c)
            patience-=1
        if patience == 0:
            # give a new random solution
            self.get_decs()
        return self.decs
        
    def eval(self):
        res = 0
        for i in range(len(self.objs)):
            self.objs[i] = self.obj_names[i]()
            res += self.objs[i]
        return res
    
    def normalize(self,res):
        # print "Min ",self.minimum," max ",self.maximum
        # print res," ",((res - self.minimum) / (self.maximum - self.minimum))
        return (res - self.minimum) / (self.maximum - self.minimum)
        
    def set_min_max(self):
        mini = 1000000000
        maxi = -1
        
        for _ in range(1000):
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
        
    def get_energy(self):
        return self.normalize(self.eval())