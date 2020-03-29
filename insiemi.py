# Insiemi Set

insieme1 = {'pluto','pippo','paperino','minni'}
print(insieme1)

lettere = set('1112333445')

print(lettere)

#operazioni


animali_piccoli = {'topo', 'mosca'}
animali_grandi = {'elefante','ippopotamo'}
animali_bianchi = {'topo', 'colomba'}

# unione
animali_tutti = animali_piccoli | animali_grandi
print(animali_tutti)

#differenza (del primo elemto in ordine)
animali_differenza =  animali_bianchi - animali_piccoli
print(animali_differenza)

#intersezione
animali_intersezione = animali_piccoli &  animali_bianchi 
print(animali_intersezione)

#differenza simmetrica
animali_differenza_simmetrica = animali_piccoli ^ animali_bianchi 
print(animali_differenza_simmetrica)


#set comprehension

numeri ={1, 4, 8, 18, 13}
resti = {(n % 4)  for n in numeri}

print(resti)

# scopire se ci sono duplicati

print(len(set("pippo")) < len('pippo'))

print(len(set("pluto")) < len('pluto'))

valide = "abcdefghi"
parola_valida = "babbi"
parola_non_valida = "pippo"

print(set(parola_valida) <=	set(valide))
print(set(parola_non_valida) <=	set(valide))



