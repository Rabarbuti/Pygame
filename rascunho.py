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
#lista geral de nypes
lista_geral=[lista_ouros,lista_espadas,lista_copas,lista_paus]
dic_valor = {'A':'ace','Q':"queen",'K':'king','J':'jack'}
#lista_geral

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
    carta_tornada=[1]
    P1=[]
    P2=[]
    P3=[]
    P4=[]
    lista_geral.remove(carta_tornada)
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
    return [P1,P2,P3,P4]
dicionario_imagens_ouro={}
for carta in lista_ouros:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_diamonds.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_diamonds.png')
    dicionario_imagens_ouro[carta]=(imagem)

dicionario_imagens_espadas = {}
for carta in lista_espadas:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_spades.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_spades.png')
    dicionario_imagens_espadas[carta]=(imagem)

dicionario_imagens_copas = {}
for carta in lista_copas:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_hearts.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_hearts.png')
    dicionario_imagens_copas[carta]=(imagem)

dicionario_imagens_paus = {}
for carta in lista_paus:
    if carta[1] in dic_valor:
        imagem=(f'Pygame\cartas\{dic_valor[carta[1]]}_of_clubs.png')  
    else:
        imagem=(f'Pygame\cartas\{carta[1]}_of_clubs.png')
    dicionario_imagens_paus[carta]=(imagem)

dicionario_imagens_1 = (dicionario_imagens_ouro|dicionario_imagens_espadas)
dicionario_imagens_2 = (dicionario_imagens_1|dicionario_imagens_copas)
dicionario_imagens_total = (dicionario_imagens_2|dicionario_imagens_paus)

'''print(dicionario_imagens_ouro)
print(dicionario_imagens_espadas)
print(dicionario_imagens_copas)
print(dicionario_imagens_paus)'''
#print(dicionario_imagens_total)
        
cartas_na_mesa = [['EA', 'O4','OQ'],['O5','O6','O7'],['P6', 'PJ','OJ'],['E4', 'E5','E6']]


pygame.init()


WIDTH = 500
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))


game = True

i = 0

while game:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    if i < 1:
        for i in range(len(cartas_na_mesa[0])):
            for t in range(len(cartas_na_mesa)):
                imagem_carta = pygame.image.load(dicionario_imagens_total[cartas_na_mesa[t][i]])
                image = pygame.transform.scale(imagem_carta, (125/2, 166/2))
                window.blit(image, [10+100*t, 10+50*i])
                pygame.display.update()
        i += 1

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


       
        


        
