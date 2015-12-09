# x9115baymax
### CSC 591 Automated Software Engineering

**Collaborators:**  
Juhi Desai (jddesai)  
Rohit Arora (rarora4)   
Ronak Nisher (rpnisher)  

# Project : Optimizing Test Case Inputs to Maximize Coverage  

## Abstract  

Testing of applications and code is an important part of the software development lifecycle. Higher code coverage is a sign of a thoroughly tested code. The process of writing inputs which would achieve the required for the test cases is a manual and time consuming process. The tool developed and documented in this report is aimed to automate this process. The tool can can give the input which can be used as in test cases to ensure a high coverage. The algorithm used in the tool is based on Differential Evolution and uses code coverage as a criteria to ensure better set of candidates in the next generation.  

## Keywords

1. Optimizer  
   An optimizer is a piece of code that makes your input, code or any entity that you care about better. In case of our model, the optimizer will optimize the inputs given to test cases.  

2. Differential Evolution  
   Differential evolution is an algorithm that is used to optimize a model in an iterative fashion based on a pre determined quality factor.  

3. Code Coverage  
   Code Coverage is a measurement of the amount of code that has is being checked by the test cases. It is generally measured in % with the aim to achieve 100% of the lines of the code. There are  many types of code coverage like Statement, branch etc. Our project measures statement level coverage (but it is also possible to check for branch level coverage).  

4. Frontier   
   A frontier is a set of solutions. It can be compared to a set of solutions which represent a generation, over time, the generation will undergo changes and a new set of solutions will be born. There are other factors which control this as well, but the essence of the algorithm remains that if the child is better than the parent, the parent will be replaced by the child.

## Introduction  

This technical report covers the project for CSC591: Automated Software Engineering. To prevent defects in software systems, extensive testing is required, though testing does not always ensure the sanity of a software system. One way of catching as many bugs as possible is to maximize the code covered in test cases (reference needed???). For this, the inputs that are given to the functions should be able to cover as many as possible, if not all, branches of the code. We propose using an optimizer to fiddle with the inputs such that we get a set of inputs that will achieve maximum (or up to the mentioned threshold) coverage.  

## Related Work  

There is literature available that revolves around dynamically generating test case inputs/test data generation but a majority of them are based on Java as an underlying language. There is very little done for Python. 

There are a lot of techniques for automated test-data generation like Random, structural, goal oriented or intelligent.  
* Random: select random inputs for the test data from some distribution.  
* Structural(path oriented): These use the program's control flow graph, select a particular path and then use symbolic evaluation to generate test data for that path.
* Goal oriented: They selecct inputs to execute a selected goal irrespective of path taken.
* Intelligent: These rely on sophisticated code analysis to help search for new test data.

The approach we use in our implementation is a Goal oriented approach as there are limitations to the others as shown here:
* Random: Although it generates a lot of data, it may not satisfy the requirements as the random generator does not know about the specific requirements.
* Structural: If the path identified is infeasible, it may not get an input that will traverse a path.
* Intelligent: Although this can be very accurate, the time and complexity required to acheive this makes it infeasible for real world problems.


The paper which resembles most to what we have done is in a paper titled "Test-data generation using genetic algorithms"(Pargas, Roy P., Mary Jean Harrold, and Robert R. Peck. "Test-data generation using genetic algorithms." Software Testing Verification and Reliability 9.4 (1999): 263-282.)[577 citations]. This paper uses a genetic algorithm to generate test data for programs written in C language with LOCs ranging from 20 to 80. The paper uses a tool they developed called TGen which helps them in doing this. The tool relies on the control dependence graph to get a better generation. The algorithm tht we propose depends on a library called coverage.py which is a highly relied upon library for measuring code coverage in Python.

## The "Model"

The real world problem, or "Model", that we are trying to optimize is of test case input generation. Any software project has code which needs to be tested. Any of these projects can be taken as our model.

## The Optimization Problem

Nowadays, emphasis is placed on testing any code that gets shipped. To achieve this, testers and developers need to write test cases and ensure code coverage atleast upto a predetermied threshold. To write effective test cases with appropriate coverage, good test cases and inputs should be used. Deciding which test case inputs will achieve this goal is a time consuming preocess. The most important factor in that is to answer the question "What is the ideal set of inputs that the code should be tested with to achieve high code coverage?" Our model comes in to solve this problem of generating test case inputs which are optimal. Given an input test case/function, our code can run through it and give the input test case that maximizes code coverae over that piece of code.
 
 The crux of the optimization lies in generating the inputs. To achieve this, we make use of Differential Equation to generate better candidates in the next generation. The DE algorithm is configurable to change parameters like number of candidates, number of runs, patience etc.
 
## The Optimizer  

As our optimizer, we are using the differential evolution method. "Differential evolution (DE) is a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. Such methods are commonly known as metaheuristics as they make few or no assumptions about the problem being optimized and can search very large spaces of candidate solutions. However, metaheuristics such as DE do not guarantee an optimal solution is ever found." [4]  

DE optimizes a problem by maintaining a population of candidate solutions (frontier) and creating new candidate solutions by taking one (randomly chosen), selecting three other than the one selected, combining values of those three and creating a new candiate. If the new candidate is better than the first one, we replace that with the new candidate.  

## Our Algorithm  

Our core algoritm follows the usual DE algoritm with changes in the parts of generating and extrapolating from candidates. Another point in the difference is that we run code coverage on each set of candidates. This passes control to an external entity which calculates the coverage values which would be later on used for checking which one is better.  

Step 1. A frontier with randomly generated inputs is prepared.  
Step 2. Code coverage for required function(s) is calculated.  
Step 3. If code coverage is less than threshold, a new generation is created. If the new candidate is better than the parent, the parent is replaced.  
Step 4. Step 2 and Step 3 are repeated till patience runs out, or coverage equal to or greater than the threshold is reached.  

## Our Approaches  

1. Varying type of inputs  
   We allow having various types of inputs like Integers, Reals, Strings and Lists. As of now, each input type has it's own different code which has it's own way of generating new children based on 3 other candidates. This can be easily turned into a unified and more general approach in the future.  

The reason a single way would not work is because each input type has it's own differenent characteristic and will not conform to a restricted type of manipulation. The current ways in which we do this are as follows:  

-- Integer:

       if random.random() < cf:
            new[i] = int(x + f*(y - z))
        else:
            new[i] = one[i]  
            
    x,y and z are 3 other candidates from same generation as parent(one)
    f is the controlling factor  
    cf is probability of change

-- Reals:  

       if random.random() < cf:
               new[i] = x + f*(y - z)
           else:
               new[i] = one[i]
    x,y and z are 3 other candidates from same generation as parent(one)
    f is the controlling factor  
    cf is probability of change           
   

-- Strings:  

       if random.random() < cf:
            tmp = int(x + f*(y - z))
            new[i] = trim(tmp)
        else:
            new[i] = one[i]
    x,y and z are 3 other candidates from same generation as parent(one)
    f is the controlling factor  
    cf is probability of change

-- Lists:  we replace a portion of the existing list by randomly replacing it with another element from another candidate. The amount of portion is controlled by a factor 'cf'.  

         if random.random() < cf:
            new[i]=[0]*len(one[i])
            new[i] = one[i]
            for j in range(int(f*len(one[i]))):
                r1 = random.randint(0,len(one[i])-1)
                r2 = random.randint(0,len(one[i])-1)
                r3 = random.randint(0,len(one[i])-1)
                new[i][r1] = x[random.randint(0,len(x)-1)]
                new[i][r2] = y[random.randint(0,len(y)-1)]
                new[i][r3] = z[random.randint(0,len(z)-1)]
        else:
            new[i] = one[i]
    x,y and z are 3 other candidates from same generation as parent(one)
    f is the controlling factor  
    cf is probability of change

  
2. Executing on an open source repository  
   Being able to run this algorithm on your test cases and project is a very important aspect of this project. To help ease this, we had a use case scenario where we took an open source project and ran our algorithm on its test cases. There is a single point entry in the code in the generator method which can be used to call all other functions that you care about. the option of which functions to take are left with the user in that single entry function. We had to put up a few conditions on the way the test case files are structured to be able to run our algorithm with ease. The code and test cases should be in the same file. This condition is mostly due to the way coverage is calculated by the coverage library. This restriction should be removed in the future work.

## Modifications needed to run the optimizer  

To run DE with different types of inputs, we had to change the way frontier was generated and how the extrapolation was done. For the open source bintrees project, the frontier was a list of 200 candidates, each candidate was a tuple containing 3 lists. For integers and real numbers, the frontier was a list of 200 candidates, each candidate was a tuple containing 2 values. For string, each candidate was a tuple containing 4 strings.  

## Problems Faced  

While dealing with the open source repository, there were issues with calculating the coverage of the actual code. This was mainly due to the fact that this repository was on trees, which is separately installed as a package for Python. We were unable to calculate the coverage on the actual source files because of this.  

As a work-around, we had to remove the import statements, and pull the source code into the test file itself. This problem should not occur for repositories which have a separate installation.  

## Instructions to Run Files  

[Instructions to Run Files] (https://github.com/juhidesai/x9115baymax/blob/master/project/README.md)  
## Results  

The algorithm we developed can be configured to take customvalues for number of candidates in each solution set(n), number of candidates to generate(candidates), the controlling factor which determines how much part of the original solution should be mutated(cf) as well as the probability of mutating a candidate parent(c). 

We have highlighed the effect of candidate solution size in the following diagrams. The core insight here is that increasing the number of candidate solutions in a set inproves coverage(and takes a less number of generations to achieve the threshold).

Data Results:

1. Varying number of candidate solutions(n)

These results show the coverage normalized to a float between 0 and 1 with 1 being the highest (100% coverage) shown with the help of an Inter Quartile Range mapping.

n is the number of candidate solutions in a single test input case (The output of our program will be such a set with maximal coverage)

n = 2
````
(            |   *--      ),  0.50,   0.55,   0.65,   0.65,   0.80
(            |   *----    ),  0.50,   0.55,   0.65,   0.70,   0.85
(            |-  *----    ),  0.50,   0.60,   0.65,   0.70,   0.85
(            |-  *----    ),  0.55,   0.60,   0.65,   0.70,   0.85
(            |   *--      ),  0.50,   0.55,   0.65,   0.70,   0.80
(            |-  *--      ),  0.50,   0.60,   0.65,   0.65,   0.80
(            |-  *--      ),  0.50,   0.60,   0.65,   0.70,   0.80
(            |-  * -      ),  0.50,   0.60,   0.65,   0.75,   0.80
(            |-  *--      ),  0.50,   0.60,   0.65,   0.70,   0.80
(            |-  *----    ),  0.50,   0.60,   0.65,   0.70,   0.85
(            |-  * ---    ),  0.50,   0.60,   0.65,   0.75,   0.85
(            |--- * --    ),  0.55,   0.65,   0.70,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
(            |---*  --    ),  0.55,   0.65,   0.65,   0.80,   0.85
````

n = 4
````
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90
(            |   -*   -   ),  0.65,   0.70,   0.70,   0.85,   0.90

````
n = 8

````
(            |         *  ),  0.70,   0.70,   0.90,   0.90,   0.90
(            |         *  ),  0.70,   0.70,   0.90,   0.90,   0.90
(            |    -    *  ),  0.70,   0.75,   0.90,   0.90,   0.90
(            |    -----*  ),  0.70,   0.90,   0.90,   0.90,   0.90
(            |    -----*  ),  0.70,   0.90,   0.90,   0.90,   0.90
(            |        -*  ),  0.85,   0.90,   0.90,   0.90,   0.90
(            |        -*  ),  0.85,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
(            |         *  ),  0.90,   0.90,   0.90,   0.90,   0.90
```` 
As we can observe, the mean has shidet towards a better solution as the number of candidates have increased. It can also be observed that a larger n resulted in getting to the threshold in less generations than the others.  

## Threats to Validity   

* If the input type is different than any of the above, the generation and extrapolation functions would need to be modified accordingly. 
* The test cases should also include the code in the same file.
* Verified only on an open source code of about 500 LOC.
* Verified only for a container type library implementation(although this a norm in verifying similar algorithms).


## Sample Output of the Program  

````
Mean:  0.632
Candidates with more than 75% coverage:  13
median:  0.65
----------------------------------------
Mean:  0.6255
Candidates with more than 75% coverage:  13
median:  0.6
----------------------------------------
Mean:  0.6475
Candidates with more than 75% coverage:  17
median:  0.65
----------------------------------------
Mean:  0.6515
Candidates with more than 75% coverage:  21
median:  0.65
----------------------------------------
Mean:  0.6655
Candidates with more than 75% coverage:  24
median:  0.65
----------------------------------------
Mean:  0.671
Candidates with more than 75% coverage:  23
median:  0.65
----------------------------------------
Mean:  0.667
Candidates with more than 75% coverage:  19
median:  0.65
----------------------------------------
Mean:  0.6735
Candidates with more than 75% coverage:  19
median:  0.65
----------------------------------------
Mean:  0.678
Candidates with more than 75% coverage:  30
median:  0.675
----------------------------------------
Mean:  0.6605
Candidates with more than 75% coverage:  30
median:  0.65
----------------------------------------
Mean:  0.6765
Candidates with more than 75% coverage:  28
median:  0.65
----------------------------------------
Mean:  0.686
Candidates with more than 75% coverage:  29
median:  0.65
----------------------------------------
Mean:  0.703
Candidates with more than 75% coverage:  38
median:  0.7
----------------------------------------
Mean:  0.684
Candidates with more than 75% coverage:  29
median:  0.65
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
----------------------------------------
Mean:  0.683
Candidates with more than 75% coverage:  28
median:  0.675
No change in coverage
****************************************
Ran out of patience
****************************************
{0: 0.85, 1: 0.6, 2: 0.55, 3: 0.55, 4: 0.65, 5: 0.6, 6: 0.85, 7: 0.85, 8: 0.5, 9: 0.8, 10: 0.65, 11: 0.65, 12: 0.85, 13: 0.55, 14: 0.85, 15: 0.6, 16: 0.8, 17: 0.85, 18: 0.7, 19: 0.75, 20: 0.6, 21: 0.8, 22: 0.75, 23: 0.75, 24: 0.75, 25: 0.7, 26: 0.55, 27: 0.6, 28: 0.8, 29: 0.6, 30: 0.7, 31: 0.65, 32: 0.7, 33: 0.55, 34: 0.85, 35: 0.85, 36: 0.7, 37: 0.55, 38: 0.7, 39: 0.75, 40: 0.85, 41: 0.65, 42: 0.6, 43: 0.6, 44: 0.5, 45: 0.5, 46: 0.65, 47: 0.5, 48: 0.85, 49: 0.65, 50: 0.8, 51: 0.8, 52: 0.85, 53: 0.75, 54: 0.7, 55: 0.8, 56: 0.75, 57: 0.6, 58: 0.75, 59: 0.6, 60: 0.65, 61: 0.8, 62: 0.65, 63: 0.75, 64: 0.7, 65: 0.5, 66: 0.5, 67: 0.65, 68: 0.65, 69: 0.65, 70: 0.55, 71: 0.5, 72: 0.5, 73: 0.8, 74: 0.7, 75: 0.65, 76: 0.8, 77: 0.45, 78: 0.75, 79: 0.55, 80: 0.6, 81: 0.6, 82: 0.8, 83: 0.85, 84: 0.7, 85: 0.55, 86: 0.8, 87: 0.8, 88: 0.65, 89: 0.85, 90: 0.65, 91: 0.55, 92: 0.5, 93: 0.65, 94: 0.85, 95: 0.8, 96: 0.7, 97: 0.65, 98: 0.6, 99: 0.7}
(            |   *--      ),  0.50,   0.55,   0.65,   0.65,   0.80
(            |-* ---      ),  0.50,   0.60,   0.60,   0.65,   0.80
(            |-  *--      ),  0.50,   0.60,   0.65,   0.70,   0.80
(            |-  *----    ),  0.50,   0.60,   0.65,   0.70,   0.85
(            |-  *----    ),  0.50,   0.60,   0.65,   0.70,   0.85
(            |-  *----    ),  0.50,   0.60,   0.65,   0.70,   0.85
(            |---*--      ),  0.55,   0.65,   0.65,   0.70,   0.80
(            |---* -      ),  0.55,   0.65,   0.65,   0.75,   0.80
(            |-   *       ),  0.50,   0.60,   0.70,   0.80,   0.80
(            |   *        ),  0.50,   0.55,   0.65,   0.80,   0.80
(            |---* -      ),  0.55,   0.65,   0.65,   0.75,   0.80
(            |---* ---    ),  0.55,   0.65,   0.65,   0.75,   0.85
(            |--- * --    ),  0.55,   0.65,   0.70,   0.80,   0.85
(            |---* ---    ),  0.55,   0.65,   0.65,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
(            |-   *---    ),  0.55,   0.60,   0.70,   0.75,   0.85
Final frontier is:
[(-9, -11, -27, -7), (9, 20, 48, 43), (-14, -5, -1, 183), (-9, 4, -56, 109), (96, -7, -29, -8), (6, 2, 76, -39), (11, 0, 10, 51), (36, 6, 6, 77), (-3, 18, -76, 46), (93, 4, 68, -4), (0, -10, -2, 3), (-11, 13, -99, 20), (-44, -7, 17, -40), (41, 15, 78, 43), (30, -16, 47, -2), (-48, -25, 35, 20), (26, 6, 20, 14), (14, -22, 4, 26), (-87, -14, 3, 15), (46, 35, 8, 34), (-3, 4, 63, 9), (-6, -15, 4, 14), (-36, -2, -33, -3), (12, 8, -42, -15), (-46, -23, 0, 7), (17, 9, 88, 6), (-47, 42, -99, -40), (-33, 28, 1, -19), (-28, 8, 1, 73), (19, 4, 47, 0), (-26, 0, 16, -7), (-36, 16, -51, -25), (-46, 49, 6, -31), (-20, 30, 136, 47), (-2, -38, -18, 26), (-84, 43, 6, 11), (30, -3, 12, 19), (-32, 10, -39, 54), (-66, 2, -119, 54), (-46, 6, 11, -23), (-13, -8, 17, 8), (-40, 47, -13, 1), (5, -32, 2, -5), (-7, 138, 48, 39), (-13, -12, 9, 25), (-36, 13, 13, 0), (7, 34, 49, -28), (-21, -12, 91, 9), (11, 18, 94, -36), (-53, -50, 41, 147), (38, 1, 13, -41), (-13, -9, -31, -47), (-2, 18, -3, -13), (-24, 10, 35, 8), (27, 33, 23, -65), (-139, 9, 10, -18), (14, 45, 68, 10), (-30, 32, -9, 4), (-7, 9, -43, -4), (-77, -3, -24, 3), (7, -11, -30, 1), (20, -3, 15, 106), (38, 8, -9, 47), (-13, -1, -22, 32), (-29, -35, 16, 17), (4, 15, -9, 33), (-9, -16, -52, 40), (62, 18, 56, 13), (17, -42, -50, 56), (-49, 49, 3, -2), (-31, -32, 102, 26), (-11, 7, 74, -9), (-32, 3, 8, -5), (33, -9, 8, 0), (11, 18, 27, -20), (-16, 57, 26, 5), (20, -8, -1, 31), (-15, 18, -20, 28), (-33, 48, -32, -68), (7, 52, -14, 13), (48, -4, 76, 48), (-11, 150, -19, -13), (46, -4, 94, 2), (5, 29, -6, 33), (-5, 9, 18, -17), (9, 10, -40, 1), (-26, 23, 123, -71), (-26, 10, -33, -10), (28, 28, -12, -10), (10, -3, 26, -1), (-7, -10, 31, 45), (110, -13, 27, 42), (50, -41, 40, -16), (56, -1, -8, 26), (56, 8, 21, 84), (4, -24, 48, 25), (-20, 9, -63, -14), (11, -45, 11, 90), (-50, 15, -31, -29), (25, -17, 26, -49), (23, 6, -11, -9), (-82, -1, 16, 21), (24, 4, 4, -67), (41, 47, 129, 79), (109, 4, -21, -71), (-20, 14, 62, 96), (12, 14, 22, -19), (4, 68, 6, 47), (-35, -17, -81, 5), (83, -8, 2, -18), (-3, -14, 3, 9), (-44, 57, 11, 69), (4, 40, -23, 16), (-26, 30, -47, 11), (8, 18, 44, 39), (-28, 18, 5, 30), (-38, 16, -23, 17), (-14, 10, -19, 8), (-37, 65, 66, 4), (26, -28, 9, -56), (-7, -10, 28, -16), (64, 19, 11, 19), (0, 20, -136, 6), (-43, 12, -14, 16), (-8, -2, 53, -119), (37, -17, 1, -20), (-8, 0, -63, 35), (12, 88, 47, -8), (-52, 57, 53, 9), (28, 0, -2, -21), (18, -6, -16, 19), (19, 3, -66, 42), (-6, -12, 106, -17), (29, -53, -50, -19), (-75, 10, -107, -39), (0, -28, -96, 6), (4, 42, 6, 46), (-85, 6, -79, 69), (11, -11, 35, -68), (-3, -7, 21, 104), (0, 4, 32, -23), (-12, 6, -46, 2), (10, 2, 113, 9), (25, 5, 41, 96), (22, -45, 26, 19), (8, -21, 17, 124), (-37, 29, 46, 125), (-41, -10, -21, -20), (28, -44, 35, 73), (16, 11, -46, -25), (47, 39, 5, -107), (-28, 0, -7, -49), (-43, 7, -3, 35), (61, 13, -32, -8), (-3, -34, 13, -51), (-12, -57, -48, -16), (-27, 8, -44, 133), (-3, 30, -30, -18), (98, -14, -1, -104), (114, -53, 40, -73), (-24, 29, -7, 3), (-8, 129, 46, -25), (-17, 36, -48, 109), (-54, -17, -13, 29), (5, -15, 0, 4), (-23, -17, 29, 62), (14, -23, 54, 10), (-88, -12, -21, 20), (28, 6, -7, 8), (43, 32, -146, -39), (37, 19, 21, 9), (12, 9, 34, 45), (46, -12, -39, 8), (-14, 6, 5, 45), (-37, -27, -24, 11), (10, 29, 4, 76), (-11, -6, -55, 42), (4, 22, 79, 15), (19, -35, -21, 5), (-35, 34, -35, 55), (-3, 62, -3, 75), (-39, -19, -75, 78), (7, -15, 20, 46), (112, -19, -74, 21), (15, -26, 10, -68), (4, -13, -12, 5), (19, -54, 4, 4), (8, 13, -14, -37), (18, -5, 7, -6), (-51, 45, 83, 47), (10, 20, -47, 2), (66, 111, -12, 8), (64, -46, -7, 45), (-8, 21, 36, 72), (-71, 8, 61, -54), (-6, 34, -19, -3), (14, -31, 0, -44), (11, 20, -15, -2), (12, -13, -12, -39), (-28, -34, 10, 33)]
ok

----------------------------------------------------------------------
Ran 1 test in 219.451s

OK
INFO:root:all tests ok: True

````
## Conclusion  

The algorithm developed by us for this project was tested on an open source project [4]. We managed to generate an input with coverage of a little over 95% while the original inputs that were used in the project had a coverage of 91%. This is an indication that Differential Evolution based input generation algorithms can generate inputs to test cases with a high coverage. The tests with other input types also got a consistently high coverage of above 95% (losing the 5% because of the way coverage libraries measured the coverage wherein they reported def function_names as executable missed statements). This goes on to show that the algorithm implemented can work on different types of inputs as well. 

## Future Work  

In terms of the algorithm, these are the few points that can be worked upon:  
1. The first thing is to do an automatic parameter optimization for the various parameters used like number of candidates, change probability, size of input set etc.
2. Another thing that can be done is to experiment with the child generation technique. give that there can be different types of inputs, a good child generation technique can be used for each type of input.

In terms of pure implementation, there are a few things that we can do to make this tool easy to use in real world projects. The following are some of the points:  
1. Currently, we have to call each test case explicitly. A possible improvement would be to parse the test case file ,read the function names and execute them dynamically.  
2. Also, the current implementation requires a complex setup in terms of dependency and test file imports, these can be resolved in a better way so that the developers can run tests irrespective of what their project structure looks like.
3. Another improvement could be to use a single file for any input type. This is just a matter of adding a switch case/if-else construct to the appropriate methods. This would also allow varied input types to be used together.
4. We can also think about allowing developers to extend this class so as to add their own implementation for the extrapolation or candidate generatio method.  

The other thing that we leartnt is that there is a lot of different ways that this can be used. It could be used directly on the code, it can be run on the test cases as well as on a single function. To be able to cater to these different methods, the tool should be able to handle a variety of inputs as well as use cases. We have tried to generalize our code accordingle to be able to handle these scenarios.

Some of the results that we saw did conform to normal human intuition. For instance, we saw that increasing the number of input candidates in a test case set resulted in a higher coverage as well as an early achievement of the threshold. On the other hand, the coverage seemed to be on the lower side and took longer to come to the threshold.
MAYBE PUT A STATISTIC DIAGRAM HERE

One more lesson learnt was that each code is different and so is its characteristic while running this code. There is no single set of parameters that will work for any input. the way to go forward with these types of algorithms is to use automatic parameter tuning.

## References  
1. [Ned Batchelder's coverage.py](https://coverage.readthedocs.org/en/coverage-4.0b3/index.html)
2. [Lecture Notes](https://github.com/txt/mase/blob/master/DE.md)
3. [Bintrees Repository] (https://bitbucket.org/mozman/bintrees/overview)
4. [Differential Evolution, Wikipedia](https://en.wikipedia.org/wiki/Differential_evolution)
5. [Pargas, Roy P., Mary Jean Harrold, and Robert R. Peck. "Test-data generation using genetic algorithms." Software Testing Verification and Reliability 9.4 (1999): 263-282.](ucvesontio-website.googlecode.com/svn/trunk/projetTut/articles/test-data%20genetic%20algo.pdf)
6. [Statictics class lecture] (https://github.com/txt/mase/blob/master/STATS.md)
