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
from test_maincode import check_em
import coverage

cov=coverage.Coverage()

frontier = []
param_list = []
cov_list = []
cov_dict = {}
main_lists = []
n = 5
##def de():
    
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
    
##param_list = [(1, 1), (5,3), (8, 6)]
def test_generator():
    generateParam()
    # Assume frontier = de()
    print frontier
    main_lists = [frontier[i:i+n] for i in range(0,len(frontier),n)]
    print main_lists[0]

    for i,sub_list in enumerate(main_lists):
        print i," ",sub_list
        cov.erase()
        cov.start()
        for params in sub_list:
            yield check_em, params[0], params[1]
        cov.stop()
        dict = cov.analysis2('test_maincode.py')
        print dict
        totLines = dict[1]
        msdLines = dict[3]
        linesExe = len(totLines) - len(msdLines)
        linesExePc = (float)(linesExe)/ len(totLines)
        cov_list.append(linesExePc)
        cov_dict[i] = linesExePc
    print cov_dict
        
    

if __name__ == '__main__':
    #This code will run the test in this file.'

    global module_name
    module_name = sys.modules[__name__].__file__
    print sys.modules[__name__]
    logging.debug("running nose for package: %s", module_name)
##    argv = ['fake','--nocapture']
    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-v', '--nocapture'])#,'--with-coverage','--cover-tests'])
    logging.info("all tests ok: %s", result)
