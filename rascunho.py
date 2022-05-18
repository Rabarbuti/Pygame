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
manilhas=[]

carta_tornada=random.choice(lista_geral)
lista_geral.remove(carta_tornada)

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

print(P1)
print(P2)
print(P3)
print(P4)