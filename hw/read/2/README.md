## Reading Homework 2
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
Shay Artzi, Adam Kiezun, Julian Dolby, Frank Tip, Danny Dig, Amit Paradkar, Senior Member, IEEE, and Michael D. Ernst. 2010  
Finding Bugs in Web Applications Using Dynamic Test Generation and Explicit-State Model Checking (IEEE Transactions on Software Engineering, v.36 n.4, p.474-494, July 2010)  

#####ii. Keywords and Definitions  
<b>ii1. Execution failures</b>  
These are the crashes or warnings in the program.  

<b> ii2. HTML failures</b>  
These occur  when there is malformed HTML in the output.  

<b> ii3. Dynamic web applications</b>  
Dynamic web applications are applications that generate web pages during execution.  

<b> ii4. Concolic testing</b>  
Concolic testing is a hybrid software verification technique that performs symbolic execution (program variables as symbolic variables) along a concrete execution (testing on particular inputs) path. Symbolic execution is used in conjunction with a constraint solver to generate new test cases.   

##### iii. Brief notes  
<b> iii1. Motivational Statements</b>  
Dynamically generated web pages pose a problem of frequent web script crashes and malformed HTML pages that impacts the usability of the web application. Thus the validation and testing tools are limited in functionality to handle dynamically generated pages. The authors proposes the extension of dynamic test generation to web domain that works on the lines of dynamic test generation tools such as DART, Cute and EXE.    

<b> iii2. Hypotheses</b>  
Based on the limitation of existing tools in the market and their limited functionality, the authors proposed a tool called Apollo, that generates dynamic tests for dynamic web applications by combining concrete and symbolic executions an explicit-state model checking for PHP language. And suggests that the tool minimizes the size of failure inducing inputs and attains over 50% line coverage.  

<b> iii3. Commentry</b>  
The authors of the paper developed their own tool Apollo described in above section. The Apollo based test generation is able to achieve over 50% coverage, and found a total of 675 faults in 6 open source PHP applications, out of which 72 are execution problems and 601 are cases of malformed HTML. Additionally it minimizes failure inducing inputs by up to 5.3 times (compared to unminimized ones).  

<b> iii4. Anti-patterns</b>  
Actions performed by JavaScript are not yet analyzed by Apollo. And it has limited tracking ability in the realm of Native methods implemented in C and through database (as it cannot explore call sequences dependent on earlier calls).  

##### iv. Three ways the paper could be improved.  
<b> iv1. No guarantee of completeness</b>  
There is no guarantee of completeness both in code coverage as well as the bugs found. This is a major letdown if this process is to used as the only test generation tool. Having a partial test generation is more cumbersome because of the  possibility of having duplicate tests or maybe even having some tests missed. If the authors can give a guaranteed threshold to  which the tool can conform to, it would be more usable.  

<b> iv2. Avoid using one user for database connection</b>  
They should avoid using just one user for DB connection. They say they can’t use static or dynamic analysis for determining users and passwords, which is not true if the tool is used for testing in the SDLC process. Having a single user may not be able to fetch all code branches if he does not have the right privilege to access that resource, the same is true for an admin user because that would not check code containing conditions when the user does not have the proper privilege. They can have predetermined users with various roles and privileges for help in this.  

<b> iv3. Not use HTML Validator</b>  
Use of a HTML validator may not give an accurate result if the already existing HTML code does not have all required elements seen in an HTML validator. The point here is that if the existing HTML itself is not conforming to HTML standards, the dynamically generated ones will also not conform to the same, giving a false impression that the dynamically generated HTML is malformed.  


##### v. Connection to [paper one](http://dl.acm.org/citation.cfm?id=2190141).   
Our earlier paper (which actually got published after this paper and refers this paper) and this paper have many commonalities. Both the papers aimed at generating test cases for PHP and produced a number of test cases. Authors of both the papers have developed their own tool/automated oracle (Apollo and SWAT) for evaluation. However, paper one focuses more on branch coverage using Dynamically Mined Values seeding, Static Constant seeding, and Near Miss Seeding approach, whereas this paper focuses more on statement coverage by combining concrete and symbolic execution and explicit state model checking.  


##### References  
1. [Finding Bugs in Web Applications Using Dynamic Test Generation and Explicit-State Model Checking, 2010.](http://dl.acm.org/citation.cfm?id=1850611)
2. [Concolic testing](https://en.wikipedia.org/wiki/Concolic_testing)  
