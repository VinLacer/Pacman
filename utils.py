import pygame
import Constantes
import os

def carregar_img(img):
        img_path = os.path.join(os.getcwd(),img)
        img = pygame.image.load(img_path).convert()
        return img

def carregar_sons(som):
        som_path = os.path.join(os.getcwd(), som)
        som = pygame.mixer.music.load(som_path)
        return som


def rodando():
        rodando = True
        while rodando:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: rodando = False
                return rodando
                                

def escrever_txt(texto,fonte,tamanho,cor):
        txt = pygame.font.Font(fonte,tamanho)
        texto_surface = txt.render(texto,True,cor)
        return texto_surface

        