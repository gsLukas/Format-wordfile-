#!/bin/bash env python3

import time

file = input("Informe o nome do arquivo desejado: ");
time.sleep(2)
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
time.sleep(2)

name_txt = input("Informe o nome da nova WordList: ");
print ("Selecione o tipo de formatação: ");
time.sleep(1)
print ("<= 8 Caracter: 1)");print (">= 8 Caracter: 2)");
time.sleep (1)
tam_texto = int(input("Informe o tamanho desejado: "));
time.sleep(2)

""" Aqui foi o primeiro teste realizado, vamos aperfeiações essa parte do código """
if tam_texto == 1: 
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            if len(word) <= 8:
                outputFile.write(word)

if tam_texto == 2:
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            if len(word) >= 8:
                outputFile.write(word)
                
                """ Fim da NOTA """

time.sleep (3)
print ("Finalizado! :");
