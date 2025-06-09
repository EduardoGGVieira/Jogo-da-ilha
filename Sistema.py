from lib.interface import *
from lib.validacao_de_dados import *

titulo("JOGO DA ILHA",n=40)

paragrafo("blalblaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabla\n")

opcoes = ['Primeira opção','Segunda']
listas(opcoes, True)

print(contagem_itens(opcoes))
apenasitem(contagem_itens(opcoes), 'Sua opção: ')

# problema que não considera a ultima opção pois a contagem começa em 0