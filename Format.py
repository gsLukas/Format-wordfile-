#!/usr/bin python3

__author__ = '@gsLukas'
__colaborator__ = '@zNairy'
__contact__ = 'Discord: gsLukao#6445 | zNairy#7181 || Github: https://github.com/gsLukas | https://github.com/zNairy/'
__version__ = '1.0'


print (__author__)
print (__colaborator__)

from Colors import BColors
from wordsFile import WordsFile
import time
import os

os.system("clear")
print ("\t\tEN-US// Welcome to FormatWordFile \n\t\tPT-BR// Bem vindo ao FormatWordFile\n" );
print ("\t\t\tby gsLukas and zNairy" )
time.sleep(2);
os.system('clear')

print (f'{BColors.WARNING}EN-US// Enter name of the WordFile to format \nPT-BR// Inserir o nome do WordFile para formatar: {BColors.RESET}');
print ('\nCurrent Directory:')
os.system ('pwd')

file = input(f"{BColors.OK}Path: {BColors.RESET}");


print (f'{BColors.WARNING}EN_US// Name for new WordFile\nPT_BR// Nome para novo WordFile {BColors.RESET}');
name_txt = input(f'{BColors.OK}New Path:{BColors.RESET}');

#Menu choice

print (f"{BColors.WARNING}\nEN-US// Standard WIFI/wpa format \nPT_BR// Formato padrão WIFI/wpa (Min 8 Max 64): Press 1{BColors.RESET}");
print (f"{BColors.WARNING}\nEN-US// Standard SSH format \nPT_BR// Formato padrão SSH (Min 1 Max 256): Press 2{BColors.RESET}");
print (f"{BColors.WARNING}\nEN-US// Standard AWS format \nPT_BR// Formato padrão AWS (Min 8 Max 128): Press 3{BColors.RESET}");
print (f"{BColors.WARNING}\nEN-US// Standard Windows format \nPT_BR// Formato padrão Windows (Min 1 Max 14): Press 4{BColors.RESET}");
print (f"{BColors.WARNING}\nEN-US// Standard SQL Server format \nPT_BR// Formato padrão SQL Server (Min 8 Max 128): Press 5{BColors.RESET}");

option = int(input(f"{BColors.OK}Select:{BColors.RESET} "));

if option == 1:
    print(f'{BColors.FAIL}\nFormatting please wait for writing confirmation!{BColors.RESET}');
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            word = "".join(w for w in word.split())
            if word and any(w.isalpha() for w in word) and len(word) >= 8 and len(word) <= 64:
                outputFile.write(word + "\n");


elif option == 2:
    print(f'{BColors.FAIL}\nFormatting please wait for writing confirmation!{BColors.RESET}');
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            word = "".join(w for w in word.split())
            if word and any(w.isalpha() for w in word) and len(word) >= 1 and len(word) <= 256:
                outputFile.write(word + "\n");

elif option == 3:
    print(f'{BColors.FAIL}\nFormatting please wait for writing confirmation!{BColors.RESET}');
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            word = "".join(w for w in word.split())
            if word and any(w.isalpha() for w in word) and len(word) >= 8 and len(word) <= 128:
                outputFile.write(word + "\n");

elif option == 4:
    print(f'{BColors.FAIL}\nFormatting please wait for writing confirmation!{BColors.RESET}');
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            word = "".join(w for w in word.split())
            if word and any(w.isalpha() for w in word) and len(word) >= 1 and len(word) <= 14:
                outputFile.write(word + "\n");

elif option == 5:
    print(f'{BColors.FAIL}\nFormatting please wait for writing confirmation!{BColors.RESET}');
    with open(name_txt, 'w') as outputFile:
        for word in WordsFile(file):
            word = "".join(w for w in word.split())
            if word and any(w.isalpha() for w in word) and len(word) >= 8 and len(word) <= 128:
                outputFile.write(word + "\n");


else:
    print(f"{BColors.FAIL}Invalid Option!{BColors.RESET}")
