import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint


pg.init()

pg.mixer.music.set_volume(0.1)
musica_de_fundo = pg.mixer.music.load("victory.mp3")
pg.mixer.music.play(-1)

barulho_colisao = pg.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

velocidade = 10
x_controle = 20
y_controle = 0


x_maca = randint(40,600)
y_maca = randint(50,430)

pontos = 0
fonte = pg.font.SysFont('arial', 40, True, True)

lista_cobra = []
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Game')
relogio = pg.time.Clock()
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pg.draw.rect(tela, (255, 25, 255), (XeY[0], XeY[1], 20,20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False

    
    
while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                 x_controle =  - velocidade
                 y_controle = 0
            
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                 x_controle =  velocidade
                 y_controle = 0
            
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                 y_controle = - velocidade
                 x_controle = 0
                 
            if event.key == K_s:
                if y_controle == velocidade:
                    pass
                else:
                 y_controle = + velocidade
                 x_controle = 0 
                 
                       
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle     
        
    cobra = pg.draw.rect(tela, (255, 25, 255), (x_cobra, y_cobra, 20, 20))
    maca = pg.draw.rect(tela, (255,0,0),(x_maca, y_maca, 20, 20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
        
    lista_cabeca =  []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pg.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione R para reiniciar o jogo'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        rect_texto = texto_formatado.get_rect()
        
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
           
            rect_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, rect_texto)            
            pg.display.update()
    
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)
    
    tela.blit(texto_formatado, (450,40))       
    pg.display.update()
    