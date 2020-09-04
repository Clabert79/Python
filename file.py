
# https://www.datacamp.com/community/tutorials/reading-writing-files-python?utm_source=adwords_ppc&utm_campaignid=9942305733&utm_adgroupid=100189364546&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=255798340456&utm_targetid=aud-517318241987:dsa-929501846124&utm_loc_interest_ms=&utm_loc_physical_ms=20609&gclid=CjwKCAjw8df2BRA3EiwAvfZWaHICHyRTZ58-qgFRUj0REIOenZqYlkMQiG3sFkf8s0bxWtCpc2xxhxoCSFIQAvD_BwE

filew_1 = open('myfile','w')
filew_1.write('testo') # restituisce il numero di caratteri

# file aperto in binary mode
filer_1 = open('myfile','rb') # la r sta per lettura la b finale sta per binary
filer_1.read()



filew_2 = open('myfile','wb')
filew_2.write(b'testo byte') # scriviamo una stringa di byte

filer_1.read(2) # legge 2 caratteri

# quando il file object non ha più etichette che fanno riferimanto svuota il file

# quando si raggiunge la fine del fil file.read() restituisce una stringa vuota
filew_2.seek(0) # svuota il buffer e ci posiziona all'inizio del file
filew_2.tell() # svuota il file e ci restituisce la posizione

filew_1.writelines(['oggetto iterabile\n'])  # scrive su file un oggetto iterabile
										  # deve essere agiunto il carettre di new line in maniera esplicita

filer_1.readline() # legge una line per volta lasciado un cratere newline

# quando scriviamo un file si genera un buffering di scrittura in memoria
filer_1.flush() #svuota il file
filer_1.close() #svuota anche il file

# usare sempre la clausola with
with open('myfile_1.txt') as f:
	print(f.read())

'''
open(
	file,
	mode = 'r', --- > 'x' gestisce meglio la gestine del file
	buffering = -1
	encoding = None (di default uft 8 es encoding='latin1')
	errors = None, (errors='ignore', errors='replace')
	newline = None,
	closefd = True,
	opener = None ) -> Object deve essere None oppure un oggetto callable
'''

open('myfile_utf_16','w',encoding='utf-16').write('Pyhton 3')
print(open('myfile_utf_16','rb').read())
print(open('myfile_utf_16','rb').read(2))
print(open('myfile_utf_16',encoding='utf-16').read())

import os, stat

filew_3 = open('foo.bash','w')
filew_3.write('testo di prova')
# imposta i permessi
open('foo.bash', opener=lambda file,flags: os.open(file, flags, 0o744))
mode = os.stat('foo.bash').st_mode
print(stat.filemode(mode))
