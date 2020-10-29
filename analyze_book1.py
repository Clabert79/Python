from __future__ import print_function, division

import random
import string


def process_file(filename, skip_header):
	"""Makes a histogram that contains the words from files

	filename:string
	skip_header: boolean, wheter to skip the Gutenberg header

	return: map from each word to number of times it appears.

	"""
	hist ={}
	fp = open(filename)

	if skip_header:
		skip_gutenberg_header(fp)
	for line in fp:
		if line.startswith('*** END OF THIS'):
			break

		process_line(line, hist)

	return hist	

def skip_gutenberg_header():
	"""Reads from until it finds the line that ends the headers
	
	fp: open file object
	"""
	for line in fp:
		if line.startswith('*** START OF THIS'):
			break
			

