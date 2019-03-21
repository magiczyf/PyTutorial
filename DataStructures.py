# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 07:47:51 2019

@author: zyf
"""

# 5.1. More on Lists

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()

# 5.1.1. Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack.pop()
stack

# 5.1.2. Using Lists as Queues
#  use collections.deque which was designed to have fast appends and pops from both ends

from collections  import deque
queue = deque (["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.pop()
queue

# 5.1.3. List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
squares

squares1 = list(map(lambda x: x**2, range(10)))
squares1

squares2 = [x**2 for x in range(10)]
squares2



[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
combs


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
# filter the list to exclude negative numbers
[x for x in vec if x>=0]



# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = ['banana', '  loganberry  ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]


# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

vec1 = [[[1,2],[3, 4]], [[5,6], [7,8]]]
[num for elem in vec1 for num in elem]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]





# learned but lost because of the software collapse...




# 5.6. Looping Techniques

# When looping through dictionaries, the key and corresponding value
# can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding
# value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time,
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence
# in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)


# To loop over a sequence in sorted order, use the sorted() function
# which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket):
    print(f)

for f in sorted(set(basket)):
    print(f)

basket

# It is sometimes tempting to change a list while you are looping over it;
# however, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
# 5.7. More on Conditions
# A and not B or C is equivalent to (A and (not B)) or C





#The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.
#
#It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,
#
#>>>
#>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
#>>> non_null = string1 or string2 or string3
#>>> non_null
#'Trondheim'


# 5.8. Comparing Sequences and Other Types
# Toooooo dificult to understand...



