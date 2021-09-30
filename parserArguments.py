from argparse import ArgumentParser

def createSetupParser():
    parser = ArgumentParser(description='Buscador de diretórios web')
    
    parser.add_argument('-u', '--url',  dest='url',
                        help='Url do site alvo', required=True)
    parser.add_argument('-w', '--wordlist', dest='wordlist',
                        help='Caminho da wordlist', default='./assets/wordlist.txt')
    parser.add_argument('-mc', '--match', dest='match',
                        help='Corresponde aos códigos de status HTTP | Ex: -mc 302,404,504', default='200')
    parser.add_argument('-s', '--ssl', help='Habilita o ssl para a requisição.',
    default=False, action='store_true', dest='ssl')
    parser.add_argument('-f', '--full', help='Mostra o status de todas as requisições, não apenas as bem-sucedidas.',
    dest='full', action='store_true')

    return parser, parser.parse_args()