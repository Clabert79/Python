from functools import reduce


#1 Capitalize all of the pet names and print the list

my_pets = ['sissi', 'bib', 'titti', 'pippo']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 list into a list of tuples, but sort thr numbers from lowest of highest

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))

#4 Combine all of numbers that are in a list on this file using reduce

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))
