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


#4.6. Defining Functions

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()

fib(2000)

f=fib

f(100)

fib(0)   #无输出

print(fib(0))  #输出None

def fib2(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result
f100=fib2(100) #call it
f100   #write the result

#4.7. More on Defining Functions
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok=input(prompt)
        if ok in('y','ye','yes'):
            return True
        if ok in('n','no','nop','nope'):
            return False
        retries=retries-1
        if retries < 0:
            raise ValueError('invalid use reponse')
        print(reminder)

ask_ok('plese input you choice:')
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


#The default values are evaluated at the point of function definition in the defining scope
i=5

def f(arg=i):
    print(arg)

i=6
f()

# It will print 5

# Important warning: The default value is evaluated only once. 
# This makes a difference when the default is a mutable object such as a list, 
# dictionary, or instances of most classes. For example, 
# the following function accumulates the arguments passed to it on subsequent calls:

def f(a,L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#4.7.2. Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("--lovely plumage, the", type)
    print("--It's", state, "!")
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# but all the following calls would be invalid:

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument

# when **name is present, it receives a dictionary;
#*name must occur before **name
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# pay attention to the comma between the parameters        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's really very,very, VERY runny, sir.",
           "It's really very, very, very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch",
           LuRenJia='A',
           LuRenYi='B')

# 4.7.3. Arbitrary Argument Lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

#----------------
def concat(*args, sep='/'):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

#4.7.4. Unpacking Argument Lists
args=[3,6]
list(range(*args))

# 4.7.5. Lambda Expressions
# first use --- easy

def make_incrementor(n):
    return lambda x:x+n

f=make_incrementor(42)
f(0)
f(1)

# The above example uses a lambda expression to return a function. 

#2 second use. difficult!!!
# Another use is to pass a small function as an argument:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

# 4.7.6. Documentation Strings
def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
