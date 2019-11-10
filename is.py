#funzioni

def decapita(t):
	del t[0]
def non_decapita(t):
	t = t[1:]

def print_keys(d):
	for c in d:
		print("key: " + c,"value: " + d[c])
	pass
def inverse_lookup(d, v):
	for k in d:
		print("-->> " + d[k])
		if d[k] == v:
			return k
	raise LookupError("value " + v + " is not found")

# codice ...
a = "pippo"
b = "pippo"

if (a == b):
	print("True")

print(a is b)
list_a = ["a", "b", "c"]
list_b = ["a", "b", "c"]

print(list_a is list_b)

list_a = list_b
print(list_a is list_b)

list_a[0] = 1
print(list_b)

decapita(list_b)
print(list_a)

list_b = list_a.append("d")
print(list_a)
print(list_b)
list_c = list_a + [4]
print(list_c)
print(non_decapita(list_c))
eng2it = {'uno':'one','tre':'tree','due':'two'}
print(eng2it)
print(eng2it['due'])
print(len(eng2it))
print_keys(eng2it)

array = [5, 1, 4, 3]
array.sort()
print(array)