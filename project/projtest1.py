'''
Dynamically generating and running and test cases.

Instructions to run this file:
1. install nose (pip install nose)
2. install coverage (pip install coverage)
3. using the commandmline, go to the location having this file and execute this line:
nosetests -v --with-coverage --cover-html --cover-erase  projtest1.py

Output:-
projtest1.test_generator(1, 1) ... ok
projtest1.test_generator(5, 3) ... ok
projtest1.test_generator(8, 6) ... ok

Name           Stmts   Miss  Cover   Missing
--------------------------------------------
projtest1.py      12      2    83%   14, 20
----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK
'''
import nose
import sys
import logging
import test_maincode
from test_maincode import *
import coverage
import random

cov=coverage.Coverage()

frontier = []
param_list = []
cov_list = []
cov_dict = {}
prev_cov_dict = {}
main_lists = []
n = 10
de_max = 50
f = 0.75
cf = 0.3
patience = 15
candidates = 200

def de():
    basefrontier = generateFrontier()
    print basefrontier
    for x in range(de_max):
        old  = basefrontier
        basefrontier = update(basefrontier)
##        if old == basefrontier:
##            print "same"
##            break;
        global patience,cov_dict,prev_cov_dict
        if patience == 0:
            print "*"*40
            print "Ran out of patience"
            print "*"*40
            print cov_dict
            break
    print basefrontier
    return basefrontier
    
def update(frnt):
##    print "in update"
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
    new = [0]*len(one)
    #TODO: use numpy
    for i in range(len(one)):
        x,y,z = two[i],three[i],four[i]
        if random.random() < cf:
            new[i] = int(x + f*(y - z))
##            print '%%'*50
##            print "changd"
##            print '%%'*50
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
##    print cov_dict
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
        a = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
            #get from some optimizer, DE? based on current value? get frontier with say 200 values         
        frontier1.append(a)
    return frontier1
    
    
def generateParam():
    for i in range(15):
        for j in range(2):
            a = (j,i)
            #get from some optimizer, DE? based on current value? get frontier with say 200 values         
            param_list.append(a)
            #from that frontier, get say 20 cadidates that dominate the rest and run nose on this newly pruned param_list
    global frontier
    frontier = param_list
##    print param_list


def test_de():
    print "in test DE"
    de()
    
##param_list = [(1, 1), (5,3), (8, 6)]
def generator(current_frontier):
##    print current_frontier
    print "inside"
    global cov_dict,prev_cov_dict
    prev_cov_dict = cov_dict
    main_lists = [current_frontier[i:i+n] for i in range(0,len(current_frontier),n)]
    
    for i,sub_list in enumerate(main_lists):
##        print i," ",sub_list
        cov.erase()
        cov.start()
        for params in sub_list:
##            check_em(params[0], params[1])
            check_em_too(params[0], params[1],params[2], params[3])
        cov.stop()
        dict = cov.analysis2('test_maincode.py')
##        print dict
        totLines = dict[1]
        msdLines = dict[3]
        linesExe = len(totLines) - len(msdLines)
        linesExePc = (float)(linesExe)/ len(totLines)
        cov_list.append(linesExePc)
        cov_dict[i] = linesExePc
    print "cov dict inside ",cov_dict
        
##de()    

if __name__ == '__main__':

    global module_name
    module_name = sys.modules[__name__].__file__
    print sys.modules[__name__]
    logging.debug("running nose for package: %s", module_name)
##    argv = ['fake','--nocapture']
    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-v', '--nocapture'])#,'--with-coverage','--cover-tests'])
    logging.info("all tests ok: %s", result)

