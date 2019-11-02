def decapita(t):
	del t[0]

a = "pippo"
b = "pippo"
def non_decapita(t):
	t = t[1:]
print(a is b)

if (a == b):
	print("True")

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
