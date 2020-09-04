import argparse
import fnmatch
import os
import re

parser = argparse.ArgumentParser(description='Cerca sia file che testo')
parser.add_argument('-f','--file', type=str,required=True,help='Nome del file')
parser.add_argument('-d','--dir',default = os.curdir, help='Nome del file')
parser.add_argument('-p','--pattern', default='', help='Pattern da cercare')
parser.add_argument('-r','--recursive', action='store_true', help='Ricorsiva')
args = parser.parse_args()

def file_finder(pattern:str,top_dir:str,recursive: bool=false):
	for path, dirs, files in os.walk(top_dir):
		if not recursive:
			dir.clear() # svuota la lista delle sotto directory di 'top_dir'
		
		for name in fnmatch.filter(file, pattern):
			yield os.path.join(path, name)
			

def file_inspector(file_name: str, pattern:str):
	for line in open(file_name):
		if re.search(pattern, line):
			yield line

for file in file_finder(args.file, args.dir, args.recursive):
	if args.pattern:
		for line in file_inspector(file, args.pattern):
			print(file,line,sep='_>',end='')
	else:
		print(file)


