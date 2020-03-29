l = [1, "pippo", 4.5, "pluto"]
l.append("paperino")

for i in range(0,len(l)):
	print(l[i])

t = (1, 3, 5, 7, 9)

for i in range(0,len(t)):
	print(t[i])


for val in t:
	print(val)


d = {"k1":1, "k2":2, "k3":3}
print(d["k1"])

for x in d.iterkeys():
	print(x)
for x in d.itervalues():
	print(x)
