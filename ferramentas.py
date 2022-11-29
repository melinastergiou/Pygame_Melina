import pygame 
import random 
from jogo import altura_da_tela


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

def cria_obstaculos_seguintes():
    obstaculos_vermelho = [1,2]
    obstaculos_azul = [1,2]

    distv = random.randrange(2*altura_comp)
    dista = random.randrange(2*altura_comp)

    pverm = random.choice(obstaculos_vermelho)
    pazul = random.choice(obstaculos_azul)

    if pverm == 1:
        posv = posições[0]
    else:
        posv = posições[1]

    if pazul == 1:
        posa = posições[2]
    else:
        posa = posições[3]

    overm = random.choice(obstaculos_vermelho)
    oazul = random.choice(obstaculos_azul)

    if overm == 1:
        obv = Quadrado(quadrado_v_img, posv, distv)
        todosquadrados.add(obv)
    else:
        obv = Circulo(circulo_v_img, posv, distv)
        todoscirculos.add(obv)

    if oazul == 1:
        oba = Quadrado(quadrado_a_img, posa, dista)
        todosquadrados.add(oba)
    else:
        oba = Circulo(circulo_a_img, posa, dista)
        todoscirculos.add(oba)

    sprites.add(obv,oba)

    return True   


class Carro(pygame.sprite.Sprite):
    def __init__(self, img, cor):
        pygame.sprite.Sprite.__init__(self)

        #self.velocidade = aumento_da_velocidade
        self.image = img
        self.rect = self.image.get_rect()
        if cor == 'v':
            self.rect.x = posições[0]
            self.pos = [posições[0], posições[1]]

        else:
            self.rect.x = posições[2]
            self.pos = [posições[2], posições[3]]

        self.rect.y = altura_da_tela - altura_carro - altura_comp - 9
        self.speedx = 0
        self.speedy = 0
        self.cor = cor
        self.indice = 0

    def update (self):
        self.rect.x += self.speedx

        if self.cor == 'v':
            if self.speedx != 0 and self.rect.x in lista_posv:
                self.speedx = 0
        else:
            if self.speedx != 0 and self.rect.x in lista_posa:
                self.speedx = 0

class Quadrado(pygame.sprite.Sprite):
    def __init__(self, img, pos, dist):
        pygame.sprite.Sprite.__init__(self)

        #self.velocidade = aumento_da_velocidade
        self.image = img
        self.rect = self.image.get_rect()
        self.c = 'n'
        self.rect.x = pos
        self.rect.y = -dist
        self.speedx = 0
        self.speedy = velocidade

    def update (self):
        if self.rect.y >= altura_da_tela/3 and self.c == 'n' and self.rect.x <= 242:
            cria_obstaculos_seguintes()
            self.c = 's'
        self.rect.y += self.speedy

class Circulo(pygame.sprite.Sprite):
    def __init__(self, img, pos, dist):
        pygame.sprite.Sprite.__init__(self)

        #self.velocidade = aumento_da_velocidade
        self.image = img
        self.rect = self.image.get_rect()
        self.c = 'n'
        self.rect.x = pos
        self.rect.y = -dist 
        self.speedx = 0
        self.speedy = velocidade
        self.indice = 0

    def update (self):
        if self.rect.y >= altura_da_tela/3 and self.c == 'n' and self.rect.x <= 242:
            cria_obstaculos_seguintes()
            self.c = 's'
        self.rect.y += self.speedy

class Borda(pygame.sprite.Sprite):
    def __init__(self, img, borda):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        if borda == 1:
            self.rect.y = altura_da_tela
        else: 
            self.rect.y = altura_da_tela + altura_comp

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
