import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice
pygame.init()

LARGURA = 640
ALTURA = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Dino Game')
