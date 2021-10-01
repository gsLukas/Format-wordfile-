from Colors import BColors

class WordsFile(object):
    """ evita sobrecarga de memoria e possibilita usar arquivos grandes de palavras
        avoids memory overload and makes it possible to use large word files """
    
    def __init__(self, namefile):
        self.namefile = namefile
        self.abriu = False
        self.wordlist = self.loadContent()
        self.currentLine = ''
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.currentLine = self.wordlist.readline()
        if not self.currentLine:
            raise StopIteration
        
        return self.currentLine

    def loadContent(self):
        try:
            arquivo = open(self.namefile, 'r', errors='ignore')
            self.abriu = True
            return arquivo

        except FileNotFoundError:
            print("Mensagem de: ")
            exit()            