from lib.chekpoint import *
from cenas import *

inventario = 'inventario.txt'

# Cria o arequivo inventario se nao existir
if not arquivoexiste(inventario):
    criararquivo(inventario)
    coletar(inventario, 'Foto da família')

personagem = 'personagem.txt'

# Cria o arquivo personagem se nao existir
if not arquivoexiste(personagem):
    criararquivo(personagem)
    modificar_status(personagem)

titulo("JOGO DA ILHA",n=ALINHAMENTO)
sleep(1)

# Executa o loop de verificação das cenas até que o fim do jogo seja decretado
cena_atual = 'cena_praia'
while cena_atual != 'fim_de_jogo':
    try:
        match cena_atual:
            case 'cena_praia':
                cena_atual = cena_praia(personagem, inventario)
            case 'cena_orla_1':
                cena_atual = cena_orla_1(personagem, inventario)
            case 'cena_orla_2':
                cena_atual = cena_orla_2(personagem, inventario)
            case 'cena_floresta_urso':
                cena_atual = cena_floresta_urso(personagem, inventario)
            case 'cena_luta_urso':
                cena_atual = cena_luta_urso(personagem, inventario)
            case 'cena_fuga_urso':
                cena_atual = cena_fuga_urso(personagem, inventario)
            case 'fim_morte_urso':
                cena_atual = fim_morte_urso(personagem, inventario)
            case 'cena_orla_espera_0':
                cena_atual = cena_orla_espera_0(personagem, inventario)
            case 'cena_orla_espera_1':
                cena_atual = cena_orla_espera_1(personagem, inventario)
            case 'cena_orla_espera_2':
                cena_atual = cena_orla_espera_2(personagem, inventario)
            case 'cena_busca_sobreviventes':
                cena_atual = cena_busca_sobreviventes(personagem, inventario)
            case 'cena_continua_procurando':
                cena_atual = cena_continua_procurando(personagem, inventario)
            case 'cena_bau':
                cena_atual = cena_bau(personagem, inventario)
            case 'cena_floresta_1':
                cena_atual = cena_floresta_1(personagem, inventario)
            case 'cena_encontra_sobreviventes':
                cena_atual = cena_encontra_sobreviventes(personagem, inventario)
            case 'cena_insetos':
                cena_atual = cena_insetos(personagem, inventario)
            case 'cena_machucado_insetos':
                cena_atual = cena_machucado_insetos(personagem, inventario)
            case 'cena_sobreviventes_machucado':
                cena_atual = cena_sobreviventes_machucado(personagem, inventario)
            case 'cena_floresta_2':
                cena_atual = cena_floresta_2(personagem, inventario)
            case 'cena_guaxinin':
                cena_atual = cena_guaxinin(personagem, inventario)
            case 'cena_fuga_guaxinin':
                cena_atual = cena_fuga_guaxinin(personagem, inventario)
            case 'cena_ataque_guaxinin':
                cena_atual = cena_ataque_guaxinin(personagem, inventario)
            case 'cena_machucado_guaxinin_total':
                cena_atual = cena_machucado_guaxinin_total(personagem, inventario)
            case 'cena_machucado_guaxinin_parcial':
                cena_atual = cena_machucado_guaxinin_parcial(personagem, inventario)
            case 'cena_acampamento_guaxinim':
                cena_atual = cena_acampamento_guaxinim(personagem, inventario)
            case 'final_base_secreta':
                cena_atual = final_base_secreta(personagem, inventario)
            case 'final_guaxinim_resgatado':
                cena_atual = final_guaxinim_resgatado(personagem, inventario)
            case 'cena_base_secreta':
                cena_atual = cena_base_secreta(personagem, inventario)
            case 'cena_tropeca_clareira':
                cena_atual = cena_tropeca_clareira(personagem, inventario)
            case 'cena_molhado_vestigios':
                cena_atual = cena_molhado_vestigios(personagem, inventario)
            case 'cena_vestigios_sobreviventes':
                cena_atual = cena_vestigios_sobreviventes(personagem, inventario)
            case 'cena_acampamento':
                cena_atual = cena_acampamento(personagem, inventario)
            case 'cena_outro_lado_ilha':
                cena_atual = cena_outro_lado_ilha(personagem, inventario)
            case 'cena_floresta_3':
                cena_atual = cena_floresta_3(personagem, inventario)
            case 'final_barco':
                cena_atual = final_barco(personagem, inventario)
            case 'final_resgatado_machucado':
                cena_atual = final_resgatado_machucado(personagem, inventario)
            case 'final_resgate_radio':
                cena_atual = final_resgate_radio(personagem, inventario)
            case 'final_barco_viu':
                cena_atual = final_barco_viu(personagem, inventario)
            case 'final_barco_nao_veio':
                cena_atual = final_barco_nao_veio(personagem, inventario)
            case 'cena_ponto_salvamento_1':
                cena_atual = cena_ponto_salvamento_1(personagem, inventario)
            case 'cena_ponto_salvamento_2':
                cena_atual = cena_ponto_salvamento_2(personagem, inventario)
            case 'final_guaxinim_resgatado':
                cena_atual = final_guaxinim_resgatado(personagem, inventario)
            case _:
                print(f'Erro: Cena "{cena_atual}" não encontrada.')
                cena_atual = 'fim_de_jogo'
    except Exception as e:
        print(f'Erro durante a execução da cena: {e}')
        cena_atual = 'fim_de_jogo'