# x9115baymax
CSC 591 Automated Software Engineering

Collaborators:

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

## Results  

## Threats to Validity   

* If the input type is different than any of the above, the generation and extrapolation functions would need to be modified accordingly. 
* The test cases should also include the code in the same file.
* Verified only on an open source code of about 500 LOC.
* Verified only for a container type library implementation(although this a norm in verifying similar algorithms).

## Conclusion  

The algorithm developed by us for this project was tested on an open source project [4]. We managed to generate an input with coverage of a little over 95% while the original inputs that were used in the project had a coverage of 91%. This is an indication that Differential Evolution based input generation algorithms can generate inputs to test cases with a high coverage. The tests with other input types also got a consistently high coverage of above 95% (losing the 5% because of the way coverage libraries measured the coverage wherein they reported def function_names as executable missed statements). This goes on to show that the algorithm implemented can work on different types of inputs as well. 

## Future Work  

Currently, we have to call each test case explicitly. A possible improvement would be to parse the test case file ,read the function names and execute them dynamically.  
Also, the algorithm needs to be modified to run with different types of input, the same code cannot be used with integers and lists currently.

## References  
1. [Ned Batchelder's coverage.py](https://coverage.readthedocs.org/en/coverage-4.0b3/index.html)
2. [Lecture Notes](https://github.com/txt/mase/blob/master/DE.md)
3. [Bintrees Repository] (https://bitbucket.org/mozman/bintrees/overview)
4. [Differential Evolution, Wikipedia](https://en.wikipedia.org/wiki/Differential_evolution)
5. [Pargas, Roy P., Mary Jean Harrold, and Robert R. Peck. "Test-data generation using genetic algorithms." Software Testing Verification and Reliability 9.4 (1999): 263-282.](ucvesontio-website.googlecode.com/svn/trunk/projetTut/articles/test-data%20genetic%20algo.pdf)
