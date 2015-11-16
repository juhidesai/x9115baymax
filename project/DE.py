import random
import math

# Defining some Paramter Settings
N = 2;
M = 50;
F = 0.5; #Mutation Factor
C = 0.9; #Cross Over rate
I_max = 200; #Max iteration rate
Run = 1;
X_max = 5
X_min = -5;

def rand1(X,M,F,m):
    items = range(M)
    R = random.shuffle(items)
    j = R[0]
    k = R[1]
    p = R[2]
    u = R[3]
    v = R[5]
    
    if j == m:
        j = R[6]
    
    elif k == m:
        k = R[6]
    
    elif p == m:
        p = R[6]
        
    elif u == m:
        u = R[6];
        
    elif v == m:
        v = R[6];
    
    V = [0 for b in  range(N)]
    for i in len(X[0]):
        V[0][i] = X[j][i] + F*(X[k][i] - X[p][i])
    
    return V 

def de():
    for r in range(Run):
        iter = 0;
        X = [[0 for x in range(N)] for x in range(M)] 
        U = [0 for b in  range(N)]
        
        X1 = [[0]*N for i in range(M)]
        U1 = [0]*N
        
        # 1.Generate MxN matrix
        for m in range(M):
            for n in range(N):
                X[m][n] = X_min + random.random()*(X_max - X_min)
                print X[m][n]
                
        for i in range(I_max):
            
            iter = iter + 1
            
            for m in range(M):
                V = rand1(X,M,F,m)
                
                for n in range(N):
                    if V[1][n] > X_max:
                        V[1][n] = X_max
                    if V[1][n] < X_min[1][n]:
                        V[1][n] = X_min
                        
                jrand = math.floor(random.random()*N + 1)
                for n in range(N):
                    R1 = random.random();
                    if R1 < C or n == jrand:
                        U[1][n] = V[1][n]
                    else:
                        U[1][n] = X[m][n]
                
                
                        
                
de()