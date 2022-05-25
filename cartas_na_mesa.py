import pygame
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
                window.blit(image, [10+100*t, 10+150*i])
                pygame.display.update()
        i += 1

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados