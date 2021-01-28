import pygame
pygame.init()

#Configurações

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Janela

#Nome da Janela
NOME_JANELA = 'Jogo da Velha'

#Dimensões Janela
LARGURA_JANELA = 600
ALTURA_JANELA = round((250 * LARGURA_JANELA) / 200)
DIMENSAO_JANELA = (LARGURA_JANELA, ALTURA_JANELA)

#Imagens Janela
FUNDO = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\fundo.png'), DIMENSAO_JANELA)
ICONE = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\icone.png'), (96, 96))

#Fundo
TAMANHO_LINHA = round((4 * LARGURA_JANELA) / 200)

#Criando a Janela
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))

#Definindo o Nome Da Janela
pygame.display.set_caption(NOME_JANELA)

#Definindo o Icone da Janela
pygame.display.set_icon(ICONE)

#Criando Variável Que Verifica Se Fecharam o Jogo
DEVE_CONTINUAR = True

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Símbolos

#Dimensão Símbolo
TAMANHO_SIMBOLO = round((64 * LARGURA_JANELA) / 200)
DIMENSAO_SIMBOLO = (TAMANHO_SIMBOLO, TAMANHO_SIMBOLO)

#Imagens Símbolos
X = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\x.png'), DIMENSAO_SIMBOLO)
O = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\0.png'), DIMENSAO_SIMBOLO)

#Identificar de Quem é a Vez
Vez = 0

#Lista dos Símbolos Desenhados
Lista_Simbolos_Desenhados = []

#Lista Dos Simbolos e Seus Valores
Lista_Simbolos = [(1, X), (-1, O)]

#Símbolo e Valor selecionado da lista
Simbolo = Lista_Simbolos[Vez][1]
Valor_Simbolo = Lista_Simbolos[Vez][0]

#Topo Esquerdo dos Quadrados
TOPO_1 = 0
TOPO_2 = TOPO_1 + TAMANHO_SIMBOLO + TAMANHO_LINHA
TOPO_3 = TOPO_2 + TAMANHO_SIMBOLO + TAMANHO_LINHA

#Inferior Direito dos Quadrados
INFERIOR_1 = TOPO_1 + (TAMANHO_SIMBOLO - 1)
INFERIOR_2 = TOPO_2 + (TAMANHO_SIMBOLO - 1)
INFERIOR_3 = TOPO_3 + (TAMANHO_SIMBOLO - 1)

#Posição dos Quadrados
Lista_Posicao_Quadrados = [
            [[TOPO_1, TOPO_1], [INFERIOR_1, INFERIOR_1], 0],
            [[TOPO_2, TOPO_1], [INFERIOR_2, INFERIOR_1], 0],
            [[TOPO_3, TOPO_1], [INFERIOR_3, INFERIOR_1], 0],
            [[TOPO_1, TOPO_2], [INFERIOR_1, INFERIOR_2], 0],
            [[TOPO_2, TOPO_2], [INFERIOR_2, INFERIOR_2], 0],
            [[TOPO_3, TOPO_2], [INFERIOR_3, INFERIOR_2], 0],
            [[TOPO_1, TOPO_3], [INFERIOR_1, INFERIOR_3], 0],
            [[TOPO_2, TOPO_3], [INFERIOR_2, INFERIOR_3], 0],
            [[TOPO_3, TOPO_3], [INFERIOR_3, INFERIOR_3], 0]
]

#Criando um Relógio
Relogio = pygame.time.Clock()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Números

#Dimensões Números
LARGURA_NUMERO = round((16 * LARGURA_JANELA) / 200)
ALTURA_NUMERO = round((20 * LARGURA_JANELA) / 200)
DIMENSAO_NUMERO = (LARGURA_NUMERO, ALTURA_NUMERO)

#Imagens Números
NUMERO_0 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero.png'), DIMENSAO_NUMERO)
NUMERO_1 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (1).png'), DIMENSAO_NUMERO)
NUMERO_2 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (2).png'), DIMENSAO_NUMERO)
NUMERO_3 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (3).png'), DIMENSAO_NUMERO)
NUMERO_4 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (4).png'), DIMENSAO_NUMERO)
NUMERO_5 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (5).png'), DIMENSAO_NUMERO)
NUMERO_6 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (6).png'), DIMENSAO_NUMERO)
NUMERO_7 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (7).png'), DIMENSAO_NUMERO)
NUMERO_8 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (8).png'), DIMENSAO_NUMERO)
NUMERO_9 = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\numero (9).png'), DIMENSAO_NUMERO)

#Posições Números
POSICAO_INICIAL_NUMERO_X = (round((167 * LARGURA_JANELA) / 200), round((204 * LARGURA_JANELA) / 200))
POSICAO_INICIAL_NUMERO_O = (POSICAO_INICIAL_NUMERO_X[0], round((228 * LARGURA_JANELA) / 200))

#Números a serem desenhados
Lista_Desenhar_Numero = []

#Lista dos Números
Lista_Numeros = [NUMERO_0, NUMERO_1, NUMERO_2, NUMERO_3, NUMERO_4, NUMERO_5, NUMERO_6, NUMERO_7, NUMERO_8, NUMERO_9]

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Mini Símbolos

#Dimensões Mini Símbolos
LARGURA_MINI_SIMBOLO = LARGURA_NUMERO
ALTURA_MINI_SIMBOLO = ALTURA_NUMERO
DIMENSAO_MINI_SIMBOLO = (LARGURA_MINI_SIMBOLO, ALTURA_MINI_SIMBOLO)

#Imagens
MINI_X = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\minix.png'), DIMENSAO_MINI_SIMBOLO)
MINI_O = pygame.transform.scale(pygame.image.load('C:\\Users\\Ivone\\Desktop\\jogo-da-velha-em-python\\jogo da velha\\imagens\\minio.png'), DIMENSAO_MINI_SIMBOLO)

#Lista Dos Mini Símbolos a Serem Selecionados
Lista_Mini_Simbolo = [MINI_X, MINI_O]

#Mini Símbolo Selecionado da lista
Mini_Simbolo = Lista_Mini_Simbolo[Vez]

#Posições Mini Símbolos
POSICAO_MINI_SIMBOLO = (round((116 * LARGURA_JANELA) / 200), POSICAO_INICIAL_NUMERO_X[1])

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Funçoes

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Redefinir o jogo

def redefinir():

    #Chamando as Variáveis
    global Lista_Posicao_Quadrados, Vez, Lista_Simbolos_Desenhados, Lista_Simbolos, Valor_Simbolo, Simbolo, Lista_Mini_Simbolo, Mini_Simbolo

    #Redefinindo os Valores dos Símbolos Para Nulo
    for Posição in Lista_Posicao_Quadrados:
        Posição[2] = 0

    #Definindo a Vez Inicial Para X
    Vez = 0

    #Apagando os Símbolos Desenhados
    Lista_Simbolos_Desenhados.clear()

    #Atualizando o Símbolo, o Valor do Símbolo e o Mini Símbolo
    Mini_Simbolo = Lista_Mini_Simbolo[Vez]
    Valor_Simbolo = Lista_Simbolos[Vez][0]
    Simbolo = Lista_Simbolos[Vez][1]

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Cliquou na Janela

def Clique():

    #Chamando as Váriaveis
    global Valor_Simbolo, Simbolo, Lista_Posicao_Quadrados, Lista_Simbolos_Desenhados, Vez, Lista_Simbolos, Lista_Mini_Simbolo, Mini_Simbolo

    #Identificando a Posição do Mouse
    mousepos = pygame.mouse.get_pos()

    #Verificando se o Jogador Cliquou na Área de Algum Quadrado
    for num in range(0, 9):
        if mousepos[0] >= Lista_Posicao_Quadrados[num][0][0] and mousepos[1] >= Lista_Posicao_Quadrados[num][0][1] and mousepos[1] <= Lista_Posicao_Quadrados[num][1][1] and mousepos[0] <= Lista_Posicao_Quadrados[num][1][0] and Lista_Posicao_Quadrados[num][2] == 0:

            #Modificando o Valor Do Simbolo Do Quadrado Cliquado
            Lista_Posicao_Quadrados[num][2] = Valor_Simbolo

            #Adicionando um Símbolo a Ser Desenhado e a Posição em Que Vai Ser Desenhado
            Lista_Simbolos_Desenhados.append([Simbolo])
            Lista_Simbolos_Desenhados[-1].append((Lista_Posicao_Quadrados[num][0][0], Lista_Posicao_Quadrados[num][0][1]))

            #Atualizando a Vez, o Mini Símbolo, o Valor do Símbolo e o Símbolo
            Vez = (Vez + 1) % 2
            Mini_Simbolo = Lista_Mini_Simbolo[Vez]
            Valor_Simbolo = Lista_Simbolos[Vez][0]
            Simbolo = Lista_Simbolos[Vez][1]

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Desenhando os Símbolos

def desenharSimbolo(Lista_Simbolos_Desenhados):

    #Para Cada Símbolo Na Lista:
    for Simbolos in Lista_Simbolos_Desenhados:
        #Desenhando os Símbolos Da Lista de Desenhar
        janela.blit(Simbolos[0], Simbolos[1])

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Verificando Derrota

def verificarDerrota():

    #Chamando as Variáveis
    global Lista_Posicao_Quadrados, Lista_Simbolos_Desenhados

    #Verificando a derrota
    n1 = Lista_Posicao_Quadrados[0][2]
    n2 = Lista_Posicao_Quadrados[1][2]
    n3 = Lista_Posicao_Quadrados[2][2]
    n4 = Lista_Posicao_Quadrados[3][2]
    n5 = Lista_Posicao_Quadrados[4][2]
    n6 = Lista_Posicao_Quadrados[5][2]
    n7 = Lista_Posicao_Quadrados[6][2]
    n8 = Lista_Posicao_Quadrados[7][2]
    n9 = Lista_Posicao_Quadrados[8][2]

    #Criando Um Contador Para o Programa Contar Somente Uma Vitória Por Vez
    Contador_Derrota = 0

    Vitorias = [
                n1 + n2 + n3,
                n4 + n5 + n6,
                n7 + n8 + n9,
                n1 + n4 + n7,
                n2 + n5 + n8,
                n3 + n6 + n9,
                n1 + n5 + n9,
                n3 + n5 + n7
                ]

    for Vitoria in Vitorias:
        if Vitoria == 3 and Contador_Derrota == 0 or Vitoria == -3 and Contador_Derrota == 0:
            print(f'O Vencedor Foi: {"X" if Vitoria == 3 else "O"}')

            Contador_Derrota += 1

            redefinir()

    if len(Lista_Simbolos_Desenhados) == 9 and Contador_Derrota == 0:

        print('Empate')

        Contador_Derrota += 1

        redefinir()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Desenhado os Objetoa

def Desenhar():

    #Desenhando o Fundo
    janela.blit(FUNDO,(0,0))

    #Desenhando o Mini Símbolo Dizendo de quem é a Vez
    janela.blit(Mini_Simbolo, POSICAO_MINI_SIMBOLO)

    #Desenhando as figuras
    desenharSimbolo(Lista_Simbolos_Desenhados)

    #Verificando a Derrota
    verificarDerrota()

    #Atualizando a Janlela
    pygame.display.update()

    #Definindo o FPS (Atualizações Por Segundo ou Frames Por Segundo)
    Relogio.tick(30)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Loop Principal
while DEVE_CONTINUAR:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            DEVE_CONTINUAR = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            Clique()

    Desenhar()