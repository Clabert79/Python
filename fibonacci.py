var_test = 0
print("Prima " + str(var_test))

def esempio():
	global var_test
	var_test += 1

esempio()

print("Dopo " + str(var_test))

#questo è valore mutabile
memo = {0:0,1:1}

def fibonacci(n):
	if n in memo:
		return memo[n]
	res = fibonacci(n - 1) + fibonacci(n - 2)
	memo[n] = res
	return res

# print(fibonacci(4));
#print(memo)