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