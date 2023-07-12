import pygame
import time
import random

# Inicialização do pygame
pygame.init()

# Definição das cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

# Dimensões da janela do jogo
largura_janela = 800
altura_janela = 600

# Tamanho do bloco da cobra e da comida
tamanho_bloco = 20

# Velocidade da cobra
velocidade = 15

# Inicialização da janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Jogo da Cobra')

# Função para exibir mensagem na tela
def mensagem(msg, cor):
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render(msg, True, cor)
    janela.blit(texto, [largura_janela / 6, altura_janela / 3])

# Loop principal do jogo
def jogo():
    game_over = False
    game_fim = False

    # Posição inicial da cobra
    posicao_x = largura_janela / 2
    posicao_y = altura_janela / 2

    # Movimento inicial da cobra
    movimento_x = 0
    movimento_y = 0

    # Lista para armazenar o corpo da cobra
    corpo = []
    comprimento_inicial = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura_janela - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_janela - tamanho_bloco) / 20.0) * 20.0

    # Loop do jogo
    while not game_over:

        while game_fim == True:
            janela.fill(cor_fundo)
            mensagem("Fim do jogo! Pressione C para jogar novamente ou Q para sair", (255, 255, 255))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_fim = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimento_x = -tamanho_bloco
                    movimento_y = 0
                elif event.key == pygame.K_RIGHT:
                    movimento_x = tamanho_bloco
                    movimento_y = 0
                elif event.key == pygame.K_UP:
                    movimento_y = -tamanho_bloco
                    movimento_x = 0
                elif event.key == pygame.K_DOWN:
                    movimento_y = tamanho_bloco
                    movimento_x = 0

        if posicao_x >= largura_janela or posicao_x < 0 or posicao_y >= altura_janela or posicao_y < 0:
            game_fim = True

        posicao_x += movimento_x
        posicao_y += movimento_y
        janela.fill(cor_fundo)
        pygame.draw.rect(janela, cor_comida, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cobra_cabeca = []
        cobra_cabeca.append(posicao_x)
        cobra_cabeca.append(posicao_y)
        corpo.append(cobra_cabeca)
        if len(corpo) > comprimento_inicial:
            del corpo[0]

        for segmento in corpo[:-1]:
            if segmento == cobra_cabeca:
                game_fim = True

        for segmento in corpo:
            pygame.draw.rect(janela, cor_cobra, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

        pygame.display.update()

        if posicao_x == comida_x and posicao_y == comida_y:
            comida_x = round(random.randrange(0, largura_janela - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_janela - tamanho_bloco) / 20.0) * 20.0
            comprimento_inicial += 1

        clock = pygame.time.Clock()
        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()
