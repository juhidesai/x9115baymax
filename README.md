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
2. Differential Evolution
3. Code Coverage  
4. Frontier   

## Introduction  

This technical report covers the project for CSC591: Automated Software Engineering. To prevent defects in software systems, extensive testing is required, though testing does not always ensure the sanity of a software system. One way of catching as many bugs as possible is to maximize the code covered in test cases (reference needed???). For this, the inputs that are given to the functions should be able to cover as many as possible, if not all, branches of the code. We propose using an optimizer to fiddle with the inputs such that we get a set of inputs that will achieve maximum (or up to the mentioned threshold) coverage.  

## Related Work  

## The "Model"

The real world problem, or "model", that we are trying to optimize is of test case input generation. 

## The Optimization Problem

What is the ideal set of inputs that the code should be tested with to achieve high code coverage? We try to give a set of inputs that will maximize code coverage for the given code base. We generate a frontier of 200 candidates and optimize it using DE's equation.  

## The Optimizer  

As our optimizer, we are using the differential evolution method. (insert from class notes here)

## Our Algorithm  

## Our Approaches  

1. Varying type of inputs  
2. Executing on an open source repository

## Modifications needed to run the optimizer

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
