import os
import shutil
import click


@gruposales.command()
def opcao1():
    click.echo('Opção 1 selecionada')

@gruposales.command()
def opcao2():
    click.echo('Opção 2 selecionada')

if __name__ == '__main__':
    click.clear()
    click.echo('Bem-vindo(a) ao Grupo Sales!')
    gruposales()  

@click.group()
def cli():
    pass

def formatar(arquivo, tamanho):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    total_linhas = len(linhas)
    metade = total_linhas // 2
    
    palavras = set()
    
    for i, linha in enumerate(linhas):
        if i == metade:
            click.echo('50% do processo concluído')
        
        linha = linha.strip()
        if linha.isalpha() and len(linha) >= tamanho:
            palavras.add(linha.lower())
    
    palavras = sorted(palavras)
    
    with open('Word list atualizada', 'w') as f:
        for palavra in palavras:
            f.write(palavra + '\n')
    
    click.echo('Arquivo formatado com sucesso!')


def corrigir(arquivo):
    # Função que corrige a lista de palavras
    if not os.access(arquivo, os.R_OK):
        click.echo(f'Não foi possível ler o arquivo {arquivo}')
        return

    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    total_linhas = len(linhas)
    metade = total_linhas // 2

    novas_linhas = []

    for i, linha in enumerate(linhas):
        if i == metade:
            click.echo('50% do processo concluído')

        linha = linha.strip()

        # Verifica se a palavra tem caracteres sequenciais iguais
        if len(set(linha)) < 2:
            continue

        # Verifica se a linha tem mais de duas combinações de caracteres iguais
        if any(linha[j] == linha[j+1] for j in range(len(linha)-1) for k in range(j+1, len(linha)-1) if linha[k] == linha[k+1]):
            continue

        novas_linhas.append(linha)

    with open('Word list atualizada corrigida', 'w') as f:
        for linha in novas_linhas:
            f.write(linha + '\n')

    click.echo('Arquivo corrigido com sucesso!')

@cli.command()
@click.argument('arquivo')
@click.option('--tamanho', default=3, help='Tamanho mínimo das palavras')
def formatar_wordlist(arquivo, tamanho):
    if not os.access(arquivo, os.R_OK):
        click.echo(f'Não foi possível ler o arquivo {arquivo}')
        return

    try:
        formatar(arquivo, tamanho)
    except Exception as e:
        click.echo(f'Ocorreu um erro ao formatar o arquivo: {str(e)}')
        return

    click.echo('Arquivo formatado com sucesso!')

@cli.command()
@click.argument('arquivo')
def corrigir_wordlist(arquivo):
    if not os.access(arquivo, os.R_OK):
        click.echo(f'Não foi possível ler o arquivo {arquivo}')
        return

    try:
        corrigir(arquivo)
    except Exception as e:
        click.echo(f'Ocorreu um erro ao corrigir o arquivo: {str(e)}')
        return

    click.echo


  
