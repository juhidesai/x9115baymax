## Reading Homework 4
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
Kiran Lakhotia , Phil McMinn , Mark Harman, Automated Test Data Generation for Coverage: Haven't We Solved This Problem Yet?, Proceedings of the 2009 Testing: Academic and Industrial Conference - Practice and Research Techniques, p.95-104, September 04-06, 2009 

##### ii. Keywords and Definitions  
<b>ii1. CUTE</b> 
A tool which used concolic testing to generate test data.

<b>ii2. AUSTIN</b> 
A tool which uses search based methods to generate test data.

<b>ii3. Search Based Testing</b> 
Applying search based metaheuristic techniques to generate test data.
code coverage: the percentage of lines out of all the lines of code that have been covered by tests.

##### iii. Brief Notes
<b> iii1. Motivational Statements</b> 
Author points out that at the time when paper was written two automated test data generation techniques were gaining a lot of attentions, namely Search-based testing and concolic testing, however there were very less evidences how these techniques works in real applications, which one is relatively more effective and what are their shortcomings in terms of program structures that cannot be handled by each technique.

<b> iii2. Hypotheses</b> 
The paper will provide an empirical study comparing CUTE and AUSTIN in terms of code coverage based on four non-trivial open source programs. Moreover this study would also provide answers to the motivational questions author raised. The paper also compares both the papers in terms of the wall clock time required for each tool to obtain respective code coverage.

<b> iii3. Related Work </b>
Author primarily mentions about DART (by Godefrois et al.), tool for Directed Random Testing that attempts to solve constraints involving memory locations. Author also mentions, EGT developed by Cader and Engler that performs pure symbolic execution. Also, CREST, open source success to CUTE, CFG based path exploration strategy. Pex, a parameterized unit test framework by Microsoft, it performs instrumentation at the .Net intermediate language level and thus is able to handle all 'safe' .Net instructions. And makes mentions of several other tools such as ET-S, IGUANA, eToc, EVACON and jCUTE.


<b> iii4. Results </b>
The study revealed that there existed many challenges that needed to be overcome in automatic test data generation as none of the tools could be considered of industrial strength. Both the tools were unable to recover from segmentation faults and could not continue test data generation, also they lacked heterogeneity. And combinations of both static and dynamic analysis is required to perform dynamic testing.


##### iv. Three ways the paper could be improved.
This paper compares two techniques of automated test data generation. They have taken care that there are no biases between test constraints.Hence, there is not much that could be improved in this paper. So, we present some of the improvements that the techniques which are compared could make.

<b> iv1.</b> CUTE: A number of functions could not be tested by CUTE because the test subject did not compile after CUTE’s instrumentation. Taking care that this does not happen should be a good way to improve the tool.

<b> iv2. </b> Both tools have problems unfolding loops. AUSTIN does not work for unbounded loops while CUTE gets stuck unfolding loops in functions. Such time outs should be removed to get a bettter tool.

<b> iv3.</b> When a modified path condition falls outside the supported theory of CUTE’s constraint solver, CUTE does not try random ‘guesses’ in order to find test data. This results in obtaining lesser test data. Having a ‘random guesser’ would increase the amount of test data generated.

##### v. Connection to [paper one](http://dl.acm.org/citation.cfm?id=2190141). 
This paper compares 2 techniques ,viz. Concolic and search based, which are widely used in automated test generation.Concolic testing was used in paper 2 and 3 while AVM (Alternating Variable Method from Search Based test generation) was used in paper 1.

##### References 
1. [Automated Test Data Generation for Coverage: Haven’t We Solved This Problem Yet?]http://ieeexplore.ieee.org.prox.lib.ncsu.edu/stamp/stamp.jsp?tp=&arnumber=5381642)