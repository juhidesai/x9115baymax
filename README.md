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

## The "Model"

The real world problem, or "Model", that we are trying to optimize is of test case input generation. Any software project has code which needs to be tested. Any of these projects can be taken as our model.

## The Optimization Problem

Nowadays, emphasis is placed on testing any code that gets shipped. To achieve this, testers and developers need to write test cases and ensure code coverage atleast upto a predetermied threshold. To write effective test cases with appropriate coverage, good test cases and inputs should be used. Deciding which test case inputs will achieve this goal is a time consuming preocess. The most important factor in that is to answer the question "What is the ideal set of inputs that the code should be tested with to achieve high code coverage?" Our model comes in to solve this problem of generating test case inputs which are optimal. Given an input test case/function, our code can run through it and give the input test case that maximizes code coverae over that piece of code.
 
 The crux of the optimization lies in generating the inputs. To achieve this, we make use of Differential Equation to generate better candidates in the next generation. The DE algorithm is configurable to change parameters like number of candidates, number of runs, patience etc.
 
 //We generate a frontier of 200 candidates and optimize it using DE's equation.  

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

-- Integer: PUT EQUATION HERE  

-- Reals: PUT EQUATION HERE  

-- Strings:  PUT EQUATION HERE

-- Lists:  we replace a portion of the existing list by randomly replacing it with another element from another candidate. The amount of portion is controlled by a factor 'cf'.  

  PUT CODE SNIPPETS IN ALL IF POSSIBLE  
  
  
2. Executing on an open source repository  
   Being able to run this algorithm on your test cases and project is a very important aspect of this project. To help ease this, we had a use case scenario where we took an open source project and ran our algorithm on its test cases. There is a single point entry in the code in the generator method which can be used to call all other functions that you care about. the option of which functions to take are left with the user in that single entry function. We had to put up a few conditions on the way the test case files are structured to be able to run our algorithm with ease. The code and test cases should be in the same file. This condition is mostly due to the way coverage is calculated by the coverage library. This restriction should be removed in the future work.

## Modifications needed to run the optimizer  

To run DE with different types of inputs, we had to change the way frontier was generated and how the extrapolation was done. For the open source bintrees project, the frontier was a list of 200 candidates, each candidate was a tuple containing 3 lists. For integers and real numbers, the frontier was a list of 200 candidates, each candidate was a tuple containing 2 values. For string, each candidate was a tuple containing 4 strings.  

## Problems Faced  

While dealing with the open source repository, there were issues with calculating the coverage of the actual code. This was mainly due to the fact that this repository was on trees, which is separately installed as a package for Python. We were unable to calculate the coverage on the actual source files because of this.  

As a work-around, we had to remove the import statements, and pull the source code into the test file itself. This problem should not occur for repositories which have a separate installation.  

## Results  

## Threats to Validity   

If the input type is different than any of the above, the generation and extrapolation functions would need to be modified accordingly. The test cases should also include the code in the same file.

## Conclusion  

## Future Work  

Currently, we have to call each test case explicitly. A possible improvement would be to parse the test case file ,read the function names and execute them dynamically.  
Also, the algorithm needs to be modified to run with different types of input, the same code cannot be used with integers and lists currently.

## References  
1. [Ned Batchelder's coverage.py](https://coverage.readthedocs.org/en/coverage-4.0b3/index.html)
2. [Lecture Notes](https://github.com/txt/mase/blob/master/DE.md)
3. [Bintrees Repository] (https://bitbucket.org/mozman/bintrees/overview)
4. [Differential Evolution, Wikipedia](https://en.wikipedia.org/wiki/Differential_evolution)
