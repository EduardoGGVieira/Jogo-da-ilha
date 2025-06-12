from lib.interface import *
from lib.validacao_de_dados import *

# variaveis
personagem = {'Vida': 100, 'Energia': 100, 'Situação': 'Saudavel', 'Localização': 'Local do acidente'}
inventario = []
lista_opcoes = []

titulo("JOGO DA ILHA",n=40)

paragrafo("blalblaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabla")

#opcoes1
while True:
    linha('~',40)
    opcoes = ['Verificar os bolsos','Correr pela orla da praia','Procurar por sobreviventes na região', 'Adentrar na floresta','Status do personagem']
    listas(opcoes, True)  
    resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

    if resposta == '1':
        listas(inventario, True)

    elif resposta == '2':
        paragrafo('vc corre')
        lista_opcoes.append('Correr pela orla da praia')
        break

    elif resposta == '3':
        paragrafo('')
        lista_opcoes.append('Procurar por sobreviventes na regeão')
        break

    
    elif resposta == '4':
        paragrafo('')
        lista_opcoes.append('Adentrar na floresta')
        break

    elif resposta == '5':
        print(personagem)

if lista_opcoes[0] == 'Correr pela orla da praia':
    #opção2
    while True:
        linha('~',40)
        opcoes = ['Verificar os bolsos','Continuar à correr desesperado','Entrar na floresta','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
          listas(inventario, True)

        elif resposta == '2':
          paragrafo('corre mais')
          lista_opcoes.append('Continuar à correr desesperado')
          break

        elif resposta == '3':
            paragrafo('')
            lista_opcoes.append('Entrar na floresta')
            break
        
        elif resposta == '4':
          print(personagem)
        
    if lista_opcoes[1] == 'Continuar à correr desesperado':

        #opção3
        while True:
            linha('~',40)
            opcoes = ['Verificar os bolsos','Aguardar por socorro','Entrar na floresta','Status do personagem']
            listas(opcoes, True)  
            resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

            contador_socorro = 0
            
            if resposta == '1':
                listas(inventario, True)

            elif resposta == '2':
                paragrafo('Vamos esperar')
                contador_socorro +=1
                if contador_socorro == 3:
                    lista_opcoes.append('Aguardar por socorro')
                    personagem['Vida'] = 0
                    print('vc morreu')
                    break

            elif resposta == '3':
                paragrafo('')
                lista_opcoes.append('Entrar na floresta')
                break
            
            elif resposta == '4':
                print(personagem)
