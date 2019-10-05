import sys

quoto = int(sys.argv[1])
dividendo = int(sys.argv[2])
try:
	quoziente = quoto / dividendo
except ZeroDivisionError:
	print ("Denominatore uguale a 0")
finally:
	print ("Ho finito")