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


# --- imagens ---
background = pygame.image.load('imagens/fundo.png').convert()

quadrado_v_img = pygame.image.load('imagens/quadrado_v.png').convert_alpha()
circulo_v_img = pygame.image.load('imagens/circulo_v.png').convert_alpha()
carro_v_img = pygame.image.load('imagens/carro_v.png')

quadrado_a_img = pygame.image.load('imagens/quadrado_a.png').convert_alpha()
circulo_a_img = pygame.image.load('imagens/circulo_a.png').convert_alpha()
carro_a_img = pygame.image.load('imagens/carro_a.png')

quadrado_v_img = pygame.transform.scale(quadrado_v_img, (largura_comp, altura_comp))
circulo_v_img = pygame.transform.scale(circulo_v_img, (largura_comp, altura_comp))
carro_v_img = pygame.transform.scale(carro_v_img, (largura_comp, altura_carro))

quadrado_a_img = pygame.transform.scale(quadrado_a_img, (largura_comp, altura_comp))
circulo_a_img = pygame.transform.scale(circulo_a_img, (largura_comp, altura_comp))
carro_a_img = pygame.transform.scale(carro_a_img, (largura_comp, altura_carro))

borda_img = pygame.image.load('imagens/Borda.PNG').convert()
borda_img = pygame.transform.scale(borda_img, (largura_da_tela, 1))

# ---- funcções e classes------

# --------- obstáculos -------