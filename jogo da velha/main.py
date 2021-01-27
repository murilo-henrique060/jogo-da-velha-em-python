import pygame
pygame.init()

#Constantes do Jogo

#Janela
LARGURA_JANELA = 600
ALTURA_JANELA = round((250 * LARGURA_JANELA)/200)


#Imagens
FUNDO = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\fundo.png'),(LARGURA_JANELA,ALTURA_JANELA))
ICONE = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\icone.png'),(96,96))
X = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\x.png')
O = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\0.png')
NUMERO_1 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (1).png')
NUMERO_2 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (2).png')
NUMERO_3 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (3).png')
NUMERO_4 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (4).png')
NUMERO_5 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (5).png')
NUMERO_6 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (6).png')
NUMERO_7 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (7).png')
NUMERO_8 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (8).png')
NUMERO_9 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (9).png')
NUMERO_0 = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero.png')
MINI_X = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\minix.png')
MINI_O = pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\minio.png')

tamanho_linha = round((4*LARGURA_JANELA)/200)

#mini simbolo
larguraMiniSimbolo = round((16 * LARGURA_JANELA) / 200)
alturaMiniSimbolo = round((20 * LARGURA_JANELA) / 200)
posicaoMiniSimboloX = round((116 * LARGURA_JANELA) / 200)
posicaoMiniSimboloY = round((204 * LARGURA_JANELA) / 200)

#Tamanho do simbolo
tamanhosimb = round((64 * LARGURA_JANELA) / 200)
#parte mais alta e a mais a esquerda dos objetos
top1 = 0
top2 = top1 + tamanhosimb + tamanho_linha
top3 = top2 + tamanhosimb + tamanho_linha
#parte mais baixa e mais a direita dos objetos
bottom1 = top1 + (tamanhosimb - 1)
bottom2 = top2 + (tamanhosimb - 1)
bottom3 = top3 + (tamanhosimb - 1)

#redimencionando os símbolos
X = pygame.transform.scale(X,(tamanhosimb,tamanhosimb))
O = pygame.transform.scale(O,(tamanhosimb,tamanhosimb))
MINI_X = pygame.transform.scale(MINI_X,(larguraMiniSimbolo,alturaMiniSimbolo))
MINI_O = pygame.transform.scale(MINI_O,(larguraMiniSimbolo,alturaMiniSimbolo))

#Posição dos Quadrados
listapos = [
            [[top1,top1],[bottom1,bottom1],0],
            [[top2,top1],[bottom2,bottom1],0],
            [[top3,top1],[bottom3,bottom1],0],
            [[top1,top2],[bottom1,bottom2],0],
            [[top2,top2],[bottom2,bottom2],0],
            [[top3,top2],[bottom3,bottom2],0],
            [[top1,top3],[bottom1,bottom3],0],
            [[top2,top3],[bottom2,bottom3],0],
            [[top3,top3],[bottom3,bottom3],0]
]

valor = 0

lista = []
listaDesenhar = []
listasimb = [(1,X),(-1,O)]
listaMiniSimb = [MINI_X,MINI_O]

miniSimb = listaMiniSimb[valor]
simbval = listasimb[valor][0]
simb = listasimb[valor][1]

#Funçoes

def reset(listapos,valor,lista,listaDesenhar,listasimb,simbval,simb,listaMiniSimb,miniSimb):
    for pos in listapos:
        pos[2] = 0
    valor = 0
    lista.clear()
    listaDesenhar.clear()

    miniSimb = listaMiniSimb[valor]
    simbval = listasimb[valor][0]
    simb = listasimb[valor][1]
    return listapos,valor,lista,listaDesenhar,listasimb,simbval,simb,miniSimb

def desenhar(simbval,simb,POS,lista,valor,listasimb,listaMiniSimb,MiniSimb):
    mousepos = pygame.mouse.get_pos()
    for num in range(0,9):
        if mousepos[0] >= POS[num][0][0] and mousepos[1] >= POS[num][0][1] and mousepos[1] <= POS[num][1][1] and mousepos[0] <= POS[num][1][0] and POS[num][2] == 0:
            
            POS[num][2] = simbval
            lista.append([simb])
            lista[-1].append(POS[num][0][0])
            lista[-1].append(POS[num][0][1])
            
            #Modificando o símbolo
            valor = (valor + 1) % 2
            MiniSimb = listaMiniSimb[valor]
            simbval = listasimb[valor][0]
            simb = listasimb[valor][1]

    return lista,POS,simbval,simb,valor,MiniSimb

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
            lista, listapos, simbval, simb, valor, miniSimb = desenhar(simbval,simb,listapos,lista,valor,listasimb,listaMiniSimb,miniSimb)

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
            listapos,valor,lista,listaDesenhar,listasimb,simbval,simb,miniSimb = reset(listapos,valor,lista,listaDesenhar,listasimb,simbval,simb,listaMiniSimb,miniSimb)

    if len(lista) == 9 and nvitoria == 0:
        nvitoria += 1
        listapos,valor,lista,listaDesenhar,listasimb,simbval,simb,miniSimb = reset(listapos,valor,lista,listaDesenhar,listasimb,simbval,simb,listaMiniSimb,miniSimb)

    #Desenhando o Fundo
    janela.blit(FUNDO,(0,0))

    #Desenhando o simbolo de quem é a vez
    janela.blit(miniSimb,(posicaoMiniSimboloX,posicaoMiniSimboloY))

    #Desenhando as figuras
    desenharFigura(lista,listaDesenhar)

    #Atualizando o jogo:
    pygame.display.update()