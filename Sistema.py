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

#CAMINHOS
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


#ENTRA NA FLORESTA EM B OU VAI PARA C
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

#PROCURA EM A OU ENTRA NA FLORESTA EM A
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
            paragrafo('Sem muita vontade, sua única chance é tentar a sorte na floresta.',alinhamento=alinhamento)
            lista_opcoes.append('Entrar na floresta 1')
            break
        
        elif resposta == '4':
          ver_status(personagem)

#ENTRAR NA FLORESTA EM A
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
          paragrafo('Você chega em uma clareira com um pequeno rio,e percebe vestigios de um acampamento',alinhamento=alinhamento)
          lista_opcoes.append('acampamento A')
          break

        elif resposta == '3':
            paragrafo('Sem entender nada, você começa a ser atacado por um enxame de insetos!',alinhamento=alinhamento)
            lista_opcoes.append('insetos')
            break
        
        elif resposta == '4':
          ver_status(personagem)

#ATACADO POR INSETOS A
if lista_opcoes[1] == 'insetos':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você tenta se defender dos insetos','Você tenta correr para longe dos insetos','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você consegue se defender, mas fica com algumas picadas.',alinhamento=alinhamento)
          modificar_status(personagem, int(pegar_status(personagem,0))-insetos()['Forca']) # Leva dano total
          lista_opcoes.append('muito machucado pelos insetos')
          break

        elif resposta == '3':
            paragrafo('Você consegue correr, mas fica com algumas picadas.',alinhamento=alinhamento)
            modificar_status(personagem, int(pegar_status(personagem,0))-insetos()['Forca']//2) # Leva um pouco de dano
            lista_opcoes.append('um pouco machucado pelos insetos')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#Depois de ser atacado pelos insetos A
if lista_opcoes[2] == 'muito machucado pelos insetos':
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
            paragrafo('Você para e recupera o folego, e depois decide seguir em frente.',alinhamento=alinhamento)
            lista_opcoes.append('ponto de resgate')
            break
        
        elif resposta == '4':
            ver_status(personagem)
#Depois de ser atacado pelos insetos A
elif lista_opcoes[2] == 'um pouco machucado pelos insetos':
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
          paragrafo('Você anda devagar devido aos ferimentos, mas encontra um grupo de sobreviventes.',alinhamento=alinhamento)
          lista_opcoes.append('Ponto de salvamento 1')
          break

        elif resposta == '3':
            paragrafo('Você para e recupera o folego, e depois decide seguir em frente.',alinhamento=alinhamento)
            lista_opcoes.append('ponto de resgate')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#ACHA O ACAMPAMENTO EM A
if lista_opcoes[9] == 'acampamento A':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você investiga o acampamento','Você ignora o acampamento e continua reto','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você econtra um rádio que está trasmitindo uma mensagem de S.O.S.',alinhamento=alinhamento)
          lista_opcoes.append('Resgate em A')
          break

        elif resposta == '3':
            paragrafo('Você contina a caminhar até chegar do outro lado da ilha.',alinhamento=alinhamento)
            lista_opcoes.append('outro lado da ilha A')
            break
        
        elif resposta == '4':
            ver_status(personagem)
#É SALVO PELO BARCO OU NÃO A
elif lista_opcoes[9] == 'outro lado da ilha A':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você avista um barco e decide gritar.','Você avista um barco e decide correr.','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('De nada adianta, pois o barco está longe no mar',alinhamento=alinhamento)
          lista_opcoes.append('Barco não viu')
          break

        elif resposta == '3':
            paragrafo('Você decide correr até que alguém do barco o veja e da certo!',alinhamento=alinhamento)
            lista_opcoes.append('Barco viu você')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#opção3
#Correr até o caminho C
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

#CAMINHO B 1 E 2
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

#guaxinin CAMINHO 1B
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

#FUGIR DO GUAXININ 1B
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
          lista_opcoes.append('Ponto de salvamento 2')
          break

        elif resposta == '3':
            paragrafo('Você fica molhado, mas chega em um local com vestigios de sobreviventes',alinhamento=alinhamento)
            lista_opcoes.append('Ponto de salvamento 1')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#ATACAR O GUAXININ 1B
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
          modificar_status(personagem, int(pegar_status(personagem,0))-Guaxinin()['Forca']) # Leva dano total
          break

        elif resposta == '3':
            paragrafo('Você afugentou o guaxinin, mas ficou um pouco machucado.',alinhamento=alinhamento)
            lista_opcoes.append('um pouco machucado pelo guaxinin')
            modificar_status(personagem, int(pegar_status(personagem,0))-Guaxinin()['30']) # Leva um pouco de dano
            break
        
        elif resposta == '4':
            ver_status(personagem)

#Depois do guaxinin 1B
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
            paragrafo('Você para e recupera o folego, e depois decide seguir em frente.',alinhamento=alinhamento)
            lista_opcoes.append('ponto de resgate')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#DEPOIS DE LUTAR COM O GUAX, VC É RESGATADO POR UM BARCO 1B
elif lista_opcoes[4] == 'ponto de resgate':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você avista um barco e decide gritar.','Você avista um barco e decide correr.','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('De nada adianta, pois o barco está longe no mar.',alinhamento=alinhamento)
          lista_opcoes.append('Barco não viu')
          break

        elif resposta == '3':
            paragrafo('Você decide correr até que alguém do barco o veja e da certo!',alinhamento=alinhamento)
            lista_opcoes.append('Barco viu você')
            break
        
        elif resposta == '4':
            ver_status(personagem)
#vestigios de sobreviventes do caminho 2B
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
#Procurar por sobreviventes CAMINHO A
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
          paragrafo('Você econtra um bau, com alguns pertences na água',alinhamento=alinhamento)
          lista_opcoes.append('Continua no caminho A')
          inventario.append('lanterna') #ta certo assim?
          break

        elif resposta == '3':
            paragrafo('Editar',alinhamento=alinhamento)
            lista_opcoes.append('Editar')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#CAMINHO C
elif lista_opcoes[1] == 'Entrar na floresta 3':
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
          paragrafo('Você chega em uma clareira com um pequeno rio,e percebe vestigios de um acampamento',alinhamento=alinhamento)
          lista_opcoes.append('acampamento C')
          break

        elif resposta == '3':
            paragrafo('Sem entender nada, você começa a ser atacado por um enxame de insetos!',alinhamento=alinhamento)
            lista_opcoes.append('insetos')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#EVENTO DO BARCO PRA OS CAMINHOS A B c
if lista_opcoes[8] == 'Barco viu você':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você corre em direção ao barco','Você fica parado no lugar esperando','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Você está tão aliviado que corre até o barco para ser resgatado.',alinhamento=alinhamento)
          lista_opcoes.append('Final do barco')
          print('Paraben você foi resgatado por um grupo de sobreviventes e está salvo!')
          break

        elif resposta == '3':
            paragrafo('Você está tão aliviado que apenas estpera o resgate vir até você.',alinhamento=alinhamento)
            lista_opcoes.append('Final do barco')
            print('Paraben você foi resgatado por um grupo de sobreviventes e está salvo!')
            break
        
        elif resposta == '4':
            ver_status(personagem)

#EVENTO ACAMPAMENTO A
if lista_opcoes[11] == 'Ponto de salvamento 1':
    while True:
        sleep(0.5)
        linha('~',alinhamento)
        opcoes = ['Verificar os bolsos','Você segue os sobreviventes até um local de resgate','Status do personagem']
        listas(opcoes, True)  
        resposta = apenasitem(contagem_itens(opcoes), '\nSua opção: ')

        if resposta == '1':
            if len(inventario) == 0:
                paragrafo('Inventario vazio!',0.05)
                sleep(0.5)
            else:
                ver_itens(inventario, True)

        elif resposta == '2':
          paragrafo('Depois de muito tempo tentando você finalmente consegue fugir da ilha com alguns sobreviventes, um pouco ferido e com fome mas dá tudo certo!',alinhamento=alinhamento)
          lista_opcoes.append('Final do Jogo')
          print('Paraben você foi resgatado por um grupo de sobreviventes e está salvo!')
          break
        elif resposta == '4':
            ver_status(personagem)
#FINAL DO JOGO CAMINHO A
elif lista_opcoes[11] == 'final do jogo':
    print('Muito obrigado por jogar, espero que tenha gostado!')
            