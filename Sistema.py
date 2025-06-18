from lib.interface import *
from lib.validacao_de_dados import *
from lib.chekpoint import *
from lib.animals import *
from time import sleep

inventario = 'Inventario.txt'
if not arquivoexiste(inventario):
    criararquivo(inventario)
    coletar(inventario, 'Foto da família')

personagem = 'personagem.txt'
if not arquivoexiste(personagem):
    criararquivo(personagem)
    modificar_status(personagem)

# variaveis
lista_opcoes = []
alinhamento = 80

sleep(0.5)
titulo("JOGO DA ILHA",n=alinhamento)
sleep(0.5)

#paragrafo("O som das ondas era tudo o que David conseguia ouvir. Quando abriu os olhos, a luz do sol o cegou por um momento — e então veio a dor. Seu corpo estava dolorido, seus pulmões queimando com o sal, e à sua volta… apenas a imensidão de uma ilha desconhecida.\nHoras antes, David era apenas mais um passageiro em um navio de carga cruzando águas traiçoeiras. Uma tempestade inesperada, gritos, madeira quebrando, escuridão. Agora, sozinho e ferido, ele desperta na areia molhada, cercado por uma floresta densa e ameaçadora, sem sinal de civilização. Cada passo pode ser decisivo. Cada escolha, uma linha tênue entre a vida e a morte.\nVocê está no controle. Ajude David a explorar, sobreviver e, talvez, encontrar uma forma de voltar para casa. Mas cuidado: nesta ilha, nem tudo é o que parece… e nem todas as escolhas têm volta.\n", alinhamento=alinhamento)

#opcoes1
while True:
    sleep(0.5)
    linha('~',alinhamento)
    opcoes = ['Verificar os bolsos','Correr pela orla da praia','Procurar por sobreviventes na região', 'Adentrar na floresta','Status do personagem']
    listas(opcoes, True)  
    resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')
    linha('-',alinhamento)

    if resposta == '1':
        if len(inventario) == 0:
            paragrafo('Inventario vazio!',0.05)
            sleep(0.5)
        else:
            ver_itens(inventario, n_em_item=True)

    elif resposta == '2':
        paragrafo('Você corre pela orla, mas não encontra nada nem ninguem.',alinhamento=alinhamento)
        lista_opcoes.append('Correr pela orla da praia')
        break

    elif resposta == '3':
        paragrafo('Editar',alinhamento=alinhamento)
        lista_opcoes.append('Procurar por sobreviventes na região')
        break

    elif resposta == '4':
        paragrafo('Editar',alinhamento=alinhamento)
        lista_opcoes.append('Entrar na floresta 1')
        break

    elif resposta == '5':
        ver_status(personagem)


#opção2
if lista_opcoes[0] == 'Correr pela orla da praia':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Continuar à correr desesperado','Entrar na floresta','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você continua a correr desesperado e sem rumo, até chegar em um paredão, suas escolhas são poucas agora.',alinhamento=alinhamento)
          lista_opcoes.append('Continuar à correr desesperado')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Entrar na floresta 2')
            break
        
        elif resposta == '4':
          ver_status(personagem)

elif lista_opcoes[0] == 'Procurar por sobreviventes na região':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Continuar procurando na região','Entrar na floresta','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Editar',alinhamento=alinhamento)
          lista_opcoes.append('Continuar procurando na região')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Entrar na floresta 1')
            break
        
        elif resposta == '4':
          ver_status(personagem)

elif lista_opcoes[0] == 'Entrar na floresta 1':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Editar','Editar','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Editar',alinhamento=alinhamento)
          lista_opcoes.append('Editar')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
          ver_status(personagem)

#opção3
#Correr pela orla
if lista_opcoes[1] == 'Continuar à correr desesperado':
    contador_socorro = 0
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Aguardar por socorro','Entrar na floresta','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)
                    
        elif resposta == '2':
            if contador_socorro == 0:
                paragrafo('Você senta na areia e aguarda por resgate',alinhamento=alinhamento)
            elif contador_socorro == 1:
                paragrafo('Depois de muito aguardar você se sente triste',alinhamento=alinhamento)
            elif contador_socorro == 2:
                paragrafo('Depois de aguardar por uma eternidade, sozinho triste e sem esperanças.',alinhamento=alinhamento)
                paragrafo("Você desiste.", alinhamento=alinhamento)
                print()

            contador_socorro += 1
            if contador_socorro == 3:
                lista_opcoes.append('Aguardar por socorro')
                print('The end')
                print("Parabens final secreto!")
                break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Entrar na floresta 3')
            #Ex atacado por animal
            modificar_status(personagem, int(pegar_status(personagem,0))-urso()['Forca'])
            break
        
        elif resposta == '4':
            ver_status(personagem)

elif lista_opcoes[1] == 'Entrar na floresta 2':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Editar','Editar','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Editar',alinhamento=alinhamento)
          lista_opcoes.append('Editar')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#Procurar por sobreviventes
if lista_opcoes[1] == 'Continuar procurando na região':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Editar','Editar','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Editar',alinhamento=alinhamento)
          lista_opcoes.append('Editar')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
            ver_status(personagem)

elif lista_opcoes[1] == 'Entrar na floresta 1':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Editar','Editar','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Editar',alinhamento=alinhamento)
          lista_opcoes.append('Editar')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#Entrar na floresta 1
if lista_opcoes[1] == 'Editar':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Editar','Editar','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Editar',alinhamento=alinhamento)
          lista_opcoes.append('Editar')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
            ver_status(personagem)

elif lista_opcoes[1] == 'Editar':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Editar','Editar','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Editar',alinhamento=alinhamento)
          lista_opcoes.append('Editar')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
            ver_status(personagem)

ver_status(personagem)