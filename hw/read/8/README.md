## Reading Homework 7
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
Nadia Alshahwan , Mark Harman, Coverage and fault detection of the output-uniqueness test selection criteria, Proceedings of the 2014 International Symposium on Software Testing and Analysis, July 21-25, 2014, San Jose, CA, USA 

##### ii. Keywords and Definitions  
<b>ii1. Output is OU-Hidden</b> 
Hidden variables can ead to a large number of variables which may correspond to number of items in the database. It it therefore useful to consider characterstics of hidden form rather than its value while finding output uniqueness.
 
<b>ii2. Output is OU-Subtype</b>   
Based on the definition of OU-Hidden, we extract the notion of usbtypes of Hidden Form which can be positive, negative, strings, zeros, ampty etc. In this value of the hidden field is replaced with the corresponding subtype (like num, string etc.)

<b>ii3. Output is OU-Seq</b>   
It is the structure of HTML that is stripped of any text or embedded values, incluing hidden fields, only opening and closing tags are considered.

<b>ii3. Output is OU-Text</b>   
This definition of output uniqueness focusses on the output text of the HTML page. It may be the case that some text on eveyr page is same therefore, it can be ignored for mutation and tester can pay attention to other page text outputs.

##### iii. Brief Notes
<b> iii1. Motivational Statements</b> 
This study is basically motivated form the fact that achieving high structural whitebox coverage may leave many faults undetected. And studies have indicated that there is a need for additional notion of test adequacy  and coverage.

<b> iii2. Hypotheses</b> 
Output uniqness exhibits very high average correlation coefficients with statement, branch, and path coverage. Therefore, Output uniqness provide a useful surrogate when whitebox techniques are  inapplicable.

<b> iii3. Study Instruments  </b> 
The author used Xdebug to record statement coverage, however it cannot be used for branch and path coverage, therefore applications' code was instrumented to produce execution traces that can be used to measure branch and path coverage.

<b> iii4. Baseline Results </b>
The author of the paper compares the results of the output uniqueness with the faults found using white-box testing that did not employ output uniqness and found that faults found along with output uniqness were 92% of the real faults found by branch coverage out of which 47% remained undetected by whitebox technique.

##### iv. Three ways the paper could be improved.

<b> iv1.</b> Scope of the paper is very limited, i.e. paper took into account output in terms of HTML, however not all applications are HTML based such as WPF, or XML parsing etc, those should be taken into account as these augment HTML.

<b> iv2.</b> It would have been better to relate input and output uniqueness and not just output uniqueness.  

<b> iv3.</b> IT should operate on applications or suggests application domains in which Output uniquness operation can be signification in independently identifying the faults. 


##### v. Walking forward in time
This paper builds upon one of the previous papers (by same authors) by implementing one of their future scope and explores its effectivness, and finds its compatiability and correlation with whitebox testing. However, testing domain is not just about black-box or whitebox testing its a very big domain and I feel those considerations should also be taken into account.  

##### References 
1. [Coverage and fault detection of the output-uniqueness test selection criteria.](http://dl.acm.org/citation.cfm?id=2610413)
