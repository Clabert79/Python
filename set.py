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

s3 = {1,2,3,4,5,6,6}
#convert to list
l1 = list(s3)
print(type(l1))
print(l1)

s3a = s3.copy()
print(1 in s3)
s3.clear()
print(1 in s3)
print(s3a)

my_set = {1,2,3,4,5,6}
your_set = {4,5,6,7,8,9,0}

print(my_set.difference(your_set))
my_set.discard(4)
print(my_set)
my_set.difference_update(your_set)
print(my_set)

tot_set = my_set.union(your_set)
print(tot_set)

my_sub_set = {2,3,4}
print(my_sub_set.issubset(tot_set))
print(tot_set.issuperset(my_sub_set))

#Differenze con i dizionari
def ha_dupplicati_d(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def ha_dupplicati_s(t):
    return len(set(t)) < len(t)
