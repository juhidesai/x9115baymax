import nose
import sys
import logging
import coverage
import random
import os
import unittest 
import data_visualization

import coverage
cov=coverage.Coverage(config_file=True)
cov.start()


import test_all_trees
#import bintrees

cov=coverage.Coverage(config_file=True)
frontier = []
param_list = []
cov_list = []
cov_dict = {}
prev_cov_dict = {}
main_lists = []
run_data = []
n = 10
de_max = 50
f = 0.75
cf = 0.3
patience = 5
candidates = 200

def de():
    basefrontier = generateFrontier()
    for x in range(de_max):
        old  = basefrontier
        basefrontier = update(basefrontier)
        global patience,cov_dict,prev_cov_dict
        if patience == 0:
            print "*"*40
            print "Ran out of patience"
            print "*"*40
            break
    visualizeData()
    print "Final frontier is:"
    print basefrontier
    return basefrontier
    
def update(frnt):
    global patience
    generator(frnt)
    if cov_dict == prev_cov_dict:
        print "No change in coverage"
        patience -= 1
    for i,x in enumerate(frnt):
        newx = extrapolate(frnt,x,f,cf)
        frnt[i] = better(x,newx)
    return frnt

def extrapolate(frnt,one,f,cf):
    two,three,four = threeOthers(frnt,one)
    new = [[0]]*len(one)
    for i in range(len(one)):
        x,y,z = two[i],three[i],four[i]
        if random.random() < cf:
            new[i]=[0]*len(one[i])
            for j in range(int(f*len(one[i]))):
                r1 = random.randint(0,len(one[i])-1)
                r2 = random.randint(0,len(one[i])-1)
                r3 = random.randint(0,len(one[i])-1)
                new[i][r1] = x[random.randint(0,len(x)-1)]
                new[i][r2] = y[random.randint(0,len(y)-1)]
                new[i][r3] = z[random.randint(0,len(z)-1)]
        else:
            new[i] = one[i]
    return tuple(new)

def better(x,new):
    x_list = 0
    list_coverage = 0
    for i,some_list in enumerate(main_lists):
        if x in some_list:
            x_list = i
            break
    global cov_dict
    list_coverage = cov_dict[x_list]
    if list_coverage > 0.75:
        return x
    return new
        

def threeOthers(frnt,avoid):
    def oneOther():
        x = avoid
        while x in seen:
            x = a(frnt)
        seen.append(x)
        return x
    seen =[avoid]
    two = oneOther()
    three = oneOther()
    four = oneOther()
    return two,three,four

def a(lst):
    return lst[random.randint(0,candidates-1)]
    
        
def generateFrontier():
    frontier1 = []
    for i in range(candidates):         
        p1 = []
        p2 = []
        p3 = []
        for i in range(40):#random.randint(1,40)):
            p1.append(random.randint(1,99))
        for i in range(20):#random.randint(1,40)):
            p2.append((random.randint(1,99), random.randint(1,99)))   
        for i in range(15):#random.randint(1,40)):
            p3.append((random.randint(1,99), random.randint(1,99)))
            
        a = (list(zip(p1,p1)), p2, p3)
        frontier1.append(a)
    return frontier1
    
def test_de():
    de()
    
def generator(current_frontier):
    global cov_dict,prev_cov_dict,run_data
    mean = 0
    maj_cnt = 0
    prev_cov_dict = cov_dict.copy()
    main_lists = [current_frontier[i:i+n] for i in range(0,len(current_frontier),n)]
    
    for i,sub_list in enumerate(main_lists):
        cov.start()
        for params in sub_list:
            def_values1 = params[0]
            def_values2 = params[1]
            slicetest_data_global = params[2]
            test_all_trees.aaa(def_values1, def_values2, slicetest_data_global)
        cov.stop()
        cov.save()
        cov.html_report()
        filename = os.path.join(os.getcwd(),)
        analyzedData = analyzeCoverageData(cov)
        cov_list.append(analyzedData)
        cov_dict[i] = analyzedData
        if cov_dict[i] > 0.75:
            maj_cnt += 1
        mean+=cov_dict[i]
    run_data.append(cov_dict.values())      
    print "--"*20       
    print "Mean: ",float(mean)/(candidates/n)       
    print "Candidates with more than 75% coverage: ",maj_cnt     
    print "median: ",data_visualization.median(cov_dict.values())
        
def analyzeCoverageData(cov):
    dict = cov.analysis2("test_all_trees.py")
    totLines = dict[1]
    msdLines = dict[3]
    linesExe = len(totLines) - len(msdLines)
    linesExePc = (float)(linesExe)/ len(totLines)
    return linesExePc

def visualizeData():
    global run_data
    for run in run_data:
        data_visualization._tileX(run)

if __name__ == '__main__':
    global module_name
    module_name = sys.modules[__name__].__file__
    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-v', '--nocapture'])#,'--with-coverage','--cover-tests'])
    logging.info("all tests ok: %s", result)

