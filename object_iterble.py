class Potenza:
    def __init__(self, base):
        self.base = base
        self.esponente = 1

    def __iter__(self):
        self.numero = self.base
        return self

    def next(self):
        if self.esponente <= 5:
            self.numero_successivo = self.numero
            self.numero = self.numero * self.base
            self.esponente += 1
            #cio' che viene stamaoato
            return self.numero_successivo
        else:
            raise StopIteration



if __name__ == '__main__':
    mia_classe = Potenza(2)
    iteratore_mia_classe = iter(mia_classe)

    for xbase in mia_classe:
        print(xbase)
