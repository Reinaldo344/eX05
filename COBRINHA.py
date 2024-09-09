import pygame
import random
import sys

# inicializa o pygame
pygame.init()

#dimensões da tela
largura = 600
altura = 400
tela = pygame.desplay.set_mode((largura, altura))
pygame.display.set_cation('jogo da cobrinha')

# definindo cores
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

# configurações do jogo 
tamanho_celula = 20
velocidade = 15
relogio = pygame.time.clock()

# fução para gerar a comida em posição aleatória
def gerar_comida ():
    x_comida = random.randrange(0, largura, tamanho_celula)
    y_comida = random.randrange(0, altura, tamanho_celula)
    return x_comida, y_comida

# função principal
def desenhar_cibrinha(cobra):
    for parte in cobra:
        pygame.draw,rect(tele), verde, (( parte[0], parte[1], tamanho_celula )
                                        
      # função principal
      def jogo():
          x = lartura // 2
          y = altura // 2
          x_velocidade = 0
          y_velocidade = 0
          cobra = [(x, y)]     
          comprimento_cobra = 1

          x_comida, y_comida = gerar-comida()  

          while true:
              # detecta eventos 
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT: 
                   pygame.quit()     
                   sys.exit()    
                 #caotura as teclas para mover a cobrinha 
                 if avento.type == pygame.KEYDOWN:
                    if evento.key == pygame.k_LEFT and x_ velocidade == 0;          
