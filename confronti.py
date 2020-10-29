formaggi_1 = ['Cheddar', 'Edam', 'Gauda']
formaggi_2 =['Cheddar', 'Edam', 'Gauda']

print(formaggi_1 == formaggi_2)
print(formaggi_1 is formaggi_2)

formaggi_3 = [ 'Edam', 'Gauda', 'Cheddar']

print(formaggi_1 == formaggi_3)

print('Cheddar' in formaggi_2)

import functools

l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 50, 40, 70]
l3 = [50, 40, 30, 20, 10]

if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,l1,l2), True):
    print ("The lists l1 and l2 are the same")
else:
    print ("The lists l1 and l2 are not the same")

if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,l1,l3), True):
    print ("The lists l1 and l3 are the same")
else:
    print ("The lists l1 and l3 are not the same")

import collections

if collections.Counter(l1) == collections.Counter(l2):
	print("List 1 is the same list 2")
else:
	print("List 1 is not the same list 2")

if collections.Counter(l1) == collections.Counter(l3):
	print("List 1 is the same list 3")
else:
	print("List 1 is not the same list 3")

l1.sort()
l2.sort()
l3.sort()

if l1 == l3:
	print("List 1 is the same list 3")
else:
	print("List 1 is not the same list 2")

# -----------------------------------------------------------
print(any(letter == 't' for letter in 'monty' ))
