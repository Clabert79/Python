# url for falsey
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
is_magician = True
is_expert = False

if is_expert and is_magician:
	print("You are a master magician")

elif is_magician and not is_expert:
	print("at least you're getting there")

elif not is_magician:
	print("You nedd magic powers")

# Ternary Operator
# condition_if_true if condition else condition_if_else

is_friend = True
can_message = "message allowed" if is_friend else "not allowed message"
print(can_message)

# valuta la codica AScii (https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html	)
print('a'>'b')

# == valuta se è equivalente non lo stesso riferimento valuta il valore
print('[ == ]')

print(True == 1)
print('1' == 1)  # false
print([] == 1)
print(10.0 == 10)
print([1, 2, 3] == [1,2,3])


# is valuta se la locazione in memoria è la stessa
print('[ is ]')

print(True is True)
print('1' is '1') 
print([] is [])
print(10 is 10)
print([1, 2, 3] is [1,2,3]) # sono riferimeti ad oggetti diversi

