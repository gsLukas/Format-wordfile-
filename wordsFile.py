import os
import csv

MIN_WORD_LEN = 3

def open_file(filename):
    try:
        fp = open(filename, 'r')
    except FileNotFoundError:
        print(f"Erro ao abrir o arquivo '{filename}'")
        return None
    else:
        return fp

def read_words(fp):
    words = []
    reader = csv.reader(fp)
    for row in reader:
        for word in row:
            if len(word) >= MIN_WORD_LEN and word.isalpha() and word.lower() == word:
                words.append(word)
    return words

def check_duplicates(words):
    return len(words) != len(set(words))

def format_wordlist():
    filename = input("Digite o nome do arquivo de word list: ")
    fp = open_file(filename)
    if fp is None:
        return

    words = read_words(fp)
    fp.close()

    if len(words) == 0:
        print(f"Nenhuma palavra válida encontrada no arquivo '{filename}'")
        return

    if check_duplicates(words):
        print(f"Foram encontradas palavras duplicadas no arquivo '{filename}'")

    outfile = input("Digite o nome do arquivo de saída: ")
    try:
        with open(outfile, 'w') as outfp:
            writer = csv.writer(outfp)
            writer.writerows([[word] for word in sorted(words)])
    except OSError:
        print(f"Erro ao criar o arquivo '{outfile}'")
        return

    print("Word list formatada com sucesso!")

format_wordlist()
