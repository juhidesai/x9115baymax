## Reading Homework 4
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
William G.J. Halfond, Saswat Anand, and Alessandro Orso. 2009. Precise interface identification to improve testing and analysis of web applications. Proceedings of the eighteenth international symposium on Software testing and analysis (ISSTA '09). ACM, New York, NY, USA.  

##### ii. Keywords and Definitions  
<b>ii1. Interface Identification</b> 
 It is the technique of identifying the interfaces which are used in a program. Interfaces can be seen as entry points to the application which would spit out dynamic content based on inputs.

<b>ii2. Penetration testing</b> 
 It is a process in which the application is tested against malicious attacks in order to reveal security vulnerabilities.  

<b>ii3. Precision</b> 
 It is the accuracy of the entity in question of doing the work that it is supposed to perform.  
 
<b>ii4. Web crawling</b>   
It is a process in which a ‘Spider’(automated program/crawler) is used to visit all the links (Web pages) which are connected in a depth first search technique. The search starts from a few seed pages which are given to the crawler program.  

##### iii. Brief Notes
<b> iii1. Motivational Statements</b> 
Web application has grown complex and sophisticated because they generate dynamic and customized content. The component of dynamic web applications communicate extensively interfaces which makes their accurate identification an important part of quality assurance.  

<b> iii2. Hypotheses</b> 
This paper proposes a new approach for interface identification based on symbolic execution which author proposes achieves higher precision and accuracy of quality assurance.  

<b> iii3. Related Work </b>
Earlier approaches depended on developer-provided interface like UML models, Finite State Machine etc. Other groups used dynamic analysis, web-crawling. Some used Static analysis to identify interfaces, and recent ones used concolic execution.  

<b> iii4. Baseline Results </b>
Author compares the result of this new technique (WAM-SE) against other interface identification techniques - WAM-DF, SPIDER and DFW in terms of Anlysis of time, precision, usefulness on four commercial Java-based web applications - Bookstore, Classifieds, Employee Directory and Events.  


##### iv. Three ways the paper could be improved.

<b> iv1.</b> Constraints which include complex operations( matching regular expressions etc) should also be dealt with in the symbolic execution.  

<b> iv2.</b> The technique should also be compared against manual specifications as manual specifications are also widely used and this comparison would be a good measure of practicality as well as community adoption for this technique.  

<b> iv3.</b> The number of applications on which the study is based should be increased. If not, then the variety among the chosen applications should be improved..  


##### v. Connection to [paper one](http://dl.acm.org/citation.cfm?id=2190141). 
The first paper implemented a tool for automated web application testing. This paper goes a step further in the same direction by making the input given to the automated tester better. This paper particularly focuses on identifying interfaces in the application. A direct effect of this increased accuracy is an increase in better test coverage and accuracy.  

##### References 
1. [Precise interface identification to improve testing and analysis of web applications.](http://dl.acm.org/citation.cfm?id=1572305)