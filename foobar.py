# import this

a = "pippo"
b = "pippo"
print(a is b)

a = 'pluto'
b = 'pluto'

print(a is b)

a = 'plutoplutopluto'
b = 'plutoplutopluto'

print(a is b)

a = 'plutoplutopluto1111'
b = 'plutoplutopluto1111'

print(a is b)

c = 'plutoplutopluto1111plutoplutopluto1111plutoplutopluto1111plutoplutopluto1111plutoplutopluto1111!'
d = 'plutoplutopluto1111plutoplutopluto1111plutoplutopluto1111plutoplutopluto1111plutoplutopluto1111!'

print(c is d)


def foo(a, b):
    a = "1"
    b = "2"

foo(c, d)

print(c, d)

list1 = list2 = ['1', '2', '3']

list1.append('4')

print(list1)
print(list2)

list2 +=['5']

print(list1)
print(list2)

print(list1)
print(list2)

class pippo():
    pass


print(pippo.__name__)

pippo_obj = pippo()

print(pippo_obj.__name__)
