from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):

    def __init__(self,screen,ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,3,15)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = (60,60,60)
        self.speed_factor = 3  # DEIXE MAIS RÁPIDO (antes era 1)

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)