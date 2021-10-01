from argparse import ArgumentParser

def createSetupParser():
    parser = ArgumentParser(description="Formata e melhora wordlists")

    parser.add_argument('-w', '--wordlist', dest='wordlistpath', help='Caminho da wordlist', default="default.txt") # adiciona argumentos
    parser.add_argument('-f', '--f', dest='perfil', required=True)
    return parser, parser.parse_args()