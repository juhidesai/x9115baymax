## Reading Homework 9
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
Suresh Thummalapenta , K. Vasanta Lakshmi , Saurabh Sinha , Nishant Sinha , Satish Chandra, Guided test generation for web applications, Proceedings of the 2013 International Conference on Software Engineering, May 18-26, 2013, San Francisco, CA, USA   

##### ii. Keywords and Definitions  
<b>ii1. URL-based equivalence </b> 
Two applications states are URL-based equivalence if their base URL (URL excluding form parameters and sessionIDs) are same.

<b>ii2. Container-based Equivalence</b> 
If two application states are URL-equivalent and include same set of visible container elements such as div and form then they are Container-based equivalent.

<b>ii3. Clickable-based Equivalence</b>
If two application states are Container-based equivalent and contains same set of clickable elements then they are Clickable-based equivalent. 

 
<b>ii4. Element-based Equivalence</b>   
If two application states are Clickable equivalence and includes same set of editable elements like textbox with same values then they are Element-based equivalent.

##### iii. Brief Notes
<b> iii1. Motivational Statements</b> 
Traditional Functional testing is primarily based on the requirement specification documentation and is performed in series of time-consuming steps which are error prone to human lapses. Therefore, goal of this paper is to automate the process of functional testing in enterprise level by discovering interesting behaviour from amaong possible infinite set of behaviours. 

<b> iii2. Hypotheses</b> 
This technique is better than earlier undirected technique for covering buisness rules and generating its corresponding test cases. It is less subject to error and much faster than the traditional functional testing tenchiques. 

<b> iii3. Study Instrument </b>
The author conducted two emperical evalution using WATEG (Web Application Test Generator - prototype tool developed by author) on 5 open source projects. In first study WATEG's effectiveness in covering test cases was compared to two other techniques. And ,in the second study the effectiveness of these three techniques were investegated.

<b> iii4. Future Work </b>
The approach presented in the paper only takes into account business rules which are similar to business-rules manaement systems. In future authors would like to take into account complex transaction-oriented rules that requires more sophisticated modeling.

##### iv. Three ways the paper could be improved.

<b> iv1.</b> This paper soley depended upon the presence of business rules and it can only be part of smaller fraction of application. Thus, this approach alone cannot be applied to many other domains so, paper should identify and complementary techniques for better effectiveness.

<b> iv2.</b> This only takes user's perspective into account, it should also take into account some documentation for well guided approach and buisness rules. 

<b> iv3.</b> It operated on smaller set of open source project, given many large scale availble solutions and high performance computing, this approach should be evaluted on many large scale open source solutions.


##### v. Walking forward in time
This paper builds upon the Read 7 that also takes into account the users perspective for develping test cases. And, it seems that this approach can be one of an effective way of generating test cases from user's perspective to save time and avoid human error. However, it has been noted earlier that it should complement other testing techniques as these would be insufficient alone for variated domains. 

##### References 
1. [Guided test generation for web applications.](http://dl.acm.org/citation.cfm?id=2486810)
