import sys
import os

out_dir_name = sys.argv[1] if sys.argv[1:] else 'out' #nome della directory di output
try:
	os.mkdir(out_dir_name) #crea directory di uotput
	print('I file verranno scritti nella directory', out_dir_name)
except FileExistsError:
    print("I file verranno scritti nella directory", out_dir_name, "esistente")

for file_name in os.listdir():
	if file_name.endswith('.data'):
		out_file_name = os.path.join(out_dir_name + 'out')
		# print('Sto per scrivere sul file `%s` ...' %out_file_name, end=' ')
		out = open(out_file_name, 'w')
		for line in open(file_name):
			d = [float(item) for item in line.split()] #splitta i vari valori della linea
			out.write('%.2f %.2f %.2f\n' %(min(d), max(d), sum(d)/len(d)))
		print('fatto')		