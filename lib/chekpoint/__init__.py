from lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        vermelho()
        print('ERRO ao criar o arquivo!')
        semcor()
    else:
        verde()
        print(f'Arquivo {nome} criado com sucesso!')
        semcor()

def ver_itens(nome, n_em_item=False):
    try:
        a = open(nome, 'rt')
    except:
        vermelho()
        print('ERRO na leitura do arquivo!')
        semcor()
    else:
        vermelho()
        if not n_em_item:
            for lin in a:
                dados = lin.split(';')
                listas([f'{dados[0]}{dados[1]:>{36-len(dados[0])}}{dados[2]:>{36-len(dados[0])-len(dados[1])}}'])
        else:
            for posicao, lin in enumerate(a):
                dados = lin.split(';')
                listas([f'{posicao} - {dados[0]}{dados[1]:>{25-len(dados[0])}}{dados[2]:>11}'])
        semcor()
    finally:
        a.close()

def coletar(arq, nome='Item', Caracteristica='-', valor='-'):
    try:
        a = open(arq, 'at')
    except:
        vermelho()
        print('ERRO na abertura do arquivo')
        semcor()
    else:
        try:
            a.write(f'{nome};{Caracteristica};{valor}\n')
        except:
            vermelho()
            print('ERRO no cadastro dos dados')
            semcor()
        else:
            verde()
            print(f'Item {nome} coletado com sucesso!')
            semcor()

def ver_status(nome):
    try:
        a = open(nome, 'rt')
    except:
        vermelho()
        print('ERRO na leitura do arquivo!')
        semcor()
    else:
        vermelho()
        for lin in a:
            dados = lin.split(';')
            print(f'Vida = {dados[0]}\nEnergia = {dados[1]}\nSituação = {dados[2]}\nLocalização = {dados[3]}')
        semcor()
    finally:
        a.close()

def pegar_status(arq, item):
    try:
        a = open(arq, 'rt')
    except:
        vermelho()
        print('ERRO na abertura do arquivo')
        semcor()
    else:
        for lin in a:
            dados = lin.split(';')
            return dados[item] 

def modificar_status(arq, vida=100, Energia=100, Situação = 'Saudavel', Localização = 'Local do acidente'):
    try:
        a = open(arq, 'wt')
    except:
        vermelho()
        print('ERRO na abertura do arquivo')
        semcor()
    else:
        try:
            a.write(f'{vida};{Energia};{Situação};{Localização}\n')
        except:
            vermelho()
            print('ERRO no cadastro dos dados')
            semcor()
        else:
            verde()
            print(f'Dados do personagem modificado')
            semcor()

