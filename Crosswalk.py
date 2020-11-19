import sys
import pygame
import numpy as np

from V2X import V2X


class Crosswalk(V2X, pygame.sprite.Sprite):
    hit = pygame.image.load('images/collision.png')

    def __init__(self, position, width, height, interval=20, phase=0):
        V2X.__init__(self, position, name="Crosswalk")
        pygame.sprite.Sprite.__init__(self)
        red_wall = [255, 0, 0] * np.ones((width, height, 3))
        self.normal = pygame.surfarray.make_surface(red_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position

        self.width = width
        self.height = height
        self.position = position
        self.time_left = interval + phase
        self.interval = interval
        self.color = "red"
        self.data =\
            [self.name, self.color, self.position,
             self.width, self.height, self.time_left, self.interval]

    def update(self):
        self.time_left -= 1
        if self.time_left <= 0:
            self.time_left = self.interval
            if self.color == "red":
                self.color = "green"
                green_wall = [0, 255, 0] *\
                    np.ones((self.width, self.height, 3))
                self.normal = pygame.surfarray.make_surface(green_wall)
                self.rect = pygame.Rect(self.normal.get_rect())
                self.rect.center = self.position
            else:
                self.color = "red"
                red_wall = [255, 0, 0] * np.ones((self.width, self.height, 3))
                self.normal = pygame.surfarray.make_surface(red_wall)
                self.rect = pygame.Rect(self.normal.get_rect())
                self.rect.center = self.position
        self.image = self.normal

        self.data = \
            [self.name, self.color, self.position,
             self.width, self.height, self.time_left, self.interval]


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Crosswalk Example")
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    c1 = Crosswalk((300, 200), 50, 10)
    c2 = Crosswalk((100, 400), 10, 50)
    crosswalks = pygame.sprite.Group()
    crosswalks.add(c1)
    crosswalks.add(c2)

    while True:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        crosswalks.update([c1])
        print(c1.data, c2.data)
        crosswalks.draw(screen)
        pygame.draw.rect(screen, (50, 50, 255), [200, 200, 100, 200], 0)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render("P", 1, (255, 255, 255))
        textpos = text.get_rect()
        screen.blit(
            text,
            [250 - textpos[2] / 2,
             300 - textpos[3] / 2,
             textpos[2],
             textpos[3]]
            )

        pygame.display.flip()
