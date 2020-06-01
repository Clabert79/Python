def foo1(a, b, c=3, d=4):
	print(a, b, c, d, sep='|')

foo1("primo",d="quarto",b="secondo")
# comportamento da tenere a mente nelle funzioni 
# il parametro di default è sempre lo stesso 
# quindi se sono oggetti mutabili verranno modificati semore gli stessi
def foo2(a=[1, 2, 3]):
	a.append(100)
	print(a)

foo2()
foo2()

def foo3(arg=None, value=0):
	arg=[] if arg == None else arg
	arg.append(value)
	return arg

print(foo3())
print(foo3())
print(foo3([1]))
print(foo3())

def foo4(*varargs):
	for element in varargs:
		print(element)

foo4('a', 'b', 'c', 'd', 'e')
foo4(1, 2, 3, 4, 5)

def foo5(a, b, c):
	print(a, b, c)

# se il numero degli elementi nell'oggeto iterabile 
# è = al numero di parametri viene spacchettato 
foo5(*[11, 22, 33])

def foo6(*varargs):
	for arg in varargs:
		print(arg, end='')

foo6(*range(4))
foo6(*range(5))

# trasforma i parametri in dizionario 
# (sempre in coda agli altri eventuali parametri)
def foo7(**kwargs):
	print(kwargs)

foo7()
foo7(a=1,c=22,e=333,z=7)

def foo8(a,*,b=3):
	print(a,b)

foo8('Python' ,b='2')
foo8('Python')

# equivalente
def foo9(a, **kwargs):
	b = kwargs.get('b',3) # se non esiste mette il default
	print(a,b)

foo9('Python' ,b='2')
foo9('Python')

def foo10(a, b, c):
	print(a, b, c)

foo10(**{'b':22, 'a':11, 'c':33})

# possiamo disenteressarci del numero dei parametri 
# (le chiavi devono essere stringe)

def foo11(**kwargs):
	for k, v in kwargs.items():
		print(k,v)

foo11(**{'nome':'pippo', 'anno':1985})

def say_hello(name='Darth Vader', side='sith'):
	print(f'hello {name} {side}')

say_hello()
say_hello("darth Maul")

say_hello('Yoda','jedi')
say_hello('sinth','duko')
say_hello(side='jedi',name='luke')
