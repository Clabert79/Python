
def min_max(t):
	return min(t), max(t)
def stampa_tutti(*args):
	print(args)
def corrispondenza_totale(t1,vt2):
	print(zip(t1, t2))
	for x,y in zip(t1, t2):
		print("x:" + str(t1) + " y:" + str(t2))
		if  x == y:
			return True

	return False


my_tuple = (1, 2, 3, 4, 5, 6)
# sono immutabili
# my_tuple[1] = 'z' genera un errore
print(my_tuple[1])
print(5 in my_tuple)
print(my_tuple.index(4))
print(my_tuple.count(5))


## x1, y1, z1, *other = (1, 2, 3, 4, 5, 6) da capire perchè non funzione
# print(z1)
# print(other)


indirizzo = 'pippo@gmail.com'
nome, dominio = indirizzo.split("@")
print(nome + " " + dominio)
a, b = nome, dominio
print(a + " - "+ b)
quoziente, resto = divmod(7, 3)
print(str(quoziente) + "  " + str(resto))
t1 = divmod(97, 3)
print(min_max(t1))

stampa_tutti(1, 2.0, '3')
t2 = (7, 3)
divmod(*t2)

s = 'abc'
t3 = [0, 1, 2]
for coppia in zip(s,t3):
	print(coppia)

print(list(zip(s,t3)))

tupla1 = (1, 7, 3)
tupla2 = (1, 7, 5)
print(corrispondenza_totale(tupla1, tupla2))

print(list(zip('Anna', 'Edo')))
for indice, elemento in enumerate('ABCD'):
	print(indice, elemento)

diz1 = dict(zip('abcd',range(4)))
print(diz1)



from collections import namedtuple
Point = namedtuple('MyPoint', ['x', 'y', 'z'])
p = Point(10, 20, 30)
print(p)
print(p._fields)
print(p.x, p.z, p.y)
