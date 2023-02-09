import pygame
import utils
import Constantes


class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.rect.move(self.rect[0],self.rect[2] - 1)
                    print('w')

class parede(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = utils.carregar_img(Constantes.MAPA).convert_alpha()
        self.image = pygame.transform.scale(self.image,(800,600))
        self.image.fill('blue',special_flags=pygame.BLEND_RGB_MAX)
        self.rect = self.image.get_rect(center = (400,300))
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_colorkey((0,0,0))
        

