import pygame
from random import choice

RES = WIDTH, HEIGHT = 1202 902
TILE = 100
cols, rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:
    sc.fill()
