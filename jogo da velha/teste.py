import pygame
pygame.init()

janela = pygame.display.set_mode((600,600))

Cor_Meio = pygame.Surface((600,600))
Cor_Meio.fill((0,0,0))
Cor_Meio.set_alpha(200)

NUMERO_1 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\fundo.png')
NUMERO_1 = pygame.transform.scale(NUMERO_1,(600,600))
NUMERO_1.set_colorkey((0,0,0))

while True:
    janela.fill((255,255,255))
    janela.blit(Cor_Meio,(0,0))
    janela.blit(NUMERO_1,(0,0))
    pygame.display.update()