import pygame
import utils
import Constantes
import sys


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = Constantes.LARGURA/2                               
        self.pos_y = Constantes.ALTURA/2   
        self.vel = 2
        self.caminhando = True                                         #variaveis de posição setadas para o meio da tela

        self.image = pygame.Surface((10,10))                            #cria uma surface nova para ser o player
        self.image.fill('red')                                          #pinta a surface de vermelho
        self.rect = self.image.get_rect()                               #pega o retangulo da surface
        self.rect.center = (self.pos_x,self.pos_y)                      #ajusta a posição do retangulo
        self.mask = pygame.mask.from_surface(self.image)                #mascara do retangulo para colisao
    
    def update(self):
        if self.caminhando == True:
            self.caminhar()
            

    def caminhar(self):
        if pygame.key.get_pressed()[pygame.K_w]:
            self.pos_y -= self.vel
        if pygame.key.get_pressed()[pygame.K_s]:
            self.pos_y += self.vel
        if pygame.key.get_pressed()[pygame.K_d]:
            self.pos_x += self.vel
        if pygame.key.get_pressed()[pygame.K_a]:
            self.pos_x -= self.vel
        self.rect.center = (self.pos_x,self.pos_y)
        



class mapa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = utils.carregar_img(Constantes.MAPA).convert_alpha()
        self.image = pygame.transform.scale(self.image,(800,600))
        self.image.fill('blue',special_flags=pygame.BLEND_RGB_MAX)
        self.rect = self.image.get_rect(center = (400,300))
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_colorkey((0,0,0))
        

