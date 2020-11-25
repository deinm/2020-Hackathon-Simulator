import pygame
import time

class Dynamic(pygame.sprite.Sprite):
    def __init__(self,image,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = position[0]
        self.y = 365
        self.time = 0
        self.update()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, deltat=False):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))


