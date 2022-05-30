# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)

# ----- Inicia assets
font = pygame.font.SysFont(None, 48)
text = font.render('HELLO WORLD', True, (0, 0, 255))
tela_fundo = pygame.image.load('Pygame/table_top.png')
tela_fundo = pygame.transform.scale(tela_fundo,(WIDTH, HEIGHT))
screen.blit(tela_fundo,(0,0))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    #   # Preenche com a cor branca
    window.blit(text, (10, 10))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados