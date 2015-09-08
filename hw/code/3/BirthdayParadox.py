from __future__ import division
from random import randint

def has_duplicate(elements):
    length = len(elements)
    count = 1
    for i in elements:
        if i in elements[count:length]:
            return True
        count+=1
    return False
        
### print has_duplicate([2,3,4,5,1])

def generate_birthdays(n):
    birth_days = []
    for birthday in range(n):
        birth_days.append(randint(1,365))
    return birth_days
    
### print generate_birthdays(100)

def check_birthday_probability(n):
    true_count = 0
    for i in range(365):
        if has_duplicate(generate_birthdays(n)):
            true_count += 1
    probablity = true_count*100/365
    print "Probability of",n,"birthdays occuring together in 365 days is: %.2f %%" % probablity
    
check_birthday_probability(23)