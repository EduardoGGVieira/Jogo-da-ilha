from lib.interface import *

def apenasitem(lst, txt=''):
    while True:
        try:
            a = input(txt)
        except KeyboardInterrupt:
            vermelho()
            print('\nUsuário preferiu não digitar nenhum valor.')
            semcor()
        else:
            if a in lst:
                break
            else:
                vermelho()
                print('ERRO! Por gentileza digite um valor válido.')
                semcor()
    return a


def apenasint(txt):
    while True:
        try:
            a = int(input(txt))
        except ValueError:
            vermelho()
            print('ERRO! Por gentileza digite um número inteiro.')
            semcor()
        except KeyboardInterrupt:
            vermelho()
            print('\nUsuário preferiu não digitar nenhum valor.')
            semcor()
        else:
            break
    return a


def apenasfloat(txt):
    while True:
        try:
            a = float(input(txt))
        except ValueError:
            vermelho()
            print('ERRO! Por gentileza digite um número inteiro.')
            semcor()
        except KeyboardInterrupt:
            vermelho()
            print('\nUsuário preferiu não digitar nenhum valor.')
            semcor()
        else:
            break
    return a


def contagem_itens(lst):
    contagem = list(map(str, range(len(lst))))
    return contagem