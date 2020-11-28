import copy
import math
import time
import random
import numpy as np
import pygame
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP,
                           KEYDOWN, USEREVENT)

from Car import CarSprite
from Trophy import TrophySprite
from Wall import WallSprite
from Dynamic import Dynamic


class Game:
    def __init__(self, walls, trophies, parkings,
                 crosswalks, traffic_signs, schoolzone, car, database):
        self.init_args =\
            [
                copy.copy(walls),
                copy.copy(trophies),
                copy.copy(parkings),
                copy.copy(crosswalks),
                copy.copy(car),
                database
            ]
        pygame.init()
        self.car = car
        self.screen = pygame.display.set_mode((1000, 800))
        self.traffic_signs = traffic_signs
        self.school_zones = schoolzone
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(None, 75)
        self.win_font = pygame.font.Font(None, 50)
        self.win_condition = None
        self.win_text = font.render('', True, (0, 255, 0))
        self.loss_text = font.render('', True, (255, 0, 0))
        self.wall_group = pygame.sprite.RenderPlain(*walls)
        self.trophy_group = pygame.sprite.RenderPlain(*trophies)
        self.crosswalk_group = pygame.sprite.RenderPlain(*crosswalks)
        self.car_group = pygame.sprite.RenderPlain(car)
        self.parkings = parkings
        self.rect = self.screen.get_rect()
        self.stop = False
        self.car_update = True
        self.database = database
        self.dynamic_flag=False
        self.dynamic = Dynamic('images/bird.png',(-100,0))
        self.dynamic_group = pygame.sprite.RenderPlain(self.dynamic)

    def run(self, auto=False):
        seconds = 0
        record = False
        temp_v2x_data = []
        while True:
            deltat = self.clock.tick(30)
            seconds += 0.03

            seconds = round(seconds, 2)

            if self.win_condition is not None:
                if not record:
                    record = True
                    result = seconds
                    print("Total time:", result)
            events = pygame.event.get()
            if auto:
                self.car.k_right = self.car.k_left =\
                    self.car.k_up = self.car.k_down = 0
            for event in events:
                if auto:
                    if not hasattr(event, 'key'):
                        continue
                    if event.type != USEREVENT and (
                            event.key == K_RIGHT or
                            event.key == K_LEFT or
                            event.key == K_UP or
                            event.key == K_DOWN
                            ):
                        continue
                    if self.win_condition is None:
                        if event.key == K_RIGHT:
                            if self.car.k_right > -8:
                                self.car.k_right += -1
                        elif event.key == K_LEFT:
                            if self.car.k_left < 8:
                                self.car.k_left += 1
                        elif event.key == K_UP:
                            if self.car.k_up < 5:
                                self.car.k_up += 1
                        elif event.key == K_DOWN:
                            if self.car.k_down > -5:
                                self.car.k_down += -1
                        elif event.key == K_ESCAPE:
                            self.database.stop = True
                    elif self.win_condition is True and event.key == K_SPACE:
                        print(result)
                        self.database.stop = True
                        time.sleep(0.1)
                    elif self.win_condition is False and event.key == K_SPACE:
                        print(result)
                        time.sleep(0.1)
                        self.database.stop = True
                    elif event.key == K_ESCAPE:
                        self.database.stop = True
                        print(result)
                        time.sleep(0.1)
                else:
                    if not hasattr(event, 'key'):
                        continue
                    down = event.type == KEYDOWN
                    if self.win_condition is None:
                        if event.key == K_RIGHT:
                            self.car.k_right = down * -5
                        elif event.key == K_LEFT:
                            self.car.k_left = down * 5
                        elif event.key == K_UP:
                            self.car.k_up = down * 2
                        elif event.key == K_DOWN:
                            self.car.k_down = down * -2
                        elif event.key == K_ESCAPE:
                            self.database.stop = True
                    elif self.win_condition is True and event.key == K_SPACE:
                        print(result)
                        time.sleep(0.1)
                        self.database.stop = True
                    elif self.win_condition is False and event.key == K_SPACE:
                        print(result)
                        time.sleep(0.1)
                        self.database.stop = True

                    elif event.key == K_ESCAPE:
                        print(result)
                        time.sleep(0.1)
                        self.database.stop = True

            if self.database.stop:
                break


            # RENDERING
            self.screen.fill((0, 0, 0))
            if self.car_update:
                self.car_group.update(deltat)
            collisions = pygame.sprite.groupcollide(
                self.car_group, self.wall_group, False, False, collided=pygame.sprite.collide_rect_ratio(0.9))

            if collisions != {}:
                self.car_update = False
                self.win_condition = False
                self.car.image = pygame.image.load('images/collision.png')
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                self.car.k_right = 0
                self.car.k_left = 0

            crosswalk_collisions = pygame.sprite.groupcollide(
                    self.car_group,
                    self.crosswalk_group,
                    False,
                    False,
                    collided=None
                )

            trophy_collision = pygame.sprite.groupcollide(
                    self.car_group,
                    self.trophy_group,
                    False,
                    True
                )

            for colled_crosswalk in crosswalk_collisions.values():
                if colled_crosswalk[0].color == "red":
                    self.car_update = False
                    self.win_condition = False
                    self.car.image = pygame.image.load('images/collision.png')
                    self.car.MAX_FORWARD_SPEED = 0
                    self.car.MAX_REVERSE_SPEED = 0
                    self.car.k_right = 0
                    self.car.k_left = 0

            if trophy_collision != {}:
                all_parking_done = True
                for parking in self.parkings:
                    if not parking.mission_complete:
                        all_parking_done = False
                        break

                if all_parking_done:
                    self.car_update = False
                    self.win_condition = True
                else:
                    self.car_update = False
                    self.win_condition = False
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                if self.win_condition is True:
                    self.car.k_right = -5

            temp_v2x_data.clear()
            for parking in self.parkings:
                parking.update(self.car)
                parking.draw(self.screen)
                if parking.is_in_range(self.car):
                    temp_v2x_data.append((id(parking), parking.data))

            self.wall_group.update()
            self.crosswalk_group.update()
            self.crosswalk_group.draw(self.screen)

            for crosswalk in self.crosswalk_group:
                if crosswalk.is_in_range(self.car):
                    temp_v2x_data.append((id(crosswalk), crosswalk.data))
            new_dict = dict()

            for traffic_sign in self.traffic_signs:
                traffic_sign.draw(self.screen)
                temp_v2x_data.append((id(traffic_sign), traffic_sign.data))

            for school_zone in self.school_zones:
                check_speed = school_zone.update(self.car)
                if check_speed is False:
                    self.car_update = False
                    self.win_condition = False
                    self.car.image = pygame.image.load('images/collision.png')
                    self.car.MAX_FORWARD_SPEED = 0
                    self.car.MAX_REVERSE_SPEED = 0
                    self.car.k_right = 0
                    self.car.k_left = 0
                school_zone.draw(self.screen)
                temp_v2x_data.append((id(school_zone), school_zone.data))

            for v2x_data in temp_v2x_data:
                key, value = v2x_data
                new_dict[key] = value
            self.database.v2x_data = new_dict
            # print(self.database.v2x_data)
            self.wall_group.draw(self.screen)
            self.car_group.draw(self.screen)
            self.trophy_group.draw(self.screen)

            # Dynamic Obstacle
            dynamic_collisions = pygame.sprite.groupcollide(
                self.car_group, self.dynamic_group, False,False,collided=pygame.sprite.collide_rect_ratio(1))
            self.dynamic_group.update(dynamic_collisions)
            if dynamic_collisions != {}:
                self.car_update = False
                self.win_condition = False
                self.car.image = pygame.image.load('images/collision.png')
                self.car.MAX_FORWARD_SPEED = 0
                self.car.MAX_REVERSE_SPEED = 0
                self.car.k_right = 0
                self.car.k_left = 0

            if self.school_zones != []:
                if (250 <= self.car.position[0] < 250 + 550) and (350 <= self.car.position[1] < 350 + 100) & (self.dynamic_flag==False):
                    if self.dynamic.x == -100:
                        self.dynamic.x = random.randint(250,600)
                    if 0<=self.car.position[0]-self.dynamic.x<=100:
                        if self.dynamic.time == 0:
                            self.dynamic.time = time.time()
                        if time.time() - self.dynamic.time < 5:
                            self.dynamic.draw(self.screen)
                        else:
                            self.dynamic.x = -100

            # Counter Render
            pygame.display.flip()

            self.make_lidar_data()

    def again(self, auto):
        self.__init__(*self.init_args)
        self.run(auto=auto)

    def make_lidar_data(self):
        lidar_data = np.zeros((360))
        L = 100
        array = pygame.surfarray.array3d(self.screen)
        car = self.database.car
        x, y = car.position

        car_direction = car.direction % 360

        lidar_x = int(x - 20 * math.sin(math.pi * car_direction / 180))
        lidar_y = int(y - 20 * math.cos(math.pi * car_direction / 180))

        for direction in range(-90 + car_direction, 90 + car_direction):
            direction = direction % 360

            x, y = lidar_x, lidar_y
            m = math.tan(math.pi * direction / 180)
            if direction == 0:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x = x
                    y -= 1
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (0 < direction < 45) or (315 <= direction < 360):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    y -= 1
                    x = (m) * (y - lidar_y) + lidar_x
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (45 <= direction < 90) or (90 < direction < 135):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x -= 1
                    y = (1 / m) * (x - lidar_x) + lidar_y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 90:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x -= 1
                    y = y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (135 <= direction < 180) or (180 < direction < 225):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    y += 1
                    x = (m) * (y - lidar_y) + lidar_x
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 180:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x = x
                    y += 1
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif (225 <= direction < 270) or (270 < direction < 315):
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x += 1
                    y = (1 / m) * (x - lidar_x) + lidar_y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            elif direction == 270:
                while (math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2) < L):
                    x += 1
                    y = y
                    try:
                        if (array[int(x)][int(y)] == 255).all():
                            break
                    except IndexError:
                        break
            else:
                print(f"Uncatched Case: {direction}")

            length = math.sqrt((x - lidar_x) ** 2 + (y - lidar_y) ** 2)
            if length > L:
                length = L

            lidar_data[direction] = length

        lidar_data = np.concatenate(
            (lidar_data[-90:], lidar_data[:270]), axis=None
            )
        lidar_data = np.concatenate(
            (lidar_data, lidar_data), axis=None
            )
        lidar_data =\
            lidar_data[self.car.direction % 360:
                       self.car.direction % 360 + 180]
        self.database.lidar.data = lidar_data


if __name__ == "__main__":
    walls = [
        WallSprite((512, 2.5), 1024, 5),
        WallSprite((512, 765.5), 1024, 5),
        WallSprite((2.5, 384), 5, 768),
        WallSprite((1021.5, 384), 5, 768)
    ]
    trophies = [
        TrophySprite((300, 50))
    ]
    car = CarSprite('images/car.png', (50, 700))
    g = Game(walls, trophies, car)
    g.run()
