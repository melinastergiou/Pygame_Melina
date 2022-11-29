import pygame 
from jogo import *
# assets

# ----- Inicia assets
largura_comp = 51
altura_comp = 51
altura_carro = 2 * altura_comp
velocidade = 6
posições = [36,156,278,398]
lista_posv = [posições[0], posições[1]]
lista_posa = [posições[2], posições[3]]
pontuação = 0
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('recursos/fundo.png').convert()

# --- imagens ---


# ---- funcções ------