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

class Kursawe:
    
    decs = []
    objs = []
    
    
