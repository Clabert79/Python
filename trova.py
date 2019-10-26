def trova(parola, lettera):
    indice = 0
    while indice < len(parola):
        
        if parola[indice] == lettera:
        	return indice
        
        indice = indice + 1
    return -1
        
print(trova("pippo","i"))

parola = "banana"
conta = 0
for lettera in parola:
	if lettera == 'a':
		conta = conta + 1

print(conta)
print(parola.find('ba',3,2))