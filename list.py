

import copy 
selfish = '01234567890'
print(selfish[0:len(selfish)])
print(selfish[:])

print(selfish[0:11:2])
print(selfish[::2])
print(selfish[-2])
print(selfish[::-1])

print("*************************")

formaggi = ['Cheddar', 'Edam', 'Gauda']
print('Edam' in formaggi)
print('Brie' in formaggi)

# ciclo
for formaggio in formaggi:
	print(formaggio)
print(".-.-.-.-.-.-.-.-.-.-.-.-.")
for i in range(len(formaggi)):
	print(formaggi[i])


mylist = ['ciao' , 100, 33, 'ciao2'] #puo' contenere tutti i tipi di dati
# print( str(mylist.index(100)) + " > " + str(mylist.index('ciao')))

# print(mylist[0:2])

print('ciao' in mylist)

mylist.reverse()

print("------------------------------------------>")
print(mylist)

#elimina l'ultimo elemeto // aggiungendo l'indice rimuove quel determinato elemento  
mylist.pop()
print(mylist)
print(mylist.pop(1)) # restituisce l'ememento che verrà eliminato
print(mylist)
print(mylist.remove('ciao2')) # restituisce none e deve essere inserito l'elemento corretto che vogliamo cancellare
print(mylist)

print("------------------------------------------>")

append_list = mylist.append(5)
print(append_list)
print(mylist)
#insert inserisce dove vuoi l'oggetto nella lista
append_list = mylist.insert(2,'Pluttooo')
print(append_list)


# mylist.sort()
print(mylist)

mylist.extend([9,10,12])
print(mylist)


print((mylist + ['python']) * 3)

#le liste sono oggetti mutabili
mylist[2] = 77
print(mylist)
mylist.clear()
print(mylist)

a,b,c,d = [1,2,3,4] #devono essere lo stesso numero
print(a)


r2 = range(3, 19, 2)
print(r2)

amazon_cart = [
				"notebooks", 
				"sunglasses",
				"toys",
				"grapes"
				]
# parte da 0 e va di 2 in 2
print(amazon_cart[0::2])
# sono mutabili
amazon_cart[0] = "laptop"
print(amazon_cart[0::1])
# prende il secondo elemento e il 3 in oridine 
# (il primo campo verifica l'indice il secondo la posizione)
print(amazon_cart[1:3])

# con lo slicing si crea una nuova lista
new_cart = amazon_cart[0:2]
new_cart[0] = "glum"
print(amazon_cart)
print(new_cart)
# se passo tutto l'oggetto python prende la referenza
new_cart_2 = amazon_cart
new_cart_2[0] = "glum"
print(amazon_cart)
print(new_cart_2)

#per creare una copia
new_cart_3 = amazon_cart[:]
new_cart_3[0] = "glum2"
print(amazon_cart)
print(new_cart_3)





