#!/bin/bash env python3

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

""" # print green :  print(f"{bcolors.OK}       _TEXTO_AQUI_  {bcolors.RESET}") """
""" # print yellow : print(f"{bcolors.WARNING}  _TEXTO_AQUI_  {bcolors.RESET}") """
""" # print red :    print(f"{bcolor.FAIL}      _TEXTO_AQUI_  {bcolors.RESET}") """

from tqdm import tqdm
from tqdm import trange
import time
from progress.bar import Bar

file = input("Inserir o nome do " f"{bcolors.OK}WordFile{bcolors.RESET} para formatar: ");
class WordsFile(object):
    """ evita sobrecarga de memoria e possibilita usar arquivos grandes de palavras """
    def __init__(self, filepath):
        self.wordfile = open(filepath, 'r', encoding="utf8", errors='ignore')
        self.currentLine = ''
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.currentLine = self.wordfile.readline()
        if not self.currentLine:
            raise StopIteration
        
        return self.currentLine

name_txt = input("Informe o nome da nova WordList: ");
print ("Selecione o tamanho da formatação: ");
print ("para formatar <= 8 Caracter: 1) ou  >= 8 Caracter: 2)");
tam_texto = int(input("Informe o numero desejado: 1 ou 2: "));

if tam_texto == 1:
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            if len(word) <= 8:
                outputFile.write(word);
        with Bar(f'{bcolors.OK}Processando...{bcolors.RESET}') as bar:
            for word in range(100):
                time.sleep(0.02);
                bar.next()

if tam_texto == 2:
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            if len(word) >= 8:
                outputFile.write(word);
    with Bar(f'{bcolors.OK}Processando...{bcolors.RESET}') as bar:
        for word in range(100):
           time.sleep(0.02);
           bar.next()

if tam_texto != 1 and tam_texto != 2:
    print(f"{bcolors.FAIL}Ocorreu um erro, tente novamente!\nVocê deve usar 1 ou 2.{bcolors.RESET}")
