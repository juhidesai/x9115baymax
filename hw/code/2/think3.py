### Exercise 1: Move the last line of this program to the top, 
### so the function call appears before the definitions. 
### Run the program and see what error message you get.

"""
repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
     
"""

### Exercise 2: Move the function call back to the bottom 
### and move the definition of print_lyrics after the 
### definition of repeat_lyrics. What happens when you run this program?

"""
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
     
repeat_lyrics()
"""


### Exercise 3: Python provides a built-in function called len that returns the length of a string, 
### so the value of len('allen') is 5.

### Write a function named right_justify that takes a string named s as a parameter and 
### prints the string with enough leading spaces so that the last letter of the string 
### is in column 70 of the display.

### >>> right_justify('allen')

"""
def right_justify(input_str):
    str_len = len(input_str)
    leading_spaces = 70 - str_len
    print " "*leading_spaces + input_str
    
right_justify("Rohit Arora")
"""

### Exercise 4: A function object is a value you can assign to a variable or pass as an argument. 
### For example, do_twice is a function that takes a function object as an argument and calls it twice:

### def do_twice(f):
###    f()
###    f()

### Here's an example that uses do_twice to call a function named print_spam twice.

### def print_spam():
###     print 'spam'

### do_twice(print_spam)

###    1. Type this example into a script and test it.
###    2. Modify do_twice so that it takes two arguments, a function object and a value, 
###    and calls the function twice, passing the value as an argument.
###    3. Write a more general version of print_spam, called print_twice, 
###    that takes a string as a parameter and prints it twice.
###    4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
###    5. Define a new function called do_four that takes a function object and a value and calls the function four times, 
###    passing the value as a parameter. There should be only two statements in the body of this function, not four.

""" 
def do_twice(f,v):
    f(v)
    f(v)
    
def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)
    
def print_twice(value):
    print value
    print value

do_twice(print_twice, 'spam')

do_four(print_twice, 'spam_new')

"""

### Exercise 5: This exercise can be done using only the statements and other features we have learned so far.

### Write a function that draws a grid like the following:

### + - - - - + - - - - +
### |         |         |
### |         |         |
### |         |         |
### |         |         |
### + - - - - + - - - - +
### |         |         |
### |         |         |
### |         |         |
### |         |         |
### + - - - - + - - - - +

### Hint: to print more than one value on a line, you can print a comma-separated sequence:

### print '+', '-'

### If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.

### print '+', 
### print '-'

### The output of these statements is '+ -'.

### A print statement all by itself ends the current line and goes to the next line.
### Write a function that draws a similar grid with four rows and four columns.

def do_twice(f,n,x):
    f(n,x)
    f(n,x)
    
def do_four(f,n,x):
    do_twice(f,n,x)
    do_twice(f,n,x)
    
def print_plus_hypen(n,x):
    print '+'+' -'*n,
    
def print_post_space(n,x):
    print '|'+'  '*n,

def print_top(n,x):
    if x == 2:
        do_twice(print_plus_hypen,n,0)
    else:
        do_four(print_plus_hypen,n,0)
    print '+'

def print_body(n,x):
    if x == 2:
        do_twice(print_post_space,n,0)
    else:
        do_four(print_post_space,n,0)
    print '|'
    
def print_plus_hyphen_post(n,x):
    print_top(n,x)
    do_four(print_body,n,x)
    
def print_grid():
    do_twice(print_plus_hyphen_post,4,2)
    print_top(4,2)
    
def print_grid_big():
    do_four(print_plus_hyphen_post,4,4)
    print_top(4,4)

print_grid()

print_grid_big()