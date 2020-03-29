contenuto = "testo di prova"
file1 = open("esempio1.txt","w") #parametro di scrittura
file1.write(contenuto)
file1.close() #close()

nuova_stringa = "stringa aggiunta"
file1 = open("esempio1.txt","a")
file1.write(nuova_stringa)
file1.close()
var_testo_file = open("esempio1.txt","r").read()
## print(var_testo_file)
for lettera in var_testo_file:
	print(lettera)