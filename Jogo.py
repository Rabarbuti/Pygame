import random
from turtle import pos
import pygame, sys
import funcoes
from pygame.locals import *
import time

#Lista de cartas criadas, separadas por naipe
lista_ouros=['O4','O5','O6','O7','OQ','OJ','OK','OA','O2','O3']
#espadas
lista_espadas=['E4','E5','E6','E7','EQ','EJ','EK','EA','E2','E3']
#copas
lista_copas=['C4','C5','C6','C7','CQ','CJ','CK','CA','C2','C3']
#paus
lista_paus=['P4','P5','P6','P7','PQ','PJ','PK','PA','P2','P3']
#lista geral de nypes
lista_geral=[lista_ouros,lista_espadas,lista_copas,lista_paus]
#acrescentando esse dic_valor para facilinar na hora de baixar as imagens das cartas
dic_valor = {'A':'ace','Q':"queen",'K':'king','J':'jack'}

list1 = [1, 2, 3]
list2 = [1]

back_card = (r"Pygame\icon\back_card.png")

#dicionarios das imagens carregadas
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

#juntando todos dicionarios em apenas um
dicionario_imagens_1 = (dicionario_imagens_ouro|dicionario_imagens_espadas)
dicionario_imagens_2 = (dicionario_imagens_1|dicionario_imagens_copas)
dicionario_imagens_total = (dicionario_imagens_2|dicionario_imagens_paus)

#começar a puxar as funçoes para colocar no jogo
carta_tornada=funcoes.tornar_carta(lista_geral)        
cartas_na_mesa = funcoes.distribui_mao(carta_tornada)
manilha_sorteada = funcoes.achar_manilhas(carta_tornada[1],lista_geral)

#criando as listas para ir dando append
cartas_da_rodada = []
lista_zuada = []
cartas_para_excluir = []



#inicio configs do jogo
mainClock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('Pygame\ambiente2.wav')
pygame.mixer.music.set_volume(0.3)
barulho_inicio = pygame.mixer.Sound('Pygame\cartas_inicio2.wav')
barulho_carta = pygame.mixer.Sound('Pygame\carta_vira2.wav')
desistiu = pygame.mixer.Sound('Pygame\01desistiu.wav')
WIDTH = 1080
HEIGHT = 720    
pygame.display.set_caption('TRUCO!')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)

font = pygame.font.SysFont(None, 20)
font1 = pygame.font.SysFont(None, 40)

verso = pygame.image.load(back_card)

#funcao para desenhar texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

#funcao do menu
def main_menu():
    pygame.mixer.music.play(-1)
    while True:
        fonte = pygame.font.SysFont(None, 40)
        fonte2  = pygame.font.SysFont("Algerian", 110)
        screen.fill((0,0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(255, 545, 100, 45)
        button_2 = pygame.Rect(710, 545, 180, 45)
        tela_fundo = pygame.image.load('Pygame\fundoinicio.jpg')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))
        if button_1.collidepoint((mx, my)):
            if click:
                barulho_inicio.play()
                time.sleep(5)
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
        
        draw_text('PLAY', fonte, (255, 255, 255), screen, 270, 556)
        draw_text('How To Play', fonte, (255, 255, 255), screen, 720, 556)

        pygame.display.update()
        mainClock.tick(60)

clock = pygame.time.Clock()
FPS = 60

#classe criada para conseguir separar o jogo em etapas
class Truco:
    fase = "escolher"

def desenha_na_tela(texto):
    return font1.render(texto, True, (0, 0, 0))

#funcao do jogo
def game():
    i   = 0
    game=True
    time1 = 0
    time2 = 0
    empate = 0
    lista_zuada=[]
    while game:
        clock.tick(FPS)

        if time1 == 2 and empate < 2:
            time1_vencedor()
        if time2 == 2 and empate < 2:
            time2_vencedor()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                desistiu.play()
                time.sleep(5)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mx , my = pygame.mouse.get_pos()
                for i in range(len(lista_zuada)):
                    carta = lista_zuada[i]
                    if carta['rect'].collidepoint(mx, my):
                        cartas_da_rodada.append(cartas_na_mesa[carta['jogador']][carta['carta']])
                        cartas_para_excluir.append(cartas_na_mesa[carta['jogador']][carta['carta']])
                        print(cartas_da_rodada)

                        if len(cartas_da_rodada) % 4 == 0:
                            Truco.fase = "ganhador"
                            print(Truco.fase)
            
            if event.type == pygame.QUIT:
                game = False
        lista_zuada=[]
        screen.fill((0, 0, 0)) 
        tela_fundo = pygame.image.load('Pygame\table_top.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        screen.blit(tela_fundo,(i,0))
        
        for t in range(len(cartas_na_mesa)):
            for i in range(len(cartas_na_mesa[t])): 
            
                #imagem dividida em back card ou a frente normal
                if cartas_na_mesa[t][i] in cartas_para_excluir:
                    imagem_carta = pygame.image.load(dicionario_imagens_total[cartas_na_mesa[t][i]])
                    #print("load da carta")
                else:
                    imagem_carta = verso
                maos = pygame.transform.scale(imagem_carta, (100, 130))

                #posicao das cartas
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

                #adicionando as cartas clicadas pelo jogador
                lista_zuada.append({'rect':pygame.Rect(posx, posy, 100, 130), 'jogador': t, 'carta': i})
                screen.blit(maos, [posx, posy])
        
        #load e blit da manilha
        imagem_manilhas = pygame.image.load(dicionario_imagens_total[carta_tornada[1]])
        manilhas = pygame.transform.scale(imagem_manilhas, (100, 130))
        screen.blit(manilhas, [470, 300])

        #truco passa para fase ganhador, assim iniciando a proxima rodada e contabilizando o vencedor da passada
        if Truco.fase == "ganhador":
            vencedor = funcoes.vencedor(cartas_da_rodada, manilha_sorteada)
            print(f'o vencedor foi: {vencedor}')
            del cartas_da_rodada[:]
            
            #sistema de pontuacao de acordo com a funcao
            if vencedor == -1:
                empate += 1
                time1 += 1
                time2 += 1

            elif vencedor == 'P1' or vencedor == 'P3':
                time1 += 1
                if time1 == 2 and empate < 2:
                    time1_vencedor()
                    

            else:
                time2 += 1

            #removendo carta, para ela não aparecer mais na tela, pós rodada
            print('tratando')
            for mao in cartas_na_mesa:
                print(f' mao: {mao}')
                for carta in mao:
                    print(f'carta: {carta}')
                    if carta in cartas_para_excluir:
                        mao.remove(carta)
                        print(f'cartas {cartas_na_mesa}')
            
            
            Truco.fase = "escolher"

        #score board canto superior direito da tela
        screen.blit(desenha_na_tela('Time 1: ' + str(time1)), (WIDTH - 150, 10))
        screen.blit(desenha_na_tela('Time 2: ' + str(time2)), (WIDTH - 150, 40))

        pygame.display.update()


#menu do HOW TO PLAY
def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        fonte = pygame.font.SysFont(None, 40)
        mx, my = pygame.mouse.get_pos()
        button_3 = pygame.Rect(0,0, 100, 30)
        tela_fundo = pygame.image.load('Pygame\Regras.png')
        tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        screen.blit(tela_fundo,(0,0))

        if button_3.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0] == True:
                main_menu()
        pygame.draw.rect(screen, (255, 0, 0), button_3)

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
            draw_text('Return', fonte, (255, 255, 255), screen, 3, 2)
            pygame.display.update()
        mainClock.tick(60)


#funcao para quando o time 1 ganha a partida
def time1_vencedor():
    running = True
    i = 0
    j = 300
    while running:

        fonte = pygame.font.SysFont(None, 35)
        fonte2 = pygame.font.SysFont(None, 80)
        mx, my = pygame.mouse.get_pos()
        tela_fundo = pygame.image.load('Pygame\table_top.png')
        while i < 30:
            tela_fundo = pygame.transform.scale(tela_fundo,(j, (j+0)))
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(10)
            screen.blit(tela_fundo,(0,0))
            j += 50
            i +=1

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
            draw_text(('Time 1 Venceu! '),fonte2, (255, 255, 255), screen, 360, 300)
            pygame.display.update()
        mainClock.tick(60)

#funcao para quando o time 2 ganha a partida
def time2_vencedor():
    running = True
    i = 0
    j = 300
    while running:

        fonte = pygame.font.SysFont(None, 35)
        fonte2 = pygame.font.SysFont(None, 80)
        mx, my = pygame.mouse.get_pos()
        tela_fundo = pygame.image.load('Pygame\table_top.png')
        while i < 30:
            tela_fundo = pygame.transform.scale(tela_fundo,(j, (j+0)))
            pygame.display.update()
            clock = pygame.time.Clock()
            clock.tick(10)
            screen.blit(tela_fundo,(0,0))
            j += 50
            i +=1

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
            draw_text(('Time 2 Venceu! '),fonte2, (255, 255, 255), screen, 360, 300)
            pygame.display.update()
        mainClock.tick(60)

main_menu()
      
        


        