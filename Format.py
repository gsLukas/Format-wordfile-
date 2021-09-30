#!/usr/bin/env python3


import time
from progress.bar import Bar
import os

os.system("clear")

print ("\t\tEN-US// Welcome to FormatWordFile \n\t\tPT-BR// Bem vindo ao FormatWordFile\n" );
print ("\t\t\tby gsLukas and zNairy" )
time.sleep(2);
os.system('clear')

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

""" # print green :  print(f"{bcolors.OK}       _TEXTO_AQUI_  {bcolors.RESET}") """
""" # print yellow : print(f"{bcolors.WARNING}  _TEXTO_AQUI_  {bcolors.RESET}") """
""" # print red :    print(f"{bcolor.FAIL}      _TEXTO_AQUI_  {bcolors.RESET}") """

print (f'{bcolors.WARNING}EN-US// Enter name of the WordFile to format \nPT-BR// Inserir o nome do WordFile para formatar: {bcolors.RESET}');
print ('\nCurrent Directory:')
os.system ('pwd')

file = input(f"{bcolors.OK}Path: {bcolors.RESET}");
class WordsFile(object):
    """ evita sobrecarga de memoria e possibilita usar arquivos grandes de palavras """
    """ avoids memory overload and makes it possible to use large word files """

#34
    def __init__(self, filepath):
        self.wordfile = open(filepath, 'r', encoding="utf8", errors='ignore')
        self.currentLine = ''
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.currentLine = self.wordfile.readline()
        if not self.currentLine:
            raise StopIteration
#46
        return self.currentLine

print (f'{bcolors.WARNING}EN_US// Name for new WordFile\nPT_BR// Nome para novo WordFile {bcolors.RESET}');
name_txt = input(f'{bcolors.OK}New Path:{bcolors.RESET}');

#Criar Menu de Escolha | Padrão de PassWord

print (f"{bcolors.WARNING}\nEN-US// Standard WIFI format \nPT_BR// Formato padrão WIFI (Min8 Max 64): Press 1{bcolors.RESET}");

wifi = int(input(f"{bcolors.OK}Select:{bcolors.RESET} "));

#if wifi == 2:
#    with Bar(f'{bcolors.RESET}Starting.....{bcolors.RESET}') as bar:
#        for word in range(100):
#            time.sleep(0.02);
#            bar.next()
#    print(f'{bcolors.FAIL}\nFormatting please wait for writing confirmation!{bcolors.RESET}');
#    with open(name_txt, 'w') as outputFile:
#        for word in WordsFile(file):
#            if len(word) <= 8:
#                outputFile.write(word);
#    with Bar(f'{bcolors.OK}Saving...{bcolors.RESET}') as bar:
#        for word in range(100):
#            time.sleep(0.02);
#            bar.next()

#73
if wifi == 1:
    with Bar(f'{bcolors.RESET}Starting.....{bcolors.RESET}') as bar:
        for word in range(100):
           time.sleep(0.02);
           bar.next()           
    print(f'{bcolors.FAIL}\nFormatting please wait for writing confirmation!{bcolors.RESET}');
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            if len(word) >= 8 and len(word) <= 64:
                outputFile.write(word);
    with Bar(f'{bcolors.OK}Saving...{bcolors.RESET}') as bar:
        for word in range(100):
            time.sleep(0.02);
            bar.next()

if wifi != 1 and wifi != 2:
    print(f"{bcolors.FAIL}Ocorreu um erro, tente novamente!\nVocê deve usar 1 ou 2.{bcolors.RESET}")
