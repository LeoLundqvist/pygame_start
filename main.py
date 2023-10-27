# initialize

import pygame

pygame.init()

# GAME WINDOW
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_captions("ECS Snake Game")
clock = pygame.time.Clock()


