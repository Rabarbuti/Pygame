import pygame
import random
import os
import rascunho

pygame.init()

MAIN_IMAGE_PATH = os.dirname(_file_)
IMAGES_FOLDER = os.path.join(MAIN_IMAGE_PATH, "imagem")
CARDS_FOLDER = os.path.join(MAIN_IMAGE_PATH, "cartas")

window = pygame.display.set_mode((1800, 900))
pygame.display.set_caption('Truco!')
icon = pygame.image.load(os.path.join(MAIN_IMAGE_PATH, "back_cards.jpg"))
#Players
player1Img = pygame.image.load('Arthur.jpg')
player1X = 370
player1Y = 0

def player1():
    window.blit(player1Img, (player1X, player1Y) )

# ----- Inicia estruturas de dados
game = True
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    
    player1()
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

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
