import random
def sottrai(d1, d2):
	res = dict()
	for chiave in d1:
		if chiave not in d2:
			res[chiave] = None
	return res

d1 ={}
d2 = {}

for i in range(20):
	x = random.randint(1,100)
	d1 [x] = i

for i in range(20):
	x = random.randint(1,100)
	d2 [x] = i

# print(d1)
# print(d2)
print(sottrai(d1,d2))
