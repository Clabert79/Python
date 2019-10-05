for line in open('data.txt'):
	result = sum(int(data)for data in line.split(';'))
	print(result)