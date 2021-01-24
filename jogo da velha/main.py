import pygame

#Constantes do Jogo

#Posição dos Quadrados
POS1 = [(0,0),(191,191)]
POS2 = [(205,0),(396,191)]
POS3 = [(409,0),(600,191)]
POS4 = [(0,205),(191,396)]
POS5 = [(205,205),(396,396)]
POS6 = [(409,205),(600,396)]
POS7 = [(0,409),(191,600)]
POS8 = [(205,409),(396,600)]
POS9 = [(409,409),(600,600)]

janela.blit(X,(409,409))
    janela.blit(O,(205,409))
    janela.blit(X,(0,409))
    janela.blit(O,(409,205))
    janela.blit(X,(205,205))
    janela.blit(O,(0,205))
    janela.blit(X,(409,0))
    janela.blit(O,(205,0))
    janela.blit(X,(0,0))
#Janela
LARGURA_JANELA = 600
ALTURA_JANELA = 600

#Imagens
FUNDO = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\fundo.png'),(LARGURA_JANELA,ALTURA_JANELA))
ICONE = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\icone.png'),(96,96))
X = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\x.png')
O = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\0.png')

pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0
pos5 = 0
pos6 = 0
pos7 = 0
pos8 = 0
pos9 = 0

#Funçoes

def atualizar():
    pygame.display.update()

#Criando a Janela
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('Jogo da Velha')
pygame.display.set_icon(ICONE)

#Deve Continuar
deve_continuar = True

#Loop Principal
while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos[0])

    #Desenhando o Fundo
    janela.blit(FUNDO,(0,0))

    #Atualizando o jogo:
    atualizar()