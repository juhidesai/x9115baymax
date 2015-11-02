from kursawe import Kursawe
from schaffer import Schaffer
from osyczka2 import Osyczka2
import sa
import mws

for model in [Schaffer, Osyczka2, Kursawe]:
    print '-*-'*20
    print 'Model is ',model.__name__
    print '-*-'*20
    for optimizer in [sa.sa, mws.mws]:
      print '='*40
      print 'Optimizer is ',optimizer.__name__
      print '='*40
      optimizer(model)