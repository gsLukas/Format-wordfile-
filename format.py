#!/usr/bin python

from colors import BColors
from wordsFile import WordsFile
from time import sleep
from os import system, path

def format_words_file(input_file_path, output_file_path, min_length, max_length):
    """Reads a file of words, formats them and writes to another file."""
    if not path.exists(input_file_path):
        print(f"{BColors.FAIL}File does not exist!{BColors.RESET}")
        return
    
    print(f'{BColors.FAIL}\nFormatting please wait for writing confirmation!{BColors.RESET}')
    with open(output_file_path, 'w') as output_file:
        for word in WordsFile(input_file_path):
            word = "".join(w for w in word.split())
            if len(word) >= min_length and len(word) <= max_length:
                output_file.write(word + "\n")

system("clear")
sleep(2)
system('clear')
print(f"Current Directory: [{path.abspath(path.curdir)}]")

input_file_path = input(f"{BColors.OK}Input file path: {BColors.RESET}")
output_file_path = input(f"{BColors.OK}Output file path: {BColors.RESET}")

option = input(f"{BColors.OK}Select an option:\n1 - Words between 8 and 64 characters\n2 - Words between 1 and 256 characters\n3 - Words between 8 and 128 characters\n4 - Words between 1 and 14 characters\n5 - Words between 8 and 128 characters\n{BColors.RESET}")

if not option.isdigit() or int(option) not in range(1, 6):
    print(f"{BColors.FAIL}Invalid option!{BColors.RESET}")
else:
    if int(option) == 1:
        format_words_file(input_file_path, output_file_path, 8, 64)
    elif int(option) == 2:
        format_words_file(input_file_path, output_file_path, 1, 256)
    elif int(option) == 3:
        format_words_file(input_file_path, output_file_path, 8, 128)
    elif int(option) == 4:
        format_words_file(input_file_path, output_file_path, 1, 14)
    else:
        format_words_file(input_file_path, output_file_path, 8, 128)
