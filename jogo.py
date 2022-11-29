
import pygame 
import random

pygame.init()

game = True

clock = pygame.time.Clock()
FPS = 60

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and carro_a.indice != 0:
                carro_a.speedx = -12
                carro_a.indice = 0

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
