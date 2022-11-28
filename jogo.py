
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame 
import random

pygame.init()

# ----- Inicia estruturas de dados
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