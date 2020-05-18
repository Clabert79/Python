import unicodedata
import string
from string import maketrans 
import sys
# --> https://www.w3schools.com/python/python_ref_string.asp
print(sys.version_info.major)

print(unicodedata.name(u'A'))
print('\n{LATIN CAPITAL LETTER A}')
# smethods = [name for name in dir(str) if not name.startwith('__')]
# print(smethods)
# print(dir(string))
s1 = 'sono unA stringA, quindi Una  sequenza immutabile di caratteri'
# numero di occorenze
print(s1.replace('una','UNA',1)) 
print(s1)

# Required to call maketrans function.
intab = "ABC"
outtab = "abc"
trantab1 = maketrans(intab, outtab)

print (s1.translate(trantab1))

# da vedere
# trantab2 = maketrans({ord('i'):None})
# print s1.translate(trantab2)
# print(s1.maketrans({ord('i'):None}))



s2 = 'Un giorno, se avro\' tempo, andro\' a correre'

split1 = s2.split()
print(split1)

split2 = s2.split(',')
print(split2)

split3 = s2.split('ro\'')
print(split3)

l1 = ["pippo", " ", "cade", " ", "dalla", " ", "bici" ]
print(" ".join(l1))

# aggiunge un carattere in prossimita' di un separatore
s3 = '-'.join(s2.split())
print(s3)

# rimuovono gli spazi
s4 = '    Stringa con    spazzi all \' interno'
print(s4.lstrip().strip()) 
print(s4.lstrip().rstrip())
# elimina i caratteri che corrispondono partendo in questo caso da sinistra
# ma ci devono essere se non non parte  
print('cccccc pluto'.lstrip('c '))

print(s4.title())
print(s4.strip().capitalize())
print(s4.upper())
print(s4.lower())
print('oggi una bella giornata'.startswith('oggi'))
print('1234bc'.isalnum()) #alfa numerici
print('abcc'.isalpha()) # alfabetici
#tutti i metodi delle stringh e di testo
##  print(set(smethods)-set(bmethods))
print('122'.isdigit)
## print('122'.isdecima
print(sys.maxunicode)
## decimals = [chr(c) for c in range(sys.maxunicode + 1) if(chr(c).isdecimal())]
## digits = [chr(c) for c in range(sys.maxunicode + 1) if(chr(c).isdigit())]
## numerics = [chr(c) for c in range(sys.maxunicode + 1) if(chr(c).isnumeric())]


#confronto tra string case sensitive
s1c = 'A presto Elisabetta'
s2c = s1c.title()
print(s1c, s2c, s1c == s2c) 
# non ne tiene conto del case migliore di Upper e lower
## print(s1c, s2c, s1c.casefold() == s2c.casefold()) 

# essendo immutabili vengono sempre restituite nuove stringhe
# %[(chiave)][opzione][profondita'][.precisione]tipo 
# '%s' Stringhe
# '%d' Intero decimale con segno
# '%i' Intero decimale con segno
# '%o' Intero ottonale con segno
# '%x' Esaadecimale
# '%c' Carattere singolo
print("%s %d una meraviglia" % ('Python', 3))
print('%d|%o|%x|%X' % (12,12,12,12))

#formattazione basata sui dizionari
print('%(name)s,%(pass)s,%(age)d' % {'age':27, 'name':'pippo', 'pass':'38388'})

# profondita' indica il numero minimo di caratteri
# puo' essere utile per incollonnare i valori in un file
print('>%d'%100)
print('>%17d'%100)

#metodo format (https://www.python.org/dev/peps/pep-3101/)
print('{name},  {0}, e nache una lista:{mylist}'.format(0,mylist=[0,1,2,3],name='Marco'))

import sys, os
print("L'utente %s usa %s su %s" %(os.environ.get("USER"), os.environ['SHELL'],sys.platform))


print('{names[0]} usa {languages[1]}'.format(languages=('C++','Python'), names=('Marco', 'Leo')))

# per formattare numeri in maniera piu' leggibile
print('{:,d}'.format(100000000))
print('{:,.3f}'.format(100000000.00))
print('{:,f}'.format(10000.00 + 10000.00j))
from decimal import Decimal
print('{:,.3f}'.format(Decimal(100000000.30)))

# si puo' utilizzare la funzione format che e' equivalente
# la funzione built-in non fa altro che chiamare il metodo __format_()
# dell'oggetto
print(format(2/4,'.2f'))
