import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, screen, x):
        super().__init__()
        self.screen = screen

        original_image = pygame.image.load('imagens/enemy.png')
        self.image = pygame.transform.scale(original_image, (60, 60))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = 0  # Começa no topo

        self.y = float(self.rect.y)
        self.speed = 0.5  # Mais lento

    def update(self):
        self.y += self.speed  # Move para baixo
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)