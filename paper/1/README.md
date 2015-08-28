## Reading Homework 1
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
Nadia Alshahwan and Mark Harman. 2011  
Automated Web Application Testing Using Search Based Software Engineering  (Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering)

#####ii. Keywords and Definitions  
<b>ii1. Automated software testing</b>  
It is a process in which the testing of the software is automated. This means that you will no longer have to manually write tests or find test cases, the software will do that for you and also run the tests for you.  

<b> ii2. Search based software engineering</b>  
It is a technique wherein we apply search based metaheuristic techniques like optimization, genetic algorithms to software engineering.

<b> ii3. Dynamically mined value(DMV) seeding</b>  
It is the process in which seed values are generated dynamically with the help of the HTML which is generated. For example, Form data (selection boxes etc) can be a good source of values which can be used as a seed to cover more/valid branch paths.

<b> ii4. Search based web application tester (SWAT)</b>  
It is a tool developed by the authors to implement their Search Based Software Engineering model on real world applications.

##### iii. Brief notes  
<b> iii1. Motivational Statements</b>  
Authors explain that increase in the number of internet users and their reliance on web-application mandates the use of automated web application testing to ensure their continual and fast availability, by relying less on manual, labour intensive and slow testing process. Moreover, inadequate testing can have a major impact on the business's customer base and loyalty, thus it is imperative to use Search-based software testing, which has historically been widely used for standalone applications, to automate test data generation.  

Authors also note that out of 399 research papers on SBST, only one talks about its applicability in web applications and none of it ever applies SBST for test data generation in web application to automate web application testing.  

<b> iii2. Hypotheses</b>  
Authors claim that the 3 algorithms defined in this paper boost the efficiency and effectiveness of SBST. The algorithms defined exploit both static as well as dynamic analysis. They also developed a tool, SWAT, which uses these algorithms for automated web application testing. They achieved a 54% increase in branch coverage and a 30% decrease in test effort.

<b> iii3. Study Instruments</b>  
Authors implemented three versions of the tool SWAT, utilizing three different algorithms - Near Miss Seeding (NMS), Static Constant Seeding (SCS) and Dynamically Mined Value Seeding (DMV).They used a fitness function to evaluate the effect of each algorithm. These three enhancements (algorithms) were compared on the basis of theie branch coverage, efficiency and fault finding ability.

<b> iii4. Sampling procedures</b>  
The authors conducted the experiment on 6 different PHP applications of sizes ranging from small to medium. They ran all 3 versions of their tool on each of the 6 applications 30 times. These applications were the ones used in other research on web testing, which did not use SBST. 

##### iv. Three ways the paper could be improved.  
<b> iv1. Support more languages</b>  
Currently, their tool supports only PHP, and considering it is one of the most widely used web technologies, that is fine, but there are a lot of web applications based on other web technologies too, and support for other languages will make this tool more widely usable.  

<b> iv2. Remove manual work</b>  
Their analysis phase involves manual inference of input types. Automating this part might not be that easy, but it will go a long way towards making the system more robust. Also, not all data types are currently supported by the system. This seems to be a pretty big disadvantage. 

<b> iv3. Create Dummy User for Testing</b>  
For systems that need login information, the username and password needs to be provided by the user and entered into the tool. This is adding one more manual step to the process. Maybe they could create a dummy user for testing purposes and this creation will by default test the Register or Sign Up functionality too.  


##### References  
1. [Automated Web Application Testing Using Search Based Software Engineering, 2011.](http://dl.acm.org/citation.cfm?id=2190141)
