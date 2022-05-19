import random

#ouros

lista_ouros=['O4','O5','O6','O7','OQ','OJ','OK','OA','O2','O3']
#espadas

lista_espadas=['E4','E5','E6','E7','EQ','EJ','EK','EA','E2','E3']
#copas

lista_copas=['C4','C5','C6','C7','CQ','CJ','CK','CA','C2','C3']
#paus

lista_paus=['P4','P5','P6','P7','PQ','PJ','PK','PA','P2','P3']

#lista_geral
lista_geral=[]
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

rodada=1
