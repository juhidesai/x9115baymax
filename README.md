# x9115baymax
CSC 591 Automated Software Engineering

Collaborators:

Juhi Desai (jddesai)  
Rohit Arora (rarora4)   
Ronak Nisher (rpnisher)  

# Project : Optimizing Test Case Inputs to Maximize Coverage  

## Abstract  

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

What is the ideal set of inputs that the code should be tested with to achieve high code coverage? We try to give a set of inputs that will maximize code coverage for the given code base. We generate a frontier of 200 candidates and optimize it using DE's equation.  

## The Optimizer  

As our optimizer, we are using the differential evolution method. (insert from class notes here)

## Our Algorithm  
Our core algoritm follows the usual DE algoritm with changes in the parts of generating and extrapolating from candidates. Another point in the difference is that we run code coverage on each set of candidates. This passes control to an external entity which calculates the coverage values which would be later on used for checking which one is better.  

## Our Approaches  

1. Varying type of inputs  
   We allow having various types of inputs like Integers, Reals, Strings and Lists. As of now, each input type has it's own different code which has it's own way of generating new children based on 3 other candidates. This can be easily turned into a unifieed and more general approach in the future.  

The reason a single way would not work is because each input type has it's own differenent characteristic and willl not conform to a restricted type of manipulation. The current ways in which we do this are as follows:  

-- Integer: PUT EQUATION HERE  

-- Reals: PUT EQUATION HERE  

-- Strings:  PUT EQUATION HERE

-- Lists:  we replace a portion of the existing list by randomly replacing it with another element from another candidate. The amount of portion is controlled by a factor 'cf'.  

  PUT CODE SNIPPETS IN ALL IF POSSIBLE  
  
  
2. Executing on an open source repository  
   Being able to run this algorithm on your test cases and project is a very important aspect of this project. To help ease this, we had a use case scenario where we took an open source project and ran our algorithm on its test cases. There is a single point entry in the code in the generator method which can be used to call all other functions that you care about. the option of which functions to take are left with the userin that single entry function. We had to put up a few conditions on the way the test case files are structures to be able to run our algorithm with ease. The code and test cases should be in the same file. This condition is mostly due to the way coverage is calculated by the coverage library. This restriction should be removed in the future work.

## Modifications needed to run the optimizer
  If the input type is different than any of the above, the generation and extrapolation functions would need to be modified accordingly. The test cases should also include the code in the same file.

## Results  

## Threats to Validity  

## Conclusion  

## Future Work  

Currently, we have to call each test case explicitly. A possible improvement would be to parse the test case file ,read the function names and execute them dynamically.  
Also, the algorithm needs to be modified to run with different types of input, the same code cannot be used with integers and lists currently.

## References  

1. Ned Batcders covergae.py
2. class slides
3. bitbucket link for bintrees2.0.2
