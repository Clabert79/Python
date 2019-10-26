formaggi = ["gorgonzola","fontina","toma"]

for formaggio in formaggi:
	print(formaggio)

for i in range(len(formaggi)):
	# print(formaggi[i])
	print(i)

formaggi.append("scamorza")
#print(formaggi * 3)
print(formaggi[1:3])

def somma_tutti(t):
	totale = 0
	for x in t:
		totale += x
	return totale

da_sommare =[1,2,3]
print(somma_tutti(da_sommare))
print(sum(da_sommare))
def tutte_maiscole(m):
	res = []
	for s in m:
		res.append(s.capitalize())
	return res
print(tutte_maiscole(formaggi))
#cancellazione elemento preciso
t =['a','b','c','d']
x = t.pop(1)
print(t)
t.remove('a')
print(t)
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:4]
print(t)


	