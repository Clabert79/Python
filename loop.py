# import antigravity

# *args(tutti i parametri in ingresso)  **kwargs(chiave velore)

def super_func(*args, **kwargs):
	print(args)
	print(kwargs)
	total = 0
	for item in kwargs.values():
		total += item
	return sum(args)

print(super_func(1,3,4,5,6, num1 = 7,num2 = 8))
print("----------------------")

my_list = (1,2,3,4,5,6,7)
for item  in my_list:
	# nel caso si verifichi la condizione non esegue il codice seguente
	if(item == 2):
		continue
	# esce dal looop
	if(item == 6):
		break

	print(item)

print("----------------------")

for item  in my_list:
	if(item == 2):
		continue
	if(item == 6):
		break

	print(item)

for number in range(0 , 100):
	print(number)
for _ in range(0, 10, 2):
	print(_)
for _ in range(10, 0, -1):
	print(_)

for i,char in enumerate(list(range(49,55))):
	print(i, char)
	if char == 50:
		print(f'index of range is {i}')

for i, char in enumerate('hello'):
	print(str(i) + ' - ' + char)

i = 0
while i < 20:
	print(i)
	i += 1
	if i > 22:
		break
else:
	print('done with all the work') # viene stampato solo se vengono eseguiti tutti i loop




i1 = 0
while i1 < len(my_list):
	print(my_list[i1])
	i += 1
	break

some_list = ['a', 'b', 'c', 'd', 'f', 'n', 'n', 'a']

duplicate = []

for value in some_list:
	if some_list.count(value) > 1:
		if value not in duplicate:
			duplicate.append(value)

print(duplicate) 


import operator

# notable_dates = [(20, 7 , 1969), (1966),(9, 11, 1989),(11, 1918),(25, 11,1915)]

# notable_dates.sort(key=operator.itemgetter(1)) 



notable_dates = [(20, 7 , 1969), (9, 11, 1989), (25, 11,1915), (11, 1918)]
getcount = operator.itemgetter(-1)

order_notable_dates = sorted(notable_dates, key=getcount)

print(order_notable_dates)

notable_dates_with_zero = [(20, 7 , 1969), (9, 11, 1989), (25, 11,1915), (11, 1918),()]

def last(seq):
	return seq(-1) if seq else 0

## notable_dates_with_zero.sort(key=lambda seq:seq[-1] else 0)
# order_notable_dates_with_zero = sorted(notable_dates_with_zero, key=lambda seq:seq[-1] else 0)

print(notable_dates_with_zero)


iterator = iter(range(5))

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def g_wondrous(n):
	""" generatore di numeri HOTPO, a partire da N """
	while n!=1:
		yield n
		n = n // 2 if n% 2 == 0 else 3 * n + 1
	else:
		yield 1

## prende gli elementi per cui la funzione che passiMO è True
from itertools import dropwhile
for i in dropwhile(lambda num: num < 4,g_wondrous(29)):
	print(i)

