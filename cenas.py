from lib.chekpoint import *
from lib.interface import *
from lib.validacao_de_dados import *
from lib.animals import *
from random import choice
from time import sleep

ALINHAMENTO = 80


#CENAS PRINCIPAIS 


def cena_praia(personagem, inventario):
    paragrafo("O som das ondas era tudo o que David conseguia ouvir. Quando abriu os olhos, a luz do sol o cegou por um momento — e então veio a dor. "
              "Seu corpo estava dolorido, seus pulmões queimando com o sal, e à sua volta… apenas a imensidão de uma ilha desconhecida."
              "\nHoras antes, David era apenas mais um passageiro em um navio de carga cruzando águas traiçoeiras. Uma tempestade inesperada, gritos, madeira quebrando, escuridão. "
              "Agora, sozinho e ferido, ele desperta na areia molhada, cercado por uma floresta densa e ameaçadora, sem sinal de civilização. Cada passo pode ser decisivo. "
              "Cada escolha, uma linha tênue entre a vida e a morte.\nVocê está no controle. Ajude David a explorar, sobreviver e, talvez, encontrar uma forma de voltar para casa. "
              "Mas cuidado: nesta ilha, nem tudo é o que parece… e nem todas as escolhas têm volta.\n", alinhamento=ALINHAMENTO)
    sleep(0.5)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Correr pela orla': 'cena_orla_1',
        'Procurar por sobreviventes': 'cena_busca_sobreviventes',
        'Adentrar a floresta': 'cena_floresta_1',
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha_idx = int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1
        escolha_txt = opcoes[escolha_idx]

        if escolha_txt == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha_txt == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            paragrafo(f'Você decide: {escolha_txt.lower()}...', alinhamento=ALINHAMENTO)
            return transicoes[escolha_txt]


# CENA 1A – Orla («Correr pela orla» na cena da praia)

def cena_orla_1(personagem, inventario):
    paragrafo('Você corre pela orla, mas não encontra ninguém.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Continuar correndo pela orla': 'cena_orla_2',
        'Sentar e esperar': 'cena_orla_espera_0',
        'Entrar na floresta': 'cena_floresta_2'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha_txt = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha_txt == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha_txt == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            paragrafo(f'Você decide: {escolha_txt.lower()}...', alinhamento=ALINHAMENTO)
            return transicoes[escolha_txt]


# CENA 1A.1 – Trilogia do "Aguardar por socorro" (final secreto)

def _espera_template(personagem, inventario, etapa):
    textos = [
        'Você senta na areia e aguarda por resgate.',
        'Depois de muito aguardar você se sente triste.',
        'Depois de aguardar por uma eternidade, sozinho, triste e sem esperanças. Você desiste e morre.'
    ]
    paragrafo(textos[etapa], alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    if etapa == 2:
        paragrafo('THE END – Final secreto conquistado!', alinhamento=ALINHAMENTO)
        return 'fim_de_jogo'

    proxima = f'cena_orla_espera_{etapa + 1}'
    transicoes = {'Aguardar por socorro': proxima, 'Entrar na floresta': 'cena_floresta_3'}
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha_txt = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha_txt == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha_txt == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            paragrafo(f'Você decide: {escolha_txt.lower()}...', alinhamento=ALINHAMENTO)
            return transicoes[escolha_txt]

def cena_orla_espera_0(personagem, inventario):
    return _espera_template(personagem, inventario, 0)

def cena_orla_espera_1(personagem, inventario):
    return _espera_template(personagem, inventario, 1)

def cena_orla_espera_2(personagem, inventario):
    return _espera_template(personagem, inventario, 2)


# CENA 1B – Buscar sobreviventes («Procurar por sobreviventes»)

def cena_busca_sobreviventes(personagem, inventario):
    paragrafo('Você procura por sinal de sobreviventes, mas não encontra nada nem sinal de vida.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Continuar procurando na região': 'cena_continua_procurando',
        'Entrar na floresta': 'cena_floresta_1'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha_txt = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha_txt == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha_txt == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            paragrafo(f'Você decide: {escolha_txt.lower()}...', alinhamento=ALINHAMENTO)
            return transicoes[escolha_txt]

def cena_continua_procurando(personagem, inventario):
    paragrafo('Você ainda acha que pode encontrar algo útil e continua procurando.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Avistar um baú na água': 'cena_bau',
        'Desistir e ir para a floresta': 'cena_floresta_1'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            paragrafo(f'Você decide: {escolha.lower()}...', alinhamento=ALINHAMENTO)
            return transicoes[escolha]

def cena_bau(personagem, inventario):
    paragrafo('Você encontra um baú na água com alguns pertences.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    coletar(inventario, 'lanterna')
    paragrafo('Uma lanterna foi adicionada ao seu inventário!', alinhamento=ALINHAMENTO)
    return 'cena_floresta_1'
def cena_orla_2(personagem, inventario):
    paragrafo('Você corre mais uma vez pela orla. O sol já começa a se pôr e o vento traz um cheiro estranho do interior da ilha.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Voltar para a praia': 'cena_praia',
        'Adentrar a floresta': 'cena_floresta_urso'
    }
    opcoes = list(transicoes.keys()) + ['Verificar os bolsos', 'Status do personagem']

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
        else:
            return transicoes[escolha]
        

#Continuar a correr pela orla.

def cena_orla_2(personagem, inventario):
    paragrafo('Você corre mais uma vez pela orla. O sol já começa a se pôr e o vento traz um cheiro estranho do interior da ilha.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Voltar para a praia': 'cena_praia',
        'Adentrar a floresta': 'cena_floresta_urso'
    }
    opcoes = list(transicoes.keys()) + ['Verificar os bolsos', 'Status do personagem']

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
        else:
            return transicoes[escolha]


#Evento do urso na floresta

def cena_floresta_urso(personagem, inventario):
    paragrafo('A floresta se fecha ao seu redor. Você ouve um rosnado. Um urso enorme surge entre as árvores!', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Lutar contra o urso': 'cena_luta_urso',
        'Tentar fugir': 'cena_fuga_urso'
    }
    opcoes = list(transicoes.keys()) + ['Verificar os bolsos', 'Status do personagem']

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
        else:
            return transicoes[escolha]
        
def cena_luta_urso(personagem, inventario):
    paragrafo('Você tenta lutar com o urso! Isso pode ser suicídio...', alinhamento=ALINHAMENTO)
    dano = urso()['Forca']
    modificar_status(personagem, int(pegar_status(personagem, 0)) - dano)
    if int(pegar_status(personagem, 0)) <= 0:
        return 'fim_morte_urso'
    else:
        return 'cena_ponto_salvamento_2'

def cena_fuga_urso(personagem, inventario):
    paragrafo('Você tenta fugir do urso. Seu destino será decidido pela sorte...', alinhamento=ALINHAMENTO)
    opcao = input('\nDigite F para fugir ou qualquer outra tecla para hesitar: ').strip().upper()
    if opcao == 'F':
        if choice([True, False]):
            paragrafo('Você consegue escapar por pouco!', alinhamento=ALINHAMENTO)
            return 'cena_ponto_salvamento_2'
        else:
            return 'fim_morte_urso'
    else:
        return 'fim_morte_urso'


# FINAL – Morte pelo urso

def fim_morte_urso(personagem, inventario):
    paragrafo('O urso avança ferozmente. Você não tem chance. Seus gritos ecoam pela floresta até o silêncio reinar.', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'


# CENA 2 – Floresta (primeira entrada)

def cena_floresta_1(personagem, inventario):
    paragrafo('Sem muita vontade, sua única chance é tentar a sorte na floresta.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Investigar o som de água corrente': 'cena_encontra_sobreviventes',
        'Andar em linha reta': 'cena_insetos'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            paragrafo(f'Você decide: {escolha.lower()}...', alinhamento=ALINHAMENTO)
            return transicoes[escolha]

#Encontrar sobreviventes
def cena_encontra_sobreviventes(personagem, inventario):
    paragrafo('Você chega a uma clareira com um pequeno rio e percebe vestígios de um acampamento.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Gritar para um barco próximo': 'final_barco',
        'Correr em direção ao barco': 'final_barco'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]

#Ataque de insetos
def cena_insetos(personagem, inventario):
    paragrafo('Sem entender nada, você começa a ser atacado por um enxame de insetos!', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Tentar se defender': ('cena_machucado_insetos', 'total'),
        'Correr para longe': ('cena_machucado_insetos', 'parcial')
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            if transicoes[escolha][1] == 'total':
                dano = insetos()['Forca']
            else:
                dano = insetos()['Forca'] // 2
            modificar_status(personagem, int(pegar_status(personagem, 0)) - dano)
            return transicoes[escolha][0]

def cena_machucado_insetos(personagem, inventario):
    paragrafo('Coberto de picadas, você sente seu corpo latejar.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Seguir sons na mata': 'cena_sobreviventes_machucado'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]

def cena_sobreviventes_machucado(personagem, inventario):
    paragrafo('Você anda devagar devido aos ferimentos, mas encontra um grupo de sobreviventes.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    return 'final_resgatado_machucado'

# CENA 2A – Floresta (entrada pela orla, rota 2)
def cena_floresta_2(personagem, inventario):
    paragrafo('Você se embrenha na floresta por um caminho diferente.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Continuar em linha reta': 'cena_guaxinin',
        'Procurar por sinais de sobreviventes': 'cena_vestigios_sobreviventes'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]

#Guaxinim
def cena_guaxinin(personagem, inventario):
    paragrafo('Você se depara com um guaxinim!', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Fugir do guaxinim': 'cena_fuga_guaxinin',
        'Atacar o guaxinim': 'cena_ataque_guaxinin'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]

def cena_fuga_guaxinin(personagem, inventario):
    paragrafo('Você foge do guaxinim correndo!', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Continuar correndo': 'cena_tropeca_clareira',
        'Atravessar um riacho raso': 'cena_molhado_vestigios'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]
        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]

def cena_ataque_guaxinin(personagem, inventario):
    paragrafo('Você decide atacar o guaxinim!', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Tentar matar o guaxinim': 'cena_machucado_guaxinin_total',
        'Afugentar o guaxinim': 'cena_machucado_guaxinin_parcial'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]

        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            if escolha == 'Tentar matar o guaxinim':
                dano = Guaxinin()['Forca']
            else:
                dano = 30  # Dano parcial fixo
            modificar_status(personagem, int(pegar_status(personagem, 0)) - dano)
            return transicoes[escolha]

def cena_machucado_guaxinin_total(personagem, inventario):
    paragrafo('Você saiu muito machucado da luta contra o guaxinim. Cada passo é uma tortura, mas você avança.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    paragrafo('Ao longe, você avista fumaça — talvez um acampamento. Com esforço, você alcança um grupo de pessoas que também caíram ali. Eles cuidam de você.', alinhamento=ALINHAMENTO)
    return 'cena_acampamento_guaxinim'

def cena_machucado_guaxinin_parcial(personagem, inventario):
    paragrafo('Você afugentou o guaxinim, mas ficou um pouco machucado.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    return 'cena_ponto_salvamento_1'

def cena_acampamento_guaxinim(personagem, inventario):
    paragrafo('O grupo conta que o guaxinim fazia parte de um experimento secreto em uma base oculta na ilha.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)
    transicoes = {
        'Investigar a base secreta': 'cena_base_secreta',
        'Esperar por resgate': 'final_guaxinim_resgatado'
    }
    opcoes = list(transicoes.keys()) + ['Verificar os bolsos', 'Status do personagem']
    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]
        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
        else:
            return transicoes[escolha]

#Depois do guaxinim
def cena_tropeca_clareira(personagem, inventario):
    paragrafo('Você tropeça e se rala, mas chega em uma clareira.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    return 'cena_ponto_salvamento_2'

def cena_molhado_vestigios(personagem, inventario):
    paragrafo('Você fica molhado atravessando o riacho e encontra vestígios de sobreviventes.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    return 'cena_ponto_salvamento_1'

def cena_base_secreta(personagem, inventario):
    paragrafo('Você encontra a entrada de um laboratório escondido sob uma formação rochosa. Dentro, arquivos revelam experiências com animais geneticamente modificados.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    return 'final_base_secreta'

def final_base_secreta(personagem, inventario):
    paragrafo('Você descobre segredos obscuros e envia provas via rádio. Um resgate é enviado por autoridades. FIM!', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

def final_guaxinim_resgatado(personagem, inventario):
    paragrafo('Você é resgatado e descobre que o guaxinim era um animal de laboratório que escapou de um experimento secreto. A ilha guardava mais mistérios do que você imaginava.', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

#Vestígios de sobreviventes
def cena_vestigios_sobreviventes(personagem, inventario):
    paragrafo('Você encontra pegadas que parecem recentes e decide seguir.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Investigar acampamento abandonado': 'cena_acampamento',
        'Continuar seguindo as pegadas': 'cena_outro_lado_ilha'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]
        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]

def cena_acampamento(personagem, inventario):
    paragrafo('O acampamento parece ter sido abandonado recentemente – há um rádio emitindo um SOS.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    return 'final_resgate_radio'

def cena_outro_lado_ilha(personagem, inventario):
    paragrafo('Depois de muito esforço, você chega ao outro lado da ilha.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Gritar para um barco distante': 'final_barco_nao_veio',
        'Correr em direção ao barco': 'final_barco_viu'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]
        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]

#FINAIS 
def final_barco(personagem, inventario):
    paragrafo('Você é resgatado por um grupo de sobreviventes que navegava por perto. FIM!', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

def final_resgatado_machucado(personagem, inventario):
    paragrafo('Apesar dos ferimentos, você é resgatado e levado para um abrigo seguro. FIM!', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

def final_resgate_radio(personagem, inventario):
    paragrafo('Você usa o rádio para chamar ajuda e um helicóptero chega algumas horas depois. FIM!', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

def final_barco_viu(personagem, inventario):
    paragrafo('Correndo e acenando freneticamente, você consegue chamar atenção do barco, que vem resgatá-lo. FIM!', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

def final_barco_nao_veio(personagem, inventario):
    paragrafo('Você grita, mas o barco segue sem notar sua presença. Você precisará encontrar outra saída…', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

# Pontos de salvamento
def cena_ponto_salvamento_1(personagem, inventario):
    paragrafo('Os sobreviventes o conduzem até um ponto de resgate improvisado. FIM!', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

def cena_ponto_salvamento_2(personagem, inventario):
    paragrafo('Na clareira você encontra um helicóptero de busca que pousa para socorrê-lo. FIM!', alinhamento=ALINHAMENTO)
    return 'fim_de_jogo'

# CENA 2B – Floresta (entrada pela espera, rota 3)
def cena_floresta_3(personagem, inventario):
    paragrafo('Você entra na floresta após esperar por socorro, exausto.', alinhamento=ALINHAMENTO)
    sleep(0.5)
    linha('~', ALINHAMENTO)

    transicoes = {
        'Procurar por água': 'cena_encontra_sobreviventes',
        'Descansar na sombra': 'cena_ponto_salvamento_1'
    }
    acoes_especiais = ['Verificar os bolsos', 'Status do personagem']
    opcoes = list(transicoes.keys()) + acoes_especiais

    while True:
        mostrar_opcoes(opcoes)
        escolha = opcoes[int(apenasitem(contagem_itens(opcoes), '\nSua opção: ')) - 1]
        if escolha == 'Verificar os bolsos':
            ver_itens(inventario, True)
            sleep(0.5)
        elif escolha == 'Status do personagem':
            ver_status(personagem)
            sleep(0.5)
        else:
            return transicoes[escolha]