
class FormatWordFile(object):
    
    """ args: Object wordsfile(namefile) """
    def __init__(self, wordsfile):
        self.wordsFile = wordsfile
    
    def getWordFileName(self):
        return self.wordsFile.namefile