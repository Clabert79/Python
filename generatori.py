def wondrous(n):
	""" Resstituisci una lista di numeri HOTPO, a partire da n"""
	my_list = []
	while n!=1:
		my_list.append(n)
		n = n//2 if n%2 == 0 else 3*n + 1

	else:
		my_list.append(1)
	
	return my_list

for i in wondrous(5):
	print(i)
	
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def conteggio(n):
	i = 0
	while i <= n:
		yield i
		i += 1
for i in conteggio(10):
	print(i)

lista = list(conteggio(5))
print(lista)

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
def foo(seq):
	print("inizia l'esequzione ...")
	for item in seq:
		yield item
		print(item)

g = foo('a1cd')
print(type(g))

g.__next__()
g.__next__()

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def g_wondrous(n):
	""" generatore di numeri HOTPO, a partire da N """
	while n!=1:
		yield n
		n = n // 2 if n% 2 == 0 else 3 * n + 1
	else:
		yield 1

g1 = g_wondrous(5)

print(g1.__next__())
print(g1.__next__())
print(g1.__next__())
g1.__next__()
print(g1.__next__())
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("genearator expression")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
my_list = [1, 3, 6]
a = (x**2 for x in my_list) ## genearator expressiona = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))



print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("Coroutine")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def c_foo():
	print("Inizia esecuzione del codice ...")
	while True:
		x = (yield)
		print(x)
		print("termina esecuzione")

c = c_foo()
print(c)
c.__next__()
c.send('Python')
c.send(1)

c.close()

def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    while True: 
        name = (yield) 
        if prefix in name: 
            print(name) 

corou = print_name("Dear") 
corou.__next__() ## ci deve essere se no va in errore
corou.send("Atul") 
corou.send("Dear Atul")


