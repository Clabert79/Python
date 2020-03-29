## Divisione parole
import string

def clean_text(s):
	return s.translate(None, string.punctuation)

def extract_word(s):
	list_word = text.split()
	return list_word

def count_by_word(l):
	d = {}
	for word in l:
		if not d.has_key(word):
			d[word] = 1
		else:
			d[word] = d[word] + 1

	return d

text = "pippox: pippox, pippo. pluto ))))"

text = text.rstrip()
text = clean_text(text)
list_words = extract_word(text)
d = count_by_word(list_words)

print(sorted(d,key = lambda i:i[2], reverse=True))