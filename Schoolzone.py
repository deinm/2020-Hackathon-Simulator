from V2X import V2X
from Car import CarSprite

import pygame
import sys


class Schoolzone(V2X):
    def __init__(self, position, width, height):
        V2X.__init__(self, position, name="Schoolzone")
        self.mission_complete = False

        self.position = position
        self.width = width
        self.height = height

        self.data = [
                self.name, self.position,
                self.width, self.height,
                self.mission_complete
            ]

    def update(self, car: CarSprite):
        left, top, width, height = car.rect
        p0 = (left, top)
        p1 = (left + width, top)
        p2 = (left, top + height)
        p3 = (left + width, top + height)
        points = [p0, p1, p2, p3]

        in_mission = True
        for point in points:
            if not self.is_in_school_zone(point):
                in_mission = False
                break

        if in_mission and abs(car.speed) > 6:
            return False

        self.data = [
            self.name, self.position,
            self.width, self.height,
            self.mission_complete
        ]

        return True

    def draw(self, screen):
        x, y = self.position
        if not self.mission_complete:
            pygame.draw.rect(
                    screen,
                    (180, 70, 70),
                    [x, y, self.width, self.height],
                    0
                )

            font_size = int((self.width + self.height) / 15)
            font = pygame.font.Font('freesansbold.ttf', font_size)
            text = font.render("S", 1, (250, 250, 250))
            textpos = text.get_rect()
            screen.blit(
                    text,
                    [x + self.width / 2 - textpos[2] / 2,
                     y + self.height / 2 - textpos[3] / 2,
                     textpos[2],
                     textpos[3]]
                )
        else:
            pygame.draw.rect(
                    screen,
                    (50, 50, 50),
                    [x, y, self.width, self.height],
                    0
                )

    def is_in_school_zone(self, point: tuple):
        x, y = point
        if (self.position[0] < x <
            self.position[0] + self.width) and\
                (self.position[1] < y <
                 self.position[1] + self.height):
            return True
        else:
            return False


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Crosswalk Example")
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    c = CarSprite('images/car.png', (320, 240))
    p = Schoolzone((320, 240), 100, 60)

    while True:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
        p.update(c)
        p.draw(screen)

        pygame.display.flip()
