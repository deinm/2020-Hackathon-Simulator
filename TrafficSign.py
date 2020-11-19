from V2X import V2X

import pygame
import numpy as np


class TrafficSign(V2X):
    def __init__(self, position, width, height, imagePath=None):
        V2X.__init__(self, position, name="TrafficSign")
        self.position = position
        self.width = width
        self.height = height

        if imagePath is None:
            sample_array = 100 * np.ones((width, height, 3), np.uint8)
            self.image =\
                pygame.pixelcopy.make_surface(sample_array)
        else:
            self.image = pygame.image.load(imagePath)
            self.image =\
                pygame.transform.scale(self.image, (self.width, self.height))

        self.data = [
                self.name, self.position,
                self.width, self.height,
            ]

    def draw(self, screen):
        image_rect = self.image.get_rect()
        image_rect.left, image_rect.top = self.position
        screen.blit(self.image, image_rect)


class Right(TrafficSign):
    def __init__(self, position, width, height,
                 imagePath="images/right.JPG"):
        TrafficSign.__init__(self, position, width, height,
                             imagePath=imagePath)
        self.name = "Right"
        self.data = [
                self.name, self.position,
                self.width, self.height,
            ]


class Left(TrafficSign):
    def __init__(self, position, width, height, imagePath="images/left.JPG"):
        TrafficSign.__init__(self, position, width, height,
                             imagePath=imagePath)
        self.name = "Left"
        self.data = [
                self.name, self.position,
                self.width, self.height,
            ]


if __name__ == "__main__":
    import sys
    pygame.init()
    pygame.display.set_caption("TrafficSign Example")
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    t = Right((300, 200), 100, 100, "images/no_left.JPG")

    while True:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        print(t.data)
        t.draw(screen)

        pygame.display.flip()
