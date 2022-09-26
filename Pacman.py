import pygame

# Inicia o pygame
pygame.init()

# Cria uma tela
screen = pygame.display.set_mode((800, 600))

# Define o pacman
pacmanImg = pygame.image.load('Pacman.png')
pacmanX = 370
pacmanY = 480
pacmanX_change = 0
pacmanY_change = 0

#Cria o pacman
def pacman(x, y):
    screen.blit(pacmanImg, (x, y))

#Função para movimento do pacman
def mov(pacmanX, pacmanY, pacmanX_change, pacmanY_change):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pacmanX_change = -0.2
        if event.key == pygame.K_RIGHT:
            pacmanX_change = 0.2
        if event.key == pygame.K_UP:
            pacmanY_change = -0.2
        if event.key == pygame.K_DOWN:
            pacmanY_change = 0.2
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            pacmanX_change = 0
            pacmanY_change = 0

    pacmanX += pacmanX_change
    pacmanY += pacmanY_change


    return pacmanX, pacmanY


# Loop do jogo
running = True
while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pacmanX, pacmanY = mov(pacmanX, pacmanY, pacmanX_change, pacmanY_change)

    pacman(pacmanX, pacmanY)
    pygame.display.update()