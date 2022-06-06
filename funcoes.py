import random
import pygame
lista_ouros=['O4','O5','O6','O7','OQ','OJ','OK','OA','O2','O3']
#espadas
lista_espadas=['E4','E5','E6','E7','EQ','EJ','EK','EA','E2','E3']
#copas
lista_copas=['C4','C5','C6','C7','CQ','CJ','CK','CA','C2','C3']
#paus
lista_paus=['P4','P5','P6','P7','PQ','PJ','PK','PA','P2','P3']
#lista geral de nypes
lista_geral=[lista_ouros,lista_espadas,lista_copas,lista_paus]
dic_valor = {'A':'ace','Q':"queen",'K':'king','J':'jack'}
#lista_geral
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
def tornar_carta(lista):
    a=lista[0]
    b=lista[1]
    c=lista[2]
    d=lista[3]
    lista_geral = []
    lista_geral.extend(a)
    lista_geral.extend(b)
    lista_geral.extend(c)
    lista_geral.extend(d)
    carta_tornada=random.choice(lista_geral)
    return [lista_geral,carta_tornada]
def achar_manilhas(carta_tornada,lista):
    a=lista[0]
    b=lista[1]
    c=lista[2]
    d=lista[3]
    if carta_tornada in a:
        indice=a.index(carta_tornada)+1
    if carta_tornada in b:
        indice=b.index(carta_tornada)+1
    if carta_tornada in c:
        indice=c.index(carta_tornada)+1
    if carta_tornada in d:
        indice=d.index(carta_tornada) +1
    if indice==10:
        indice=0
    manilhas=[lista_ouros[indice],lista_espadas[indice],lista_copas[indice],lista_paus[indice]]
    return manilhas
def distribui_mao(lista):
    lista_geral=lista[0]
    carta_tornada=lista[1]
    P1=[]
    P2=[]
    P3=[]
    P4=[]
    lista_geral.remove(carta_tornada)
    while len(P1)<3:
        carta_sorteada=random.choice(lista_geral)
        P1.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
    while len(P2)<3:
        carta_sorteada=random.choice(lista_geral)
        P2.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
    while len(P3)<3:
        carta_sorteada=random.choice(lista_geral)
        P3.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
    while len(P4)<3:
        carta_sorteada=random.choice(lista_geral)
        P4.append(carta_sorteada)
        lista_geral.remove(carta_sorteada)
    return [P1,P2,P3,P4]
'''def ganhador(lista_jogadores,lista_rodada,manilhas):
    i=0
    j=0
    lista_manilhas_usadas=[]
    P1=lista_jogadores[0]
    P2=lista_jogadores[1]
    P3=lista_jogadores[2]
    P4=lista_jogadores[3]
    a=intersection(manilhas,lista_rodada)
    if len(a)==1:
        if a[0] in P1:
            return 'P1'
        if a[0] in P2:
            return 'P2'
        if a[0] in P3:
            return 'P3'
        if a[0] in P4:
            return 'P4'
    if len(a)>1:
        while i<=4:
            while j<=4:
                if manilhas[i]==a[j]:
                    lista_manilhas_usadas.append(manilhas[i])
                    j+=1
                else:
                    j+=1
            i+=1
        manilha_vencedora=lista_manilhas_usadas[-1]
        if manilha_vencedora in P1:
            return 'P1'
        if manilha_vencedora in P2:
            return 'P2'
        if manilha_vencedora in P3:
            return 'P3'
        if manilha_vencedora in P4:
            return 'P4'
    if len(a)==0:'''
        
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
def vencedor(rodada, manilhas):
    carta_p1 = rodada[0]
    carta_p2 = rodada[1]
    carta_p3 = rodada[2]
    carta_p4 = rodada[3]
    cartas = [carta_p1, carta_p2, carta_p3, carta_p4]
    manilha = False
    for carta in cartas:
        if carta[1:2] == manilhas[0][1:2]:
            manilha = True
    if manilha:
        qtd_manilhas = 0
        jogadores_com_manilha = []
        for carta in cartas:
            if carta[1:2] == manilhas[0][1:2]:
                jogadores_com_manilha.append("P{}".format(cartas.index(carta) + 1))
                qtd_manilhas+=1

        if qtd_manilhas == 1:
            return jogadores_com_manilha[0]

        maior_carta = ""
        manilhas = []
        for jogador in jogadores_com_manilha:
            indice = int(jogador[1:2]) - 1
            manilhas.append(cartas[indice])

        naipes = ['O', 'E', 'C', 'P']
        count = 0
        for manilha in manilhas:
            if count == 0:
                maior_carta = manilha
            else:
                if manilha[1:2] == 'P':
                    maior_carta = manilha
                else:
                    idx = naipes.index(manilha[0:1])
                    maior_idx = naipes.index(maior_carta[0:1])

                    if (idx > maior_idx):
                        maior_carta = manilha
            count+=1

        ganhador_idx = cartas.index(maior_carta)
        return 'P{}'.format(ganhador_idx+1) 

    else:
        ordem = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']

        maior_carta_indice = 0
        empatou = False
        carta_vencedora = ""
        carta_indice = 0

        for carta in cartas:
            if ordem.index(str(carta[1:2])) > maior_carta_indice:
                maior_carta_indice = ordem.index(str(carta[1:2]))
                carta_indice = cartas.index(carta)
                carta_vencedora = carta
        for carta in cartas:
            if cartas.index(carta) != carta_indice:
                if ordem.index(str(carta[1:2])) == maior_carta_indice:
                    empatou = True

        if empatou:
            return -1

        carta_vencedora_indice = cartas.index(carta_vencedora)
        ganhador = 'P{}'.format(carta_vencedora_indice+1)

        return ganhador
