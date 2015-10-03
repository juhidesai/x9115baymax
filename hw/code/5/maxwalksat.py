import random
import model

mins = [0,0,1,0,1,0]
maxs = [10,10,5,6,5,10]

step_size = 10

def maxwalksat():
    max_tries = 1000
    max_changes = 100
    
    min1,max1 = model.getBaselineEnergy()
    
    threshold = max1 * 5
    
    solution_values = []
    solution_energy = -1
    
    best_solution_values = []
    best_solution_energy = -1
    
    for i in range(max_tries):
        solution_energy, solution_values = model.getSolution()
        if i%50 == 0:
            print "\n",i,", ",
        for j in range(max_changes):
            score = model.getScore(solution_values)
            if score > threshold:
                print "Best Solution Greater than threshold found"
                print score
                print solution_values
                return score, solution_values
            
            c = random.randint(0,5)
            
            if 0.5 < random.random():
                while True:
                    solution_values[c] = model.getRandomXValues(c)
                    
                    if model.checkConstraints(solution_values) == True:
                        break
                    c = random.randint(0,5)
                solution_energy = model.getScore(solution_values)
                print "?",  # Crazy jump
            else:
                local_best_solution_energy = -10000
                local_best_value = -1;
                local_best_solution_values = solution_values
                for k in range(step_size):
                    new_value = float((float(maxs[c] - mins[c])/step_size)*k)
                    new_solution = local_best_solution_values
                    new_solution[c] = new_value
                    new_score = model.getScore(new_solution)
                    
                    if new_score > local_best_solution_energy:
                        local_best_solution_energy = new_score
                        local_best_value = new_value
                solution_values[c] = local_best_value
                solution_energy = local_best_solution_energy
                    
        ##update best seen so far
            if solution_energy > best_solution_energy:
                best_solution_energy = solution_energy
                best_solution_values = solution_values
                print "!",  #Global best solution
            else:
                print ".",  # No change
    print "\nBest energy is ",best_solution_energy
    print "Best values are ",best_solution_values
    
maxwalksat()