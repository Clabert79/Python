def alfabetica(parola):
	precedente = parola[0]
	for c in parola:
		if c < precedente:
			return False
		precedente = c	
	return True

def alfabetica1(parola):
	if len(parola) <= 1:
		return True
	if parola[0] > parola[1]:
		return False
	return  alfabetica1(parola[1:])


def alfabetica2(parola):
	i = 0
	while i < len(parola):
		if parola[i+1] < parola[i]:
			return False
		i = i+1

	return True

def triple_doppie(parola):
	i = 0
	numero_doppie = 0
	lettera_precedente = 0
	while i < len(parola):
		if (lettera_precedente + 1) < len(parola): 
			print("prima lettera: " + parola[lettera_precedente] + " seconda: " + parola[lettera_precedente + 1])
			if parola[lettera_precedente] == parola[lettera_precedente + 1]:
				numero_doppie = numero_doppie + 1
			else:
				numero_doppie = 0

			print(numero_doppie)
			if numero_doppie == 3:
				return True

		if i == len(parola): 
			if parola[len(parola) - 2] == parola[len(parola) - 1]:
				numero_doppie = numero_doppie + 1
			if numero_doppie == 3:
				return True
		
		lettera_precedente = i + 1
		i = i + 1

	return False

print(triple_doppie("aaxbbccxaabbcc"))
# print(alfabetica("abcde"))
# print(alfabetica1("pluto"))
# print(alfabetica2("paperino"))
