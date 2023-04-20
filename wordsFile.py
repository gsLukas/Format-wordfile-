import os
from colors import BColors


class WordsFile:
    """
    Esta classe é responsável por ler arquivos grandes de palavras, evitando sobrecarga de memória.
    """

    def __init__(self, namefile: str):
        """
        Inicializa a classe.

        :param namefile: O nome do arquivo a ser lido.
        """
        self.namefile = namefile
        self.current_line = ''

        # Verifica se o arquivo existe e é um arquivo válido
        if not os.path.isfile(self.namefile):
            raise FileNotFoundError(f"{BColors.FAIL}Arquivo '{self.namefile}' não encontrado.{BColors.RESET}")

        # Abre o arquivo e armazena em uma variável
        try:
            self.wordlist = open(self.namefile, 'r', errors='ignore')
        except PermissionError:
            raise PermissionError(f"{BColors.FAIL}Falha ao abrir o arquivo '{self.namefile}', permissão negada!{BColors.RESET}")

    def __iter__(self):
        """
        Retorna um iterador para a classe.
        """
        return self

    def __next__(self):
        """
        Retorna a próxima linha do arquivo.
        """
        self.current_line = self.wordlist.readline()

        # Verifica se a linha é válida
        while self.current_line:
            self.current_line = self.current_line.strip()
            if self.current_line and any(w.isalpha() for w in self.current_line):
                return self.current_line
            self.current_line = self.wordlist.readline()

        # Fecha o arquivo
        self.wordlist.close()

        # Levanta a exceção para indicar o final do arquivo
        raise StopIteration

    def loadContent(self):
        """
        Carrega o conteúdo do arquivo em uma lista.

        :return: Uma lista com as palavras do arquivo.
        """
        wordlist = []

        # Verifica se o objeto retornado é um arquivo válido
        if not isinstance(self.wordlist, file):
            raise TypeError("O objeto retornado não é um arquivo válido.")

        # Lê as linhas do arquivo e adiciona na lista
        for line in self.wordlist:
            line = line.strip()
            if line and any(w.isalpha() for w in line):
                wordlist.append(line)

        # Fecha o arquivo
        self.wordlist.close()

        return wordlist
