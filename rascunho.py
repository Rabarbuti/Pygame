import random
import pygame
import funcoes
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
list1 = [1, 2, 3]
list2 = [1]
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
print(dicionario_imagens_total)


        
cartas_na_mesa = funcoes.distribui_mao(funcoes.tornar_carta(lista_geral))
print(cartas_na_mesa)
manilha_sorteada = funcoes.achar_manilhas(funcoes.tornar_carta(lista_geral)[1],lista_geral)


pygame.init()


WIDTH = 1200
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))


game = True

i = 0

while game:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    tela_fundo = pygame.image.load('Pygame/table_top.png')
    tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
    window.blit(tela_fundo,(i,0))
    if i < 1:
        for i in range(len(cartas_na_mesa[0])):
            for t in range(len(cartas_na_mesa)):
                imagem_carta = pygame.image.load(dicionario_imagens_total[cartas_na_mesa[t][i]])
                maos = pygame.transform.scale(imagem_carta, (100, 130))
                imagem_manilhas = pygame.image.load(dicionario_imagens_total[manilha_sorteada[t]])
                manilhas = pygame.transform.scale(imagem_manilhas, (100, 130))
                window.blit(maos, [10+150*t, 10+60*i])
                window.blit(manilhas, [10+50*t, 10+600])
                pygame.display.update()
        i += 1

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


       
        


        
