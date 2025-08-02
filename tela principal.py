import pygame
from pygame.locals import *
from sys import exit

pygame.init()

musica_de_fundo = pygame.mixer.music.load('Nonograma cats/investigations.mp3')
pygame.mixer.music.play(-1)

largura = 640
altura = 480

fonte = pygame.font.SysFont('Inter', 50, False)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Nonograma Cats')

while True:
    tela.fill((255,255,255))
    mensagem = f'Nonograma Cats'
    texto_formatado = fonte.render(mensagem,True,(0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(texto_formatado, (180,160))

    pygame.display.flip()
