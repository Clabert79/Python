for number in range(0 , 100):
	print(number)
for _ in range(0, 10, 2):
	print(_)
for _ in range(10, 0, -1):
	print(_)

for i,char in enumerate(list(range(49,55))):
	print(i, char)
	if char == 50:
		print(f'index of range is {i}')

