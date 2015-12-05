import nose
import sys
import logging
import random
import os
import unittest

import coverage
cov=coverage.Coverage(config_file=True)
cov.start()


import test_all_trees
import bintrees
from bintrees import BinaryTree, AVLTree, RBTree

frontier = []
param_list = []
cov_list = []
cov_dict = {}
prev_cov_dict = {}
main_lists = []
n = 10
de_max = 50
f = 0.75
cf = 0.30
patience = 5
candidates = 200

def de():
    basefrontier = generateFrontier()
    # print basefrontier
    for x in range(de_max):
        old  = basefrontier
        basefrontier = update(basefrontier)
##        if old == basefrontier:
##            print "%"*40
##            print "No Change"
##            print old[0]
##            print "base"
##            print basefrontier[0]
##            return
        global patience,cov_dict,prev_cov_dict
        if patience == 0:
            print "*"*40
            print "Ran out of patience"
            print "*"*40
            print cov_dict
            break
    # print basefrontier
    return basefrontier
    
def update(frnt):
    print "in update"
##    print frnt[0]
    global patience
    generator(frnt)
    if cov_dict == prev_cov_dict:
        print "No change in coverage"
        patience -= 1
##    print len(frnt)
    for i,x in enumerate(frnt):
        newx = extrapolate(frnt,x,f,cf)
        frnt[i] = better(x,newx)
##        print len(frnt)
    
    return frnt

def extrapolate(frnt,one,f,cf):
    if len(frnt)==3:
        print "Gotcha"
        print frnt
    two,three,four = threeOthers(frnt,one)
    new = [[0]]*len(one)
    # print "//"*40
    # print len(one)
    #TODO: use numpy
    for i in range(len(one)):
        x,y,z = two[i],three[i],four[i]
        # print "&&"*40
        # print one
        # print x
        # print y
        # print z
        #print int(f*len(one[i]))
        if random.random() < cf:
            ## these are lists. Do a change in the list
            # try:
            # print "$"*45
            # print(len(new))
            new[i]=[0]*len(one[i])
            new[i] = one[i]
            for j in range(int(f*len(one[i]))):
                r1 = random.randint(0,len(one[i])-1)
                r2 = random.randint(0,len(one[i])-1)
                r3 = random.randint(0,len(one[i])-1)
                # print r1," ",r2," ",r3 
                new[i][r1] = x[random.randint(0,len(x)-1)]
                new[i][r2] = y[random.randint(0,len(y)-1)]
                new[i][r3] = z[random.randint(0,len(z)-1)]
                    # print new
            #new[i] = int(x + f*(y - z))
            # except:
            #     1==1
                # print len(new), len(one)
##            print "New ",new
##            print "One ",one
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
    #####print cov_dict
    list_coverage = cov_dict[x_list]
##    print "()"*20
    if list_coverage > 0.75:
        return x
##    print "returning new"
    return new
        

def threeOthers(frnt,avoid):
    def oneOther():
        x = avoid
        while x in seen:
            x = a(frnt)
        seen.append(x)
        return x
    # print "+"*40
    # print frnt
    seen =[avoid]
    two = oneOther()
    three = oneOther()
    four = oneOther()
    return two,three,four

def a(lst):
##    print "+"*40
##    print len(lst)
##    print candidates
    return lst[random.randint(0,candidates-1)]
    
        
def generateFrontier():
    frontier1 = []
    for i in range(candidates):
        #a = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
            #get from some optimizer, DE? based on current value? get frontier with say 200 values         
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
        # print frontier1
    return frontier1
    
def test_de():
    print "in test DE"
    de()
    
##param_list = [(1, 1), (5,3), (8, 6)]
def generator(current_frontier):
##    print current_frontier
    print "inside"
    mean = 0
    global cov_dict,prev_cov_dict
    prev_cov_dict = cov_dict
    main_lists = [current_frontier[i:i+n] for i in range(0,len(current_frontier),n)]
    
    for i,sub_list in enumerate(main_lists):
##        print i," ",sub_list
##        cov.erase()
        cov.start()
        for params in sub_list:
##            check_em(params[0], params[1])
            # os.system("test_all_trees.py")
            
            
            def_values1 = params[0]#list(zip([13, 13, 13], [13, 13, 13]))
            def_values2 = params[1]#[(3, 12), (9, 35), (8, 95), (1, 16), (3, 57)]
            slicetest_data_global = params[2]#[(1, 1), (2, 2), (3, 3), (4, 4), (8, 8), (9, 9), (10, 10), (11, 11)]

            #test_all_trees.aaa()
            test_all_trees.aaa(def_values1, def_values2, slicetest_data_global)
##            test_001_init(def_values1)
            # result = nose.run(argv=[
            #                 'test_all_trees.py',
            #                 '-v', '--nocapture'])
            #CheckTree().check_em_too(params[0], params[1],params[2], params[3])
##            return
        cov.stop()
        cov.save()
        cov.html_report()
#         dict = cov.analysis2('test_all_trees.py')
# ##        print dict
#         totLines = dict[1]
#         msdLines = dict[3]
#         linesExe = len(totLines) - len(msdLines)
#         linesExePc = (float)(linesExe)/ len(totLines)
#         cov_list.append(linesExePc)
#         cov_dict[i] = linesExePc
        
        # ../bintrees/bintree.py, test_all_trees.py
        filename = os.path.join(os.getcwd(),)
        # print "^^"*40
        # print os.path.abspath('../bintrees/bintree.py')
        #/home/ubuntu/workspace/project/bintrees-2.0.2/bintrees/bintree.py
        #os.path.join(os.path.abspath('../'),'/bintrees/bintree.py')
        analyzedData = analyzeCoverageData(cov,"C:\Users\Juhi\Desktop\notes\sem 3\ASE\git repo\x9115baymax\project\bintrees-2.0.2\bintrees")
        cov_list.append(analyzedData)
        cov_dict[i] = analyzedData
        mean+=analyzedData
    print "cov dict inside ",cov_dict
    print "Mean cov is ",float(mean)/(candidates/n)
        
##de()  
def analyzeCoverageData(cov,filename):
##    dict = cov.analysis2("C:\\python27\\lib\\site-packages\\bintrees\\bintree.py")
##    dict = cov.analysis2("C:\\Users\\Juhi\\Desktop\\notes\\sem 3\\ASE\\git repo\\x9115baymax\\project\\bintrees-2.0.2\\bintrees\\bintree.py")
    dict = cov.analysis2("test_all_trees.py")
##    print dict
    totLines = dict[1]
    msdLines = dict[3]
    linesExe = len(totLines) - len(msdLines)
    linesExePc = (float)(linesExe)/ len(totLines)
    
    return linesExePc
    #     cov_list.append(linesExePc)
    #      cov_dict[i] = linesExePc
    # print "cov dict inside ",cov_dict


##def test_001_init(default_values1):
##    cov.erase()
##    cov.start()
##    tree = TREE_CLASS()
##    tree.update(default_values1)
##    cov.stop()


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

