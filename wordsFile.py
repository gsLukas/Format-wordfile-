from colors import BColors

class WordsFile(object):
    """ evita sobrecarga de memoria e possibilita usar arquivos grandes de palavras
        avoids memory overload and makes it possible to use large word files """
    
    def __init__(self, namefile):
        self.namefile = namefile
        self.wordlist = self.loadContent()
        self.currentLine = ''

    def __iter__(self):
        return self

    def __next__(self):
        self.currentLine = self.wordlist.readline()
        if self.currentLine:
            self.currentLine = self.currentLine.strip()
            if self.currentLine and any(w.isalpha() for w in self.currentLine):
                return self.currentLine
                
            self.__next__()

        raise StopIteration

    def loadContent(self):
        try:
            return open(self.namefile, 'r', errors='ignore')

        except FileNotFoundError:
            print(f'{BColors.FAIL}File {BColors.WARNING}"{self.namefile}" {BColors.FAIL}not found.{BColors.RESET}')
            exit(1)
            
        except PermissionError:
            print(f'{BColors.FAIL}Failed to open file {BColors.WARNING}"{self.namefile}", {BColors.FAIL}permission denied!{BColors.RESET}')
            exit(1)