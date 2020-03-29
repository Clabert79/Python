# def more_frequent(s):
def get_key(val, diz): 
    for key, value in diz.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
s = "pippo"
d = {}
for l in s:
	if not d.has_key(l):
		d[l] = 1
	else:
		d[l] = d[l] + 1


list_reverse = sorted(d.values(), reverse=True)
for k in list_reverse:
	print(get_key(k,d))	


