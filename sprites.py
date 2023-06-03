import pygame
import utils
import Constantes
import sys


class Player (pygame.sprite.Sprite):                                        #Cria player
    def __init__(self):
        super().__init__()
        self.pos_x = Constantes.LARGURA/2                               
        self.pos_y = Constantes.ALTURA/2   
        self.vel = 2
        self.caminhando = True

        self.direção = ''
        self.block_dire = ''

        self.Pac_img = []

        self.Pac_img.append(utils.carregar_img(Constantes.PAC_0)) 
        self.Pac_img.append(utils.carregar_img(Constantes.PAC_1))
        self.Pac_img.append(utils.carregar_img(Constantes.PAC_2))

        self.sprite_atual = 0

        self.image = self.Pac_img[int(self.sprite_atual)]
        self.rect = self.image.get_rect()
        
        
    def update(self):                                                    #função para atualizar o player
        if self.caminhando == True:
            self.caminhar()
            self.animar()
    
    def voltar(self):
        #print(self.block_dire)
        if self.block_dire == 'CIMA' :
            self.pos_y += 5
        if self.block_dire == 'BAIXO':
            self.pos_y -= 5
        if self.block_dire == 'DIREITA':
            self. pos_x -= 5
        if self.block_dire == 'ESQUERDA':
            self.pos_x += 5
        self.caminhando = True
          

    def caminhar(self):
        if self.caminhando == True:                                                   #movimentação do player
            if pygame.key.get_pressed()[pygame.K_w]:
                self.direção = 'CIMA'
                self.pos_y -= self.vel
            if pygame.key.get_pressed()[pygame.K_s]:                        
                self.direção = 'BAIXO'
                self.pos_y += self.vel
            if pygame.key.get_pressed()[pygame.K_d]:
                self.direção = 'DIREITA'
                self.pos_x += self.vel
            if pygame.key.get_pressed()[pygame.K_a]:
                self.direção = 'ESQUERDA'
                self.pos_x -= self.vel

            if self.rect.right < 0:                                           #para nao sair da tela no eixo X
                self.pos_x = Constantes.LARGURA
            if self.rect.left > Constantes.LARGURA:
                self.pos_x = 0

        self.rect.center = (self.pos_x,self.pos_y)
            

    def animar(self): 
        self.sprite_atual += 0.05
        if pygame.key.get_pressed()[pygame.K_w]:
            self.image = self.Pac_img[int(self.sprite_atual)]
            self.image = pygame.transform.rotate(self.image, 90)
            
        if pygame.key.get_pressed()[pygame.K_s]:
            self.image = self.Pac_img[int(self.sprite_atual)]
            self.image = pygame.transform.rotate(self.image, 270)

        if pygame.key.get_pressed()[pygame.K_a]:
            self.image = self.Pac_img[int(self.sprite_atual)]
            self.image = pygame.transform.rotate(self.image, 180)
        
        if pygame.key.get_pressed()[pygame.K_d]:
            self.image = self.Pac_img[int(self.sprite_atual)]

        if self.sprite_atual >= 2.4:
                self.sprite_atual = 0
        
        self.image = pygame.transform.scale(self.image,(25,20))
        self.mask = pygame.mask.from_surface(self.image)
        

class mapa(pygame.sprite.Sprite):                                           #classe para o mapa permite criar colisoes
    def __init__(self):
        super().__init__()
        self.image = utils.carregar_img(Constantes.MAPA)
        self.image = pygame.transform.scale(self.image,(802,550))
        self.image.fill('blue',special_flags=pygame.BLEND_RGB_MAX)
        self.rect = self.image.get_rect(center = (400,315))
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_colorkey((0,0,0))
        