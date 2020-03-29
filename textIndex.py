import string

def trova(stringa, carattere):
	indice = 0
	while indice < len(stringa):
		if(stringa[indice] == carattere):
			return indice
		indice = indice + 1;
	return -1

frutto = "banana"
posizione = string.find(frutto,"a")
print("posizione -->" + str(posizione))	

s = "prova stringa" # Equivale ad a = 'o' b = 'v'  c = 'a' d = ' '
a,b,c,d = s[2:6]
print(a + "-" + b + "-" + c + "-" + d + "-")
print(s.startswith("pro"))
print(s.count('pro')) # conta le ricorenza dell'espresione nella stringa

print(s.title())#Restituisce una coppia della variabile ma con le prime lettere maiuscle 

print(s.upper()) #Tutto maiscolo

print(s.strip()) #Rimuove tutti gli spazzi all'inizio e alla fine
print(s.strip() * 3)

print(int('44') + int('44'))
print(s[1])

ultimo = len(s)-1

print( str(ultimo) + " - " + str(len(s))) 
print(s[12])

mylist = []
for item in "33;45;46;78".split(';'):
	mylist.append(int(item))

print(sum(mylist))

print(sum([int(item) for item in "33;45;46;78".split(';')]))

#generator expression
print(sum(int(item) for item in "33;45;46;79".split(';')))


# I boolenai vengono trattati come numeri
b = False

c = b + 1

if c:
	c = c + 1
	print(c)

c = c + 1

if c:
	c = None
	print(c)

## if c Error 
