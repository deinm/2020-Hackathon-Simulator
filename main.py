import argparse
import os
import threading

import pygame

from Brain import Brain
from Control import Control
from Course import Map1, Map2, Map3
from Database import Database
from Game import Game
from LiDAR import LiDAR


def main(auto):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 30)
    _ = (Map1, Map2, Map3)
    walls, trophies, parkings, crosswalks, traffic_signs, schoolzone, car = Map3
    lidar = LiDAR()
    control = Control()
    database = Database(lidar, control, car)
    # Get LiDAR data, Set Control data
    brain = Brain(database)
    # Get Control data Set LiDAR data
    game = Game(walls, trophies, parkings,
                crosswalks, traffic_signs, schoolzone, car, database)
    if auto:
        brain_thread = threading.Thread(target=brain.run,)
        brain_thread.start()
    game.run(auto=auto)
    pygame.quit()

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--auto",
            help="Do not use your keyboard command,\
                 but use pre-defined brain's command.",
            action="store_true", default=True
        )
    args = parser.parse_args()
    main(args.auto)
