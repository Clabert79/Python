import json

json_data = '{"name":"Tom","age":39}'
json_to_python = json.loads(json_data)
print(json_to_python['name'])

j_dict ={'name':'Bob','age':44, 'employed':True}
dict_to_json = json.dumps(j_dict)

print(dict_to_json)

class Employee(object):
	def __init__(self, name):
		self.name = name

def jsonDefault(object):
		return object.__dict__

abder = Employee('Abder') 


jsonAbder = json.dumps(abder, default=jsonDefault) 
print(jsonAbder)

s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}'
j_s = json.loads(s)

print(j_s["wonderland"])

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('test.json', 'w') as outfile:
    json.dump(data, outfile)

with open("test.json") as json_file:
    json_data = json.load(json_file)	

for p in json_data['people']:
	print('Name: ' + p['name'])
	print('Website: ' + p['website'])
	print('From: ' + p['from'])


# Lavorare sulle stringhe

data_s ={u"foo":u"bar",u"baz":[]}
json_s = json.dumps(data_s) #con le stringhe con 's'
print(json_s)

# Lavoriamo con i file
from io import StringIO
json_IO = StringIO()
