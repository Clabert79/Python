import math

print("floor: " + str(math.floor(-11.6)) + " -- " + str(math.floor(11.6)))

print("int: " + str(int(-11.6)) + " -- " + str(int(11.6)))

print("round: " + str(round(-11.6)) + " -- " + str(round(11.6)))

a = 2.0e200 #2.0*10**200
b = 2.0e200 #2.0*10**200

print("a: " + str(a))
print("b: " + str(b))

print(b - b == 0)
print(a - a == 0)

print(a * b == b)