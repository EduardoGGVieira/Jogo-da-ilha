from time import sleep


def amarelo():
    return print('\033[33m', end='')


def azul():
    return print('\033[34m', end='')


def verde():
    return print('\033[32m', end='')


def vermelho():
    return print('\033[31m', end='')


def semcor():
    return print('\033[m', end='')


def linha(lin="-",n=0):
    print(f"{lin}"*n)
    

def titulo(txt, lin="-" , n=0):
    linha(lin,n)
    print(f"{txt:^{n}}")
    linha(lin,n)


def paragrafo(txt,n=0.01):
    cont=0
    for i in txt:
        sleep(n)
        print(i, end='', flush=True)
        cont+=1
        if cont == 40:
            print()
            cont = 0
    print()


def listas(lst, n_em_item=False):
    if n_em_item:
        for posicao, valor in enumerate(lst):
            print(f'{posicao+1} - {valor}')
    else:
        for valor in lst:
            print(valor)
