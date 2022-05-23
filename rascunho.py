import random
import pygame

#ouros

lista_ouros=['O4','O5','O6','O7','OQ','OJ','OK','OA','O2','O3']
#espadas

lista_espadas=['E4','E5','E6','E7','EQ','EJ','EK','EA','E2','E3']
#copas

lista_copas=['C4','C5','C6','C7','CQ','CJ','CK','CA','C2','C3']
#paus

lista_paus=['P4','P5','P6','P7','PQ','PJ','PK','PA','P2','P3']

dic_valor = {'A':'ace','Q':"queen",'K':'king','J':'jack'}

pontos_d1=0
pontos_d2=0
turno=1
pontos_rodada_d1=0
pontos_rodada_d2=0

    
#lista_geral
lista_geral = []
lista_geral.extend(lista_ouros)
lista_geral.extend(lista_espadas)
lista_geral.extend(lista_copas)
lista_geral.extend(lista_paus)

#lista_jogadores e manilha
P1=[]
P2=[]
P3=[]
P4=[]

carta_tornada=random.choice(lista_geral)
lista_geral.remove(carta_tornada)

if carta_tornada in lista_ouros:
    indice=lista_ouros.index(carta_tornada)+1
if carta_tornada in lista_espadas:
    indice=lista_espadas.index(carta_tornada)+1
if carta_tornada in lista_copas:
    indice=lista_copas.index(carta_tornada)+1
if carta_tornada in lista_paus:
    indice=lista_paus.index(carta_tornada) +1
if indice==10:
    indice=0
manilhas=[lista_ouros[indice],lista_espadas[indice],lista_copas[indice],lista_paus[indice]]

while len(lista_geral)>27:
    if len(P1)<3:
        carta_sorteada=random.choice(lista_geral)
        P1.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
    if len(P2)<3:
        carta_sorteada=random.choice(lista_geral)
        P2.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
    if len(P3)<3:
        carta_sorteada=random.choice(lista_geral)
        P3.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
    if len(P4)<3:
        carta_sorteada=random.choice(lista_geral)
        P4.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
pontos_d1=0
pontos_d2=0
turno=1
pontos_rodada_d1=0
pontos_rodada_d2=0

dicionario_imagens_ouro={}
for carta in lista_ouros:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_diamonds.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_diamonds.png')
    dicionario_imagens_ouro[carta]=pygame.image.load(imagem)

dicionario_imagens_espadas = {}
for carta in lista_espadas:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_spades.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_spades.png')
    dicionario_imagens_espadas[carta]=pygame.image.load(imagem)

dicionario_imagens_copas = {}
for carta in lista_copas:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_hearts.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_hearts.png')
    dicionario_imagens_copas[carta]=pygame.image.load(imagem)

dicionario_imagens_paus = {}
for carta in lista_paus:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_clubs.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_clubs.png')
    dicionario_imagens_paus[carta]=pygame.image.load(imagem)
# dicionario_imagens_ouros = {'O4': 'cartas/4_of_diamonds.png', 'O5':'cartas/5_of_diamonds.png' ,'O6': 'cartas/6_of_diamonds.png', 'O7':'cartas/7_of_diamonds.png' , 'OQ':'cartas/queen_of_diamonds2.png' ,'OJ':'cartas/jack_of_diamonds2.png' , 'OK':'cartas/king_of_diamonds2.png' ,'OA': 'cartas/ace_of_diamonds.png', 'O2':'cartas/2_of_diamonds.png' , 'O3':'cartas/3_of_diamonds.png' }
print(dicionario_imagens_ouro)
print(dicionario_imagens_espadas)
print(dicionario_imagens_copas)
print(dicionario_imagens_paus)
# pygame.image.load("cartas/4_of_diamonds.png")

