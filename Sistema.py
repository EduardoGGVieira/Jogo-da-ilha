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
        paragrafo('Você procura por sinal de sobreviventes, mas não encontra nada nem sinal de vida.',alinhamento=alinhamento)
        lista_opcoes.append('Procurar por sobreviventes na região')
        break

    elif resposta == '4':
        paragrafo('Sem muita vontade, sua única chance é tentar a sorte na floresta.',alinhamento=alinhamento)
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
        linha('-',alinhamento)

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
            paragrafo('Sem muita vontade, sua única chance é tentar a sorte na floresta.',alinhamento=alinhamento)
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
        paragrafo('',alinhamento=alinhamento)


        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Voce ainda acha que pode achar algo últil, e continua procurando.',alinhamento=alinhamento)
          lista_opcoes.append('Continuar procurando na região')
          break

        elif resposta == '3':
            paragrafo('editar',alinhamento=alinhamento)
            lista_opcoes.append('Entrar na floresta 1')
            break
        
        elif resposta == '4':
          ver_status(personagem)

elif lista_opcoes[0] == 'Entrar na floresta 1':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você escuta oque parece um riacho e decide investigar','Você apeanas anda em linha reta','Status do personagem']
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
                paragrafo('Depois de aguardar por uma eternidade, sozinho, triste e sem esperanças.',alinhamento=alinhamento)
                paragrafo("Você desiste e morre.", alinhamento=alinhamento)
                print()

            contador_socorro += 1
            if contador_socorro == 3:
                lista_opcoes.append('Aguardar por socorro')
                print('The end')
                print("Parabens final secreto!")
                break

        elif resposta == '3':
            paragrafo('Sem muita vontade, sua única chance é tentar a sorte na floresta.',alinhamento=alinhamento)
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
        opcoes = ['Verificar os bolsos','Continuar a andar em linha reta','Procurar por sinal de sobreviventes','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você se depara com um guaxinin!',alinhamento=alinhamento)
          lista_opcoes.append('guaxinin')
          break

        elif resposta == '3':
            paragrafo('Você encontra pegadas de sobreviventes e decide seguir.',alinhamento=alinhamento)
            lista_opcoes.append('vestigios de sobreviventes')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#guaxinin
if lista_opcoes[2] == 'guaxinin':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você decide fugir do guaxinin','Você decide atacar o guaxinin','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')
        linha('-',alinhamento)

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Voce foge do guaxinin correndo',alinhamento=alinhamento)
          lista_opcoes.append('correr do guaxinin')
          break

        elif resposta == '3':
            paragrafo('Você ataca o guaxinin',alinhamento=alinhamento)
            lista_opcoes.append('atacar o guaxinin')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#FUGIR DO GUAXININ
if lista_opcoes[3] == 'correr do guaxinin':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você continua correndo desesperado','Você atavessa um riacho raso','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')
        linha('-',alinhamento)

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você tropeça e se rala, mas chega em uma clareira.',alinhamento=alinhamento)
          lista_opcoes.append('clareira')
          break

        elif resposta == '3':
            paragrafo('Você fica molhado, mas chega em um local com vestigios de sobreviventes',alinhamento=alinhamento)
            lista_opcoes.append('vestigios')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#ATACAR O GUAXININ
elif lista_opcoes[3] == 'atacar o guaxinin':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Matar o guaxinin','Afugentar o guaxinin','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você não conseguiu matar o guaxinin e ficou muito machucado.',alinhamento=alinhamento)   #PERDE VIDA
          lista_opcoes.append('muito machucado pelo guaxinin')
          break

        elif resposta == '3':
            paragrafo('Você afugentou o guaxinin, mas ficou um pouco machucado.',alinhamento=alinhamento)
            lista_opcoes.append('um pouco machucado pelo guaxinin')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#Depois do guaxinin
if lista_opcoes[4] == 'muito machucado pelo guaxinin':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você anda em direção a vozes na mata.','Você decide descansar um pouco.','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você anda muito devagar devido aos ferimentos, mas encontra um grupo de sobreviventes.',alinhamento=alinhamento)
          lista_opcoes.append('Ponto de salvamento 1')
          break

        elif resposta == '3':
            paragrafo('Você para e recupera o folego.',alinhamento=alinhamento)
            lista_opcoes.append('Ponto de salvamento 2')
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

#vestigios de sobreviventes
if lista_opcoes[2] == 'vestigios de sobreviventes':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você encontra um acampamento abandonado','Você continua a seguir as pegadas','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')
        linha('-',alinhamento)

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você percebe que ali tem vestigios recentes de humanos, sobreviventes talvez?',alinhamento=alinhamento)
          lista_opcoes.append('acampamento')
          break

        elif resposta == '3':
            paragrafo('Você segue por um caminho ingrime que o leva até o outro lado da ilha.',alinhamento=alinhamento)
            lista_opcoes.append('continuar a seguir as pegadas')
            break
        
        elif resposta == '4':
            ver_status(personagem)
            
        
elif lista_opcoes[2] == 'acampamento':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você desncansa no acampamento','Você segue em frente','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você consegue um lugar para descansar e beber um pouco de água.',alinhamento=alinhamento)
          lista_opcoes.append('após o descanso')
          break

        elif resposta == '3':
            paragrafo('Você sente que está chegando mais perto de encontrar alguém.',alinhamento=alinhamento)
            lista_opcoes.append('ponto de salvamento 1')
            break
        
        elif resposta == '4':
            ver_status(personagem)


#Seguir em frente
if lista_opcoes[2] == 'após o descanso':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você decide continuar sua trilha','Você decide escalar um morro','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você chega do outro lado da ilha e encontra um grupo de sobreviventes',alinhamento=alinhamento)
          lista_opcoes.append('')
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
            ver_status(personagem)

elif lista_opcoes[2] == 'Editar':
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
        opcoes = ['Verificar os bolsos','Você avista um bau na água e decide pegar','Você desiste e vai para a floresta','Status do personagem']
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

#Entrar na floresta 2
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