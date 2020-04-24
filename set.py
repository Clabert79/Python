s0 = set()
print(type(s0))
s1 = set([1, 'ciao', 2, ('a','b')])
print(type(s1))
s2 = {1, 'py', ('a','b'), 3}
print(type(s2))
# set un oggetto mutabile
s0.add(4) 
print(s0)
# ma gli oggetti all'interno no mutabili
# s0.add([1,2]) NO

s2.add('py') # non aggiunge duplicati
print(s2)
for item in s2:
	print(item)

print("Len: " + str(len(s2)))

#intersezione

print({'a', 'b', 'c', 'd'} & {'a', 'c', 'e'}) # 'a' ,'c'

#unione

print({'a', 'b', 'c', 'd'} | {'a', 'c', 'e'}) # 'a' ,'c', 'b', 'e', 'd'

#differenza
print({'a', 'b', 'c', 'd'} - {'a', 'c', 'e'}) # 'b' ,'d'

#differenza simmentrica
print({'a', 'b', 'c', 'd'} ^ {'a', 'c', 'e'}) # 'b' , 'e', 'd'

