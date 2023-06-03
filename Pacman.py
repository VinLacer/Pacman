import utils
import pygame
import Constantes
import sprites
import sys

class Game:
    
    def __init__(self):
        pygame.init()                                                                                    #inicia o pygame
        pygame.mixer.init()                                                                              #inicia parte de sons
        self.screen = pygame.display.set_mode((Constantes.LARGURA,Constantes.ALTURA))                    #configura a tela
        pygame.display.set_caption(Constantes.NOME_JOGO)                                                           
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.jogando = False
            
    def esperar_jogador(self):
        self.relogio.tick(Constantes.FPS)
        esperando = True
        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    utils.carregar_sons(Constantes.SOM_TELA_INIT)
                    pygame.mixer.music.play()
                    esperando = False
                    self.jogando = True
                if event.type == pygame.QUIT:
                    esperando = False
                    self.rodando = False
        
    def tela_ini(self):
        utils.carregar_sons(Constantes.MUSICA_TELA_INIT)
        pygame.mixer.music.play()
        self.screen.fill('black')
        
        logo_img = utils.carregar_img(Constantes.LOGO)
        logo_img = pygame.transform.scale(logo_img,(1.5*333,1.5*151))
        logo_rect = logo_img.get_rect()
        logo_rect.midtop = (Constantes.LARGURA/2,30)
        self.screen.blit(logo_img,logo_rect)

        txt_tecla_surf = utils.escrever_txt('Aperte qualquer tecla para iniciar!!!',
        Constantes.FONTE_GAME,
        30,
        'white')

        txt_tecla_rect = pygame.Surface.get_rect(txt_tecla_surf)
        txt_tecla_rect.midtop = (Constantes.LARGURA/2, 350)

        self.screen.blit(txt_tecla_surf,txt_tecla_rect)


        txt_vinicius_surf = utils.escrever_txt('Work in progress by Vinicius Lacerda Costa',
        Constantes.FONTE,
        30,
        'blue',)

        txt_vinicius_rect = pygame.Surface.get_rect(txt_vinicius_surf)
        txt_vinicius_rect.midbottom = (Constantes.LARGURA/2,600)

        self.screen.blit(txt_vinicius_surf,txt_vinicius_rect)
        
        pygame.display.flip()
        self.esperar_jogador()
    
    def sair_jogo(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def novo_Jogo(self):
        self.screen.fill('black')
        player_group.draw(self.screen)
        mapa_group.draw(self.screen)

        pygame.display.flip()
        player_group.update()
        self.eventos()
        self.relogio.tick(Constantes.FPS)

    def eventos(self):
        if pygame.sprite.collide_mask(player,mapa):
            print('colisao')
            player.vel = 0
            player.caminhando = False
            player.block_dire = player.direção
            player.voltar()
        else:
            player.block_dire = ''
        player.vel = 2

        if player.mask.overlap(mapa.mask,(0,0)):
            print('overlap')
    
            
g = Game()
g.tela_ini()

player = sprites.Player()
mapa = sprites.mapa()

player_group = pygame.sprite.Group()
mapa_group = pygame.sprite.Group()

player_group.add(player)
mapa_group.add(mapa)


while g.rodando:
    g.sair_jogo()
    g.novo_Jogo()
    
    
    
                