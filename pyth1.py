import string

def items(x, depth=-1):
  if isinstance(x,(list,tuple)):
    for y in x:
      for z in items(y, depth+1):
         yield z
  else:
    yield x

out = [x if x > 20 else 0 for x in items(  [10,[ 20,30], 40,[(50,60,70),[80,90,100],110]])]
print out

def display(text):
    str = [char for char in text if char not in string.whitespace]
    print ''.join(str)
    
display("This is a text")

def lines(string):
  a =[]
  tmp=''
  for ch in string:
    if ch == "\n":
        if len(tmp) > 20 and tmp:
            a += ''.join(tmp)
        tmp = ' '
    else:
        tmp += ch
  
  if len(tmp) > 20 and tmp:
        a += tmp
  return a
    
inp = ["this is a multiline code\n\n\n    \nhjjkkuummjmjmjmjmjmjmjmjmyeah.","","","Hello","\n\n","aaaaaaaaaaaaaaaaaaaaaaaaaa"]
a = [lines(line) for line in inp if lines(line) is not None]

print str(a)

import random

r = random.random
rseed = random.seed

class Some:
  def __init__(self, max=8): 
    self.n, self.any, self.max = 0,[],max
  def __iadd__(self,x):
    self.n += 1
    now = len(self.any)
    if now < self.max:    
      self.any += [x]
    elif r() <= now/float(self.n):
      self.any[ int(r() * now) ]= x 
    return self

p = Some(10)

for i in range(999):
    p+=i
print p.n
print p.any
print p.max

p = [x for x in range(5)]
print p