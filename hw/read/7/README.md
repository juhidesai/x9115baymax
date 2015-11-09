## Reading Homework 7
#####Group Members:
Juhi Desai (jddesai)  
Rohit Arora (rarora4)  
Ronak Nisher (rpnisher)  

##### i. Paper Details
Nadia Alshahwan , Mark Harman, Augmenting test suites effectiveness by increasing output diversity, Proceedings of the 34th International Conference on Software Engineering, June 02-09, 2012, Zurich, Switzerland   

##### ii. Keywords and Definitions  
<b>ii1. Content</b> 
 Textual data that is presented to the user, it is mainly the data user has requested and is presented in HTML format.

<b>ii2. HTML Code</b> 
 It is the code that defines look and feel of the code, how a web HTML page shoul be contructed using tags.

<b>ii3. Output is OU-All Unique</b> 
 When a new output page is displayed and there is difference in any element on the new page compared to previous one categorize the new page as unique.
 
<b>ii4. Output is OU-Strict Unique</b>   
This is simillar to OU-All Unique except that is eliminates the 'potential infinite output' issue. In this HTML page is stripped of any text or embedded values only opening and closing tags are taken into account to eliminate variations caused due to default values, style or font settings.

##### iii. Brief Notes
<b> iii1. Motivational Statements</b> 
Program outputs are provides valueable resource for identifying unexpected program behaviour and are critical from user's point of view.

<b> iii2. Hypotheses</b> 
The paper proposes that output uniqueness can compliment traditional coverage criteria and can make test suites more effective at exposing faults. 

<b> iii3. Baseline Results </b>
The approach proposed by the author is compared to the random augmentation	in fault finding ability and is found to outperform it by 280% in 5 medium-sized, real world applications.

<b> iii4. Future Work </b>
To define output uniquness for more complex applications, such as outputs that are ranges, or data types. Another aspect is to combine white-box coverage with the output uniqness.

##### iv. Three ways the paper could be improved.

<b> iv1.</b> Scope of the paper is very limited, i.e. paper took into account output in terms of HTML, however not all applications are HTML based such as WPF, or XML parsing etc, those should be taken into account as these augment HTML.

<b> iv2.</b> It would have been better to relate input and output uniqueness and not just output uniqueness.  

<b> iv3.</b> It  Given availability of many open sour projects, it would have been effective to try this technique on new popular open source projects by fetching their initial commits and running tests on them and comparing them with later findings.  


##### v. Walking forward in time
This paper introduces a whole new aspect of testing, that can completement existing test suits. This new perspective also uses mutation techniques that are used for autmated test case generation, however this techniques tries to acomplisht he same form user's point of view of taking output into account.  

##### References 
1. [Augmenting Test Suites Effectiveness by Increasing Output Diversity.](http://dl.acm.org/citation.cfm?id=2337414)
