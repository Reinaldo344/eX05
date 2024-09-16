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
                        k_velocidade = tanmaho_celula
                        y_velocidade = 0
                     elif evento.key == pygame.k_RIGHT ant d y_velocidade == 0
                       x_velocidade = -tanmaho tamanho_celula
                       y_velocidade= 0
                       elif evento.key == pygama.k_UP and y_velo
                            y_velocidade = -tamanho_celula
                            x_velocideda - 0 
                        elif evento.key == pygame.k_DOWN and y_velocidade == 0
                            y_velocideda - tamanho_celula
                            x_velocida = 0
        # ataliza a posição da cobrinha 
        x += x_velocidade
        y += y_velocidade
        cordra.append((x, y))

        # detecta se a cobrinha comeu a comida
        if len((cordra)) > comrimento_cordra:
           del cobra[0]

         # detecta colisão com as bordas ou com o próprio corpo 
         if x == x_comida = >= largura or y < 0 or >= altura or (x, y) in corbra[:-1]:
            break
            
        # detecta se acobirnha comeu a comida
        if x == x_comida and y == y_comida
            coprimeto_cobra += 1
            x_comida, y_comida = gerar_comida

        # atualiza a tela 
        tela.fill(preta)
        desenhar_cobirnha(corbra)
        pygame.draw.rect(rela, vermelho, (x_comida; tamanho_celula, tamanho_celula)
        pygame.displa.flip()

        relogio.tick(velocidade)

        # inicin o jogo 
jogo()
