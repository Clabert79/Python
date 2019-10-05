import sys

quoto = int(sys.argv[1])
dividendo = int(sys.argv[2])

try:
	quoziente = quoto / quoziente
except :
	print "Eccezione"
	print sys.exc_info()[0]
	print sys.exc_info()[1]
	print sys.exc_info()[2]

else:
	print "quoziente uguale a " ,quoziente
finally:
	print "Ho finito"