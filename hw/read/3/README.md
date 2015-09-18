## Reading Homework 3
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
G. Wassermann, D. Yu, A. Chander, D. Dhurjati, H. Inamura and Z. Su, "Dynamic Test Input Generation for Web Applications," Proc. ACM/SIGSOFT Int',l Symp. Software Testing and Analysis, pp. 249-260, 2008.

##### ii. Keywords and Definitions  
<b>ii1. Web application</b>
It is a client-server software application in which the client runs on a web browser.

<b>ii2. Verification </b>
The evaluation of whether the application complies with the conditions.

<b>ii3. Reliability</b> 
Ability of a system to do it intended work for a long(specified) period of time.

<b>ii4. Directed random testing</b>
Directed random testing is a test generation technique which combines bottom-up generation of tests with runtime guidance. The generator executes tests whose result determines whether the test is redundant, illegal, error-revealing, or useful for generating more tests. This helps reduce illegal / unnecessary test generation.

##### iii. Brief Notes
<b> iii1. Motivational Statements</b> 
Authors claims that its hard to perform static analysis on the dynamic features of the scripting languages like PHP as a result the chances of missing out bugs in applications generated using these languages can be significantly high.

<b> iii2. Hypotheses</b> 
The approach presented in paper should be able to address the challenges faced in test generation input for dynamic languages such as PHP. Author basically lists 3 challenges - 1). Scripting languages are not complied languages and are more string - and array-centric as opposed to languages like Java thus allow arbitrary meta-programming. 2). Need for a different kind of test Oracle for PHP and 3). Experimentation of Concolic testing approach - It should be scalable beyond functions.
These challenges can be overcome by 1). Modelling string operations using finite state transducers and employing a constraint resolution algorithm, 2). Using values at run time to backtracking where queries are constructed and making note of the constraints.

<b> iii3. New Results </b>
Authors presented a novel approach of generating test inputs for analysis of scripting languages based on the information collected from previous executions. Author also explored constraint generation wit several orders of magnitude fewer constraints and constraint resolution by considering only one variable occurrence per expression.

<b> iii4. Future Work </b>
As a future work, author proposes to use an oracle that also take into consideration privacy issue such as medical records, also how multiple test executions can be compared to detect information leakage.
Authors also proposes to to explore implementation tradeoffs esp related to constraint generation implementation.

##### iv. Three ways the paper could be improved.
<b> iv1.</b> The algorithm as well as accuracy could be improved by supporting multiple variables in the predicates. The issue with not supporting multivariate constraints is that the accuracy is affected and also it may miss out on certain path executions.

<b> iv2.</b> The current process that they use is manual in many places like loading the page, invoking the analyzer etc. The process should be fully automated to be of use in the real world.

<b> iv3.</b> Selective logging may not always be useful because you may not always know the possible points of failure as well as their approximate location. Removing at least 1 constraint would improve the paper.


##### v. Connection to [paper one](http://dl.acm.org/citation.cfm?id=2190141). 
Like with the previous papers, it also targets PHP web applications. It also uses concolic testing as was used in one of the previous papers. One aspect which is different in this paper is even though it was published before the other papers, It targets discovering security holes like SQL Injection attacks from the generated test cases which the later ones have not covered.

##### References 
1. [Finding Bugs in Web Applications Using Dynamic Test Generation and Explicit-State Model Checking, 2010.](http://dl.acm.org/citation.cfm?id=1850611)
2. [Web application](https://en.wikipedia.org/wiki/Web_application)  
3. [Verification and validation](https://en.wikipedia.org/wiki/Verification_and_validation)
4. [Reliability engineering](https://en.wikipedia.org/wiki/Reliability_engineering)
5. [Directed Random Testing](http://people.csail.mit.edu/cpacheco/publications/pacheco-phd-abstract.html)