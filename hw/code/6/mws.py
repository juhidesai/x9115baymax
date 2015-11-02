import random

def mws(model_class):
    step_size = 10
    max_tries = 10000
    max_changes = 50

    model = model_class()
    
    min1,max1 = model.set_min_max()
    # print "min max is ",min1," ",max1
    threshold = - 1.2
    # print threshold
    solution_values = []
    solution_energy = -1
    
    best_solution_values = []
    best_solution_energy = max1
    
    for i in range(max_tries):
        # print "*"*20
        solution_values = model.any()
        solution_energy = model.get_energy()
        # if i%25 == 0:
        #     print "\n",i,", ",
        for j in range(max_changes):
            # print '-'*40
            # print model.decs
            score = model.get_energy()
            # print score
            if score < threshold:
                print "\nBest Solution Greater than threshold found"
                return score, solution_values
            
            c = random.randint(0,model.dec_count-1)
            
            if 0.5 < random.random():
                # print "Looking for a solution"
                solution_values = model.any(c)
                solution_energy = model.get_energy()
                # print model.decs
                # print solution_values
                # print "?",  # Crazy jump
            else:
                # print "Rolling in one direction"
                local_best_solution_energy = score # minimize the result
                local_best_value = 0;
                local_best_solution_values = solution_values
                for k in range(step_size):
                    new_value = float((float(model.get_maximum_bound(c) - model.get_minimum_bound(c))/step_size)*k)
                    new_solution = local_best_solution_values
                    new_solution[c] = new_value
                    model.decs = new_solution
                    new_score = model.get_energy()
                    
                    if new_score < local_best_solution_energy:
                        local_best_solution_energy = new_score
                        local_best_value = new_value
                solution_values[c] = local_best_value
                # print solution_values
                solution_energy = local_best_solution_energy
                    
        ##update best seen so far
            # print "current ",solution_energy," ",best_solution_energy
            if solution_energy < best_solution_energy:
                best_solution_energy = solution_energy
                best_solution_values = solution_values
                # print "!",  #Global best solution
            # else:
                # print ".",  # No change
    print "\nBest energy is ",best_solution_energy
    print "Best values are ",best_solution_values
    
