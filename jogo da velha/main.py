import pygame

#Constantes do Jogo

#Janela
LARGURA_JANELA = 600
ALTURA_JANELA = 600

#Imagens
FUNDO = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\fundo.png'),(LARGURA_JANELA,ALTURA_JANELA))
ICONE = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\icone.png'),(96,96))
X = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\x.png')
O = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\0.png')

#Posição dos Quadrados
listapos = [
            [[0,0],[191,191],0],
            [[205,0],[396,191],0],
            [[409,0],[600,191],0],
            [[0,205],[191,396],0],
            [[205,205],[396,396],0],
            [[409,205],[600,396],0],
            [[0,409],[191,600],0],
            [[205,409],[396,600],0],
            [[409,409],[600,600],0]
]

valor = 0

lista = []
listaDesenhar = []
listasimb = [(1,X),(-1,O)]

simbval = listasimb[valor][0]
simb = listasimb[valor][1]

#Funçoes

def reset(listapos,valor,lista,listaDesenhar,listasimb,simbval,simb):
    for pos in listapos:
        pos[2] = 0
    valor = 0
    lista.clear()
    listaDesenhar.clear()

    simbval = listasimb[valor][0]
    simb = listasimb[valor][1]
    return listapos,valor,lista,listaDesenhar,listasimb,simbval,simb

def desenhar(simbval,simb,POS,lista,valor,listasimb):
    mousepos = pygame.mouse.get_pos()
    for num in range(0,9):
        if mousepos[0] >= POS[num][0][0] and mousepos[1] >= POS[num][0][1] and mousepos[1] <= POS[num][1][1] and mousepos[0] <= POS[num][1][0] and POS[num][2] == 0:
            
            POS[num][2] = simbval
            lista.append([simb])
            lista[-1].append(POS[num][0][0])
            lista[-1].append(POS[num][0][1])
            
            #Modificando o símbolo
            valor = (valor + 1) % 2
            simbval = listasimb[valor][0]
            simb = listasimb[valor][1]

    return lista,POS,simbval,simb,valor

def desenharFigura(lista,listaDesenhar):
    for opcoes in lista:
        if opcoes not in listaDesenhar:
            listaDesenhar.append(opcoes)
        janela.blit(opcoes[0],(opcoes[1],opcoes[2]))

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
            lista, listapos, simbval, simb, valor = desenhar(simbval,simb,listapos,lista,valor,listasimb)

    #Verificando a derrota
    n1 = listapos[0][2]
    n2 = listapos[1][2]
    n3 = listapos[2][2]
    n4 = listapos[3][2]
    n5 = listapos[4][2]
    n6 = listapos[5][2]
    n7 = listapos[6][2]
    n8 = listapos[7][2]
    n9 = listapos[8][2]

    nvitoria = 0

    v1 = n1 + n2 + n3
    v2 = n4 + n5 + n6
    v3 = n7 + n8 + n9
    v4 = n1 + n4 + n7
    v5 = n2 + n5 + n8
    v6 = n3 + n6 + n9
    v7 = n1 + n5 + n9
    v8 = n3 + n5 + n7

    vitorias = [v1,v2,v3,v4,v5,v6,v7,v8]

    for vitoria in vitorias:
        if vitoria == 3 and nvitoria == 0 or vitoria == -3 and nvitoria == 0:
            print(f'O Vencedor Foi: {"X" if vitoria == 3 else "O"}')
            nvitoria += 1
            listapos,valor,lista,listaDesenhar,listasimb,simbval,simb = reset(listapos,valor,lista,listaDesenhar,listasimb,simbval,simb)

    if len(lista) == 9 and nvitoria == 0:
        nvitoria += 1
        listapos,valor,lista,listaDesenhar,listasimb,simbval,simb = reset(listapos,valor,lista,listaDesenhar,listasimb,simbval,simb)

    #Desenhando o Fundo
    janela.blit(FUNDO,(0,0))

    #Desenhando as figuras
    desenharFigura(lista,listaDesenhar)

    #Atualizando o jogo:
    pygame.display.update()