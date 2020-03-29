import math

def tutte_maiuscole_verbose(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def tutte_maiscole_contratta(t):
	return [s.capitalize() for s in t]

def solo_maiuscole_verbose(t):
	res = []
	for s in t:
		if s.isupper():
			res.append(s)
	return res

def solo_maiuscole_contratta(t):
	return [s for s in t if s.isupper()]



#Fundamental Data Type
print(type(6))
print(type(2 - 4))
print(type(2 * 4))
print(type(2.00 / 5.00))
print(2.00 ** 5.00)

print((20 - 3) + 2 ** 2)

# ()
# **
# ] /
# + -

# Espressioni condizionali

x = 100

# verbose
if x > 0:
	y = math.log(x)
else:
	y = float('nan')

print(y)

#contratta

y = math.log(x) if x > 0 else float('nan')

print(y)

print(tutte_maiuscole_verbose('pluto'))
print(tutte_maiscole_contratta('pluto'))
print(solo_maiuscole_verbose('pLuTO'))
print(solo_maiuscole_contratta('pLuTO'))

# Generator expression
g = (x**2 for x in range(7))

print("*******************")
print(next(g))
print(next(g))
print("*******************")

for val in g:
	print(val)

print(sum(x**2 for x in range(5)))

# se almeno un valore e' True

print(any([False, False, True]))

print(any(lettera == 't' for lettera in 'monty'))



