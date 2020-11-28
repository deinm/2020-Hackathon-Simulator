from Wall import WallSprite
from Wall import invisible_WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from Parking import Parking
from Crosswalk import Crosswalk
from Schoolzone import Schoolzone
from TrafficSign import Right, Left

import random
import numpy as np

Map1 = (
    [
        WallSprite((500, 0), 1000, 4),  # Boundary box
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
        WallSprite((450, 700), 900, 4),  # Horizontal line
        WallSprite((550, 500), 900, 4),
        WallSprite((450, 300), 900, 4),
        WallSprite((535, 100), 930, 4),
        WallSprite((910, 550), 180, 100),  # Static obstacle - Big
        WallSprite((650, 650), 150, 100),
        WallSprite((360, 550), 180, 100),
        WallSprite((100, 650), 200, 100),
        WallSprite((100, 440), 4, 120),  # Static obstacle - Small ver1
        WallSprite((270, 360), 4, 120),
        WallSprite((440, 440), 4, 120),
        WallSprite((610, 360), 4, 120),
        WallSprite((780, 440), 4, 120),
        WallSprite((900, 360), 4, 120),
        WallSprite((900, 230), 4, 140),  # Static obstacle - Small ver2
        WallSprite((750, 170), 4, 140),
        WallSprite((650, 230), 4, 140),
        WallSprite((550, 170), 4, 140),
        WallSprite((480, 230), 4, 140),
        WallSprite((410, 170), 4, 140),
        WallSprite((310, 230), 4, 140),
        WallSprite((210, 170), 4, 140),
        WallSprite((30, 230), 60, 140),
    ],
    [
        TrophySprite((930, 15))
    ],
    [

    ],
    [

    ],
    [

    ],
    [

    ],
    CarSprite('images/car.png', (40, 750), 270),
)


Map2 = (
    [
        WallSprite((450, 700), 4, 200),
        WallSprite((510, 550), 4, 100),
        WallSprite((480, 500), 60, 4),
        WallSprite((480, 600), 60, 4),
        WallSprite((450, 300), 4, 400),
        WallSprite((550, 0), 200, 4),
        WallSprite((500, 100), 100, 4),
        WallSprite((550, 150), 4, 100),
        WallSprite((610, 150), 4, 100),
        WallSprite((580, 200), 60, 4),
        WallSprite((730, 100), 240, 4),
        WallSprite((850, 400), 4, 600),
        WallSprite((700, 500), 4, 600),
        WallSprite((775, 200), 150, 4),
        WallSprite((150, 460), 4, 720),
        WallSprite((300, 340), 4, 720),
        WallSprite((500, 800), 1000, 4),
        WallSprite((500, 0), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
    ],
    [
        TrophySprite((745, 230))
    ],
    [
        Parking((450, 500), 60, 100),
        Parking((550, 100), 60, 100),

    ],
    [
        Crosswalk((75, 300), 150, 4, interval=random.randint(20, 40), phase=0),
        Crosswalk((225, 500), 150, 4, interval=random.randint(20, 40), phase=8),
        Crosswalk((800, 50), 4, 100, interval=random.randint(20, 40), phase=16),
        Crosswalk((925, 150), 150, 4, interval=random.randint(20, 40), phase=24),
        Crosswalk((925, 400), 150, 4, interval=random.randint(20, 40), phase=32),
        Crosswalk((925, 600), 150, 4, interval=random.randint(20, 40), phase=40),
        Crosswalk((775, 500), 150, 4, interval=random.randint(20, 40), phase=48),
    ],
    [

    ],
    [

    ],
    CarSprite('images/car.png', (75, 760)),
)


Map3 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 1000),
        WallSprite((1000, 400), 4, 1000),

        WallSprite((550, 350), 900, 4),
        WallSprite((450, 450), 900, 4),

        WallSprite((100, 220), 4, 260),
        WallSprite((200, 130), 4, 260),
        WallSprite((300, 220), 4, 260),
        WallSprite((400, 130), 4, 260),
        WallSprite((500, 220), 4, 260),
        WallSprite((600, 130), 4, 260),
        WallSprite((700, 220), 4, 260),
        WallSprite((800, 130), 4, 260),
        WallSprite((900, 220), 4, 260),
        WallSprite((100, 685), 4, 230),

        invisible_WallSprite((190, 570), 180, 4),
        invisible_WallSprite((380, 570), 4, 235),
        invisible_WallSprite((290, 690), 180, 4),
        invisible_WallSprite((485, 670), 4, 255),
        invisible_WallSprite((590, 570), 4, 235),
        invisible_WallSprite((640, 690), 100, 4),
        invisible_WallSprite((750, 570), 100, 4),

        invisible_WallSprite((900, 580), 4, 260),
        invisible_WallSprite((800, 685), 4, 225),
    ],
    [
        TrophySprite((920, 270))
    ],
    [

    ],
    [
        Crosswalk((50, 180), 100, 4, interval=random.randint(20, 40), phase=0),
        Crosswalk((150, 240), 100, 4, interval=random.randint(20, 40), phase=10),

        Crosswalk((250, 115), 100, 4, interval=random.randint(20, 40), phase=20),
        Crosswalk((350, 180), 100, 4, interval=random.randint(20, 40), phase=30),

        Crosswalk((450, 110), 100, 4, interval=random.randint(20, 40), phase=40),
        Crosswalk((550, 110), 100, 4, interval=random.randint(20, 40), phase=50),

        Crosswalk((650, 150), 100, 4, interval=random.randint(20, 40), phase=60),
        Crosswalk((750, 200), 100, 4, interval=random.randint(20, 40), phase=70),

        Crosswalk((850, 180), 100, 4, interval=random.randint(20, 40), phase=80),
        Crosswalk((950, 220), 100, 4, interval=random.randint(20, 40), phase=90),
    ],
    [

    ],
    [
        Schoolzone((250, 350), 550, 100),
    ],

    CarSprite('images/car.png', (50, 750)),

)
