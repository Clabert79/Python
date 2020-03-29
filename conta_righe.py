def contarighe(nomeFile):
	conta = 0
	
	for conta in range(10):
		print(nomeFile + str(conta))
		conta = conta + 1

	conta = 0

	while conta <= 10:
		print(nomeFile + str(conta))
		conta = conta + 1

if __name__ == '__main__':
	print(contarighe("prova"))
	i = 1
	i += 1
	print(i)