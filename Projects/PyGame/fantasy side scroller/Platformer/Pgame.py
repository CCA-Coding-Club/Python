import pygame
pygame.init()

TILE = 50; WIDTH = HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH , HEIGHT))
clock = pygame.time.Clock ()

images = {
    'bg': pygame.transform.scale(pygame.image.load('img/sky.png').convert(), (WIDTH , HEIGHT)),
    'sun': pygame.image.load('img/sun.png').convert_alpha(),
    }