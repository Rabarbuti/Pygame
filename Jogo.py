import random
from turtle import pos
import pygame, sys
import funcoes
from pygame.locals import *
import time
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
back_card = (r"Pygame\icon\back_card.png")
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

carta_tornada=funcoes.tornar_carta(lista_geral)  
conserta = [lista_geral,carta_tornada]      
cartas_na_mesa = funcoes.distribui_mao(carta_tornada)
print(cartas_na_mesa)

manilha_sorteada = funcoes.achar_manilhas(carta_tornada[1],lista_geral)
cartas_da_rodada = []
lista_zuada = []



mainClock = pygame.time.Clock()
pygame.init()

WIDTH = 1080
HEIGHT = 720    
pygame.display.set_caption('TRUCO!')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:
        
        fonte = pygame.font.SysFont(None, 40)
        fonte2  = pygame.font.SysFont("Algerian", 110)
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        tela_fundo = pygame.image.load('Pygame/table_top.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        draw_text('PLAY', fonte, (255, 255, 255), screen, 110, 116)
        draw_text('How To Play', fonte, (255, 255, 255), screen, 65, 210)
        draw_text('As escuras', fonte2, (255, 0, 0), screen, 370, 50)
        draw_text('com Maciel', fonte2, (255, 0, 0), screen, 380, 170)

        pygame.display.update()
        mainClock.tick(60)

def game():
    i   = 0
    game=True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx , my = pygame.mouse.get_pos()
                for i in range(len(lista_zuada)):
                    carta = lista_zuada[i]
                    if carta['rect'].collidepoint(mx, my):
                        print(f'clicou na {i}')
                        print(carta['jogador'])
                        print(carta['i'])
                        del cartas_na_mesa[carta['jogador']][carta['i']]

            
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas
        screen.fill((0, 0, 0))  # Preenche com a cor branca
        tela_fundo = pygame.image.load('Pygame/table_top.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        screen.blit(tela_fundo,(i,0))
        if i < 1:
            for i in range(len(cartas_na_mesa[0])): 
                for t in range(len(cartas_na_mesa)):
                    if cartas_na_mesa[t][i] in cartas_da_rodada:
                        imagem_carta = pygame.image.load(dicionario_imagens_total[cartas_na_mesa[t][i]])
                    else:
                        imagem_carta = pygame.image.load(back_card)
                    maos = pygame.transform.scale(imagem_carta, (100, 130))
                    imagem_manilhas = pygame.image.load(dicionario_imagens_total[carta_tornada[1]])
                    manilhas = pygame.transform.scale(imagem_manilhas, (100, 130))
                    if t == 0:
                        posx=0
                        posy=180+140*i
                    elif t == 1:
                        posx=360+110*i
                        posy=0
                    elif t == 2:
                        posx=980
                        posy=180+140*i
                    elif t ==3:
                        posx = 360+110*i
                        posy = 590

                    lista_zuada.append({'rect':pygame.Rect(posx, posy, 100, 130), 'jogador': t, 'i': i})
                    screen.blit(maos, [posx, posy])
                    screen.blit(manilhas, [470, 300])
                    pygame.display.update()
            i += 1


def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

main_menu()
       
        


        
