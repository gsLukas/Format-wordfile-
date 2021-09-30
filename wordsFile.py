
class WordsFile(object):
    def __init__(self, namefile):
        self.namefile = namefile
        self.wordlist = open(namefile, 'r', encoding="utf8", errors='ignore')
        self.currentLine = ''
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.currentLine = self.wordlist.readline()
        if not self.currentLine:
            raise StopIteration
        
        return self.currentLine