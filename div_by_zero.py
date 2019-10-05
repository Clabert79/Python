a = 1
b = 0 
try:
	print 	"Risultato ", a/b

except ZeroDivisionError:
	print "Divisione per zero !"

print "Fine programma"

try:
	print "Adesso solleveremo un'eccezione"
	raise ValueError, "Bingo!"
except :
	print "Un'eccezione si è sollevata!"
	raise