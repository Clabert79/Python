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
