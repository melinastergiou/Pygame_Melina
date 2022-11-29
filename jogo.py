
import pygame 
import random
from ferramentas import *

pygame.init()

# ----- Gera tela principal
largura_da_tela = 484
altura_da_tela = 968
window = pygame.display.set_mode((largura_da_tela, altura_da_tela))
pygame.display.set_caption('jogo')


game = True

clock = pygame.time.Clock()
FPS = 60


# ----- criando obstaculos

todosquadrados = pygame.sprite.Group()
todoscirculos = pygame.sprite.Group()
carros = pygame.sprite.Group()
sprites = pygame.sprite.Group()

carro_v = Carro(carro_v_img, 'v')
carro_a = Carro(carro_a_img, 'a')

cvinicial = Circulo(circulo_v_img, posições[0], 300)
cainicial = Circulo(circulo_a_img, posições[2], 300)

borda = Borda(borda_img, 1)
borda2 = Borda(borda_img, 2)

todoscirculos.add(cvinicial)
todoscirculos.add(cainicial)
carros.add(carro_v)
carros.add(carro_a)
sprites.add(carro_v)
sprites.add(carro_a)
sprites.add(cvinicial)
sprites.add(cainicial)


# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

            # serão criados (carro a carro v)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and carro_a.indice != 0:
                carro_a.speedx = -12
                carro_a.indice=0
            

            if event.key == pygame.K_RIGHT and carro_a.indice != 1:
                carro_a.speedx = 12
                carro_a.indice = 1

            if event.key == pygame.K_a and carro_v.indice != 0:
                carro_v.speedx = -12
                carro_v.indice = 0

            if event.key == pygame.K_d and carro_v.indice != 1:
                carro_v.speedx = 12
                carro_v.indice = 1

    sprites.update()

    
    # ----- Verifica Colisões
    hitsquadradosv = pygame.sprite.spritecollide(carro_v, todosquadrados, True)
    hitsquadradosa = pygame.sprite.spritecollide(carro_a, todosquadrados, True)
    hitsquadrados = len(hitsquadradosv) + len(hitsquadradosa)
    if hitsquadrados > 0:
        game = False

    hitscirculosv = pygame.sprite.spritecollide(carro_v, todoscirculos, True)
    hitscirculosa = pygame.sprite.spritecollide(carro_a, todoscirculos, True)
    hitscirculos = len(hitscirculosv) + len(hitscirculosa)
    if hitscirculos > 0:
        pontuação += hitscirculos
        FPS += 1

    fora = pygame.sprite.spritecollide(borda, todoscirculos, True)
    if len(fora) > 0:
        game = False

    n_sei_nome = pygame.sprite.spritecollide(borda2, todosquadrados, True)

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    sprites.draw(window)
    text = font.render('{0:.0f}'.format(pontuação), True, (255, 255, 255))
    window.blit(text, (420, 0))

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
