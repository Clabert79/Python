import copy

def lookup_inverse(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise LookupError()



d = {'nome':'pippo','professione':['studente','lavoratore']}
print(d['nome'])
print(len(d))

##  un oggetto mutabile
d_num ={1:['uno'],2:['due','two']}
print(d_num)
d_num[3] = ['tre','three']
print(d_num)

# del cancella
del d_num[3]
print(d_num)

# i valori di un dizionario sono riferimenti ad oggetti

mylist = d_num[1]

print(mylist)
d_num[1].append('one')
print(mylist)

# si posso creare con la classe 'dict'

d_dict_a = dict([('colore','giallo'),('numero',33)])

print(d_dict_a)

# chiave velore

d_dict_b = dict(colore='giallo', numero=33)

print(d_dict_b)

print(len(d_num))

print("-----------------------------")
# ** funzione zip in python
s = 'ABCD' # oggetto itereabike
l = ["alfa", "beta", "gamma", "delta"]

for i in zip(s, l):
		print(i)
print("-----------------------------")

# A dictionary comprehension takes the form {key: value for (key, value) in iterable}
keys = ['a', 'b', 'c', 'd', 'e']

values = [1, 2, 3, 4, 5]

d_com_1 = {k:v for (k,v) in zip(keys, values)}
print(d_com_1)

d_com_2 = dict(zip(keys, values))

print(d_com_2)

d_com_3 = {k: bin(k**2) for k in range(5) if k % 2 == 0}

print(d_com_3)

d_com_4 = {x: x**2 for x in [1, 2, 3, 4, 5]}

print(d_com_4)

d_com_5 = {100:100, 'numeri':[1,2,3], 'lettere': ['a', 'b', 'c']}

d_com_6 = d_com_5.copy()

#stesso riferimentp
print(d_com_5["numeri"] is d_com_6["numeri"])

d_com_7 = copy.deepcopy(d_com_5)

#diverso riferimento
print(d_com_5["numeri"] is d_com_7["numeri"])

# se si accede a una chiave con esiste viene sollevata un'eccezione
# per gestirlo in maniera precisa usare il metodo GET

print(d_com_6.get("nessuno", "'nessono no esiste'"))

d_num_no_keys = {1:'uno', 2:'due'}

#se esiste si comporta come get
print(d_num_no_keys.setdefault(1))

#se non esiste aggiunge la chiave con valore none
print(d_num_no_keys.setdefault(3))
print(d_num_no_keys)

print(d_num_no_keys.setdefault(4, 'quattro'))
print(d_num_no_keys)

d_com_8 = dict(nome='Python', creatore='Guido')
print(d_com_8)

d_com_8.update(creatore='Guido van Rossum')
print(d_com_8)

d_com_8.update(versione='3.8')
print(d_com_8)

#Iterazione
d_com_9 = {11:'undici', 22:'ventidue', 33: 'trentatre'}
for k in d_com_9:
	print(k)

for k in sorted(d_com_9, reverse=True):
	print(k, d_com_9[k])

for v in d_com_9.values():
	print(v)

for item in d_com_9.items():
	print(item)

d_com_1a = dict(a=1,b=2,c=3)
for k1 in d_com_1a.keys():
	print(k1)
d_com_1b = dict(d=4,e=5)
# d_com_1b.keys() & d_com_1b.keys()

from collections import OrderedDict

#does not order the elements for you, it preserves the order you give it.
d_ord_1 = OrderedDict()
d_ord_1[33]= 'trentatre'
d_ord_1[22]= 'ventidue'
d_ord_1[24]='ventiquattro'

print(d_ord_1)

mydict = {'b':2,'a':1,'d':3,'c':4}

orddict = OrderedDict(mydict)

print(mydict)
print(orddict)
sort_dic = sorted(mydict.items())
print(sort_dic)
print(orddict)

mydict.popitem()
orddict.popitem(True)

print(mydict)
print(orddict)

user = {
	'basket':[1,2,3],
	'greet': 'hello',
	'name': 'pippo'
}
# se non esiste la chiave crea il default
print(user.get('age'),55)

#print('basket' in user)


print('Items ...')
for key, value in user.items():
	print("Key: " + str(key) + " Value: " + str(value) )

print('Values ...')
for val in user.values():
	print(val)

print('Keys ...')
for k in user.keys():
	print(k)

########################
#defaultdict
########################

from collections import defaultdict

def def_value():
	return '*'

dir_d = defaultdict(def_value)
dir_d["A"] = 1
dir_d["B"] = 2

print(dir_d["A"])
print(dir_d["B"])
print(dir_d["C"])
