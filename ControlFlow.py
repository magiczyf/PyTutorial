# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#4.2 for statements
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w)>6:
        words.insert(0,w)
words

# The range function
range(5,10)
range(0,10,3)
range(-10,-100,-30)

for i in range(5,10):
    print(i)
 
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])

print(range(10))

list(range(5))    

#4.4. break and continue Statements, and else Clauses on Loops    
for n in range(2, 10):
         for x in range(2, n):
             if n % x == 0:
                 print(n, 'equals', x, '*', n//x)
                 break
         else:
         # loop fell through without finding a factor
             print(n, 'is a prime number')

for num in range(2,10):
    if num%2==0:
        print("Found an even number",num)
        continue
    print("Found a number",num)
             
#4.5. pass Statements
class MyEmptyClass():
    pass

    def initlog(*args):
        print(*args)
    
MyEmptyClass.initlog('aaaaaaaaaaaaaa')
