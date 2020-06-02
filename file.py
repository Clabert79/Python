
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

