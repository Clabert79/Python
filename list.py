
selfish = '01234567890'
print(selfish[0:11])
print(selfish[0:11:2])
print(selfish[::2])
print(selfish[-2])
print(selfish[::-1])
print("*************************")

mylist = ['ciao' , 100, 33, 'ciao2'] #puo' contenere tutti i tipi di dati
print( str(mylist.index(100)) + " > " + str(mylist.index('ciao')))

print(mylist[0:2])

print('ciao' in mylist)

mylist.reverse()
print(mylist)

mylist.pop()
print(mylist)

mylist.append(5)
print(mylist)

mylist.sort()
print(mylist)

mylist.extend([9,10,12])
print(mylist)


print((mylist + ['python']) * 3)

#le liste sono oggetti mutabili
mylist[2] = 77
print(mylist)

a,b,c,d = [1,2,3,4] #devono essere lo stesso numero
print(a)

r1 = range(6);
print(r1)

r2 = range(3, 19, 2)
print(r2)
