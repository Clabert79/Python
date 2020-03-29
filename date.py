import datetime

t = datetime.time(1,2,3)
t1 = datetime.time(1,2,3)

print(t)
print('Ora: ' + str(t.hour))
print('Minuti: ' + str(t.minute))
print('Secondi: ' + str(t.second))


if t == t1:
	print("uguali")
else:
	print("diversi")

t = "pippo"
t1 = "pippo"

if t == t1:
	print("uguali")
else:
	print("diversi")

## differenze tra == e is

a = {1:2}
b = a
print(a is b)
print(a == b)

c = {1:2}

print(a is c) # false	
print(a == c)

print(bool((1, 2) and 'python' and {1:'uno'}))

print(bool((1, 2) and '' and {1:'uno'}))

# a terminale funziona
# *sa1, b1, c1 = 'python' 
#print(a1)  ['p', 'y', 't', 'h']
#print(b1) 'o'
#print(c1) 'n'

# *a, b, c = [1, 2, 3]
# print(a,b,c) ([1], 2, 3)
# *a, b, c, d = [1, 2, 3]
# print(a, b, c, d)([], 1, 2, 3)

print('yth' in 'python')
print((1, 2) in ['a', 'b', (1, 2)])

print('name' in {'age': 33, 'name': 'Beppe'}) # 'name' appartiene alle chiavi?
print( 'Beppe' in {'age': 33, 'name': 'Beppe'})# 'Beppe' appartiene alle chiavi?

for j in[('a','b'),'pyhton']:
	print(j)
		
ordinato = sorted([(1, 2, 3), 'pyhnn', {'quattro':4, 'cinque':5}], key=len, reverse = True)

print(ordinato)

for i in map(bin, [2, 3, 4]):
	print(i)

def product(x,y):
	return x * y

print(product(3,6))


