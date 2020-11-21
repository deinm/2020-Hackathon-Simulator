from Wall import WallSprite
from Car import CarSprite
from Trophy import TrophySprite
from Parking import Parking
from Crosswalk import Crosswalk
from TrafficSign import Right, Left


import numpy as np

Map1 = (
    [
        WallSprite((500, 0), 1000, 4),  # Boundary box
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
        WallSprite((450, 700), 900, 4),  # Horizontal line
        WallSprite((550, 500), 900, 4),
        WallSprite((900, 600), 200, 4),
        WallSprite((450, 300), 900, 4),
        WallSprite((535, 100), 930, 4),
        WallSprite((650, 650), 150, 100),  # Static obstacle - Big
        WallSprite((395, 550), 150, 100),
        WallSprite((175, 650), 150, 100),
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
    CarSprite('images/car.png', (40, 750)),
)

Map2 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 1000),
        WallSprite((1000, 400), 4, 1000),

        WallSprite((550, 350), 900, 4),
        WallSprite((450, 450), 900, 4),

        WallSprite((100, 230), 4, 240),
        WallSprite((200, 120), 4, 240),
        WallSprite((300, 230), 4, 240),
        WallSprite((400, 120), 4, 240),
        WallSprite((500, 230), 4, 240),
        WallSprite((600, 120), 4, 240),
        WallSprite((700, 230), 4, 240),
        WallSprite((800, 120), 4, 240),
        WallSprite((900, 230), 4, 240),

        WallSprite((100, 685), 4, 230),
        WallSprite((190, 570), 180, 4),

        WallSprite((380, 570), 4, 240),
        WallSprite((290, 690), 180, 4),

        WallSprite((490, 690), 4, 240),
        WallSprite((590, 570), 4, 240),
        WallSprite((640, 690), 100, 4),
        WallSprite((750, 570), 100, 4),

        WallSprite((900, 570), 4, 240),
        WallSprite((800, 685), 4, 230),

        # WallSprite((120, 200), 4, 900),
        # WallSprite((360, 450), 4, 900),

        # WallSprite((600, 450), 4, 700),
        # WallSprite((840, 450), 4, 700),
        # WallSprite((920, 100), 160, 4),
        # WallSprite((240, 350), 4, 700),
        # WallSprite((480, 350), 4, 700),
        # WallSprite((720, 350), 4, 700),
    ],
    [
        TrophySprite((930, 20))
    ],
    [

    ],
    [
        Crosswalk((60, 400), 120, 4, interval=40, phase=0),
        # Crosswalk((180, 300), 120, 4, interval=30, phase=5),
        # Crosswalk((180, 500), 120, 4, interval=30, phase=15),
        # Crosswalk((300, 200), 120, 4, interval=20, phase=30),
        # Crosswalk((300, 600), 120, 4, interval=20, phase=40),
        # Crosswalk((420, 400), 120, 4, interval=40, phase=55),
        # Crosswalk((540, 600), 120, 4, interval=20, phase=65),
        # Crosswalk((540, 200), 120, 4, interval=20, phase=80),
        # Crosswalk((660, 300), 120, 4, interval=30, phase=70),
        # Crosswalk((660, 500), 120, 4, interval=30, phase=85),
        # Crosswalk((780, 400), 120, 4, interval=40, phase=95),
    ],
    [

    ],
    CarSprite('images/car.png', (50, 750)),
)

Map3 = (
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
        Crosswalk((75, 300), 150, 4, interval=30, phase=0),
        Crosswalk((225, 500), 150, 4, interval=30, phase=8),
        Crosswalk((800, 50), 4, 100, interval=30, phase=16),
        Crosswalk((925, 150), 150, 4, interval=30, phase=24),
        Crosswalk((925, 400), 150, 4, interval=30, phase=32),
        Crosswalk((925, 600), 150, 4, interval=30, phase=40),
        Crosswalk((775, 500), 150, 4, interval=30, phase=48),
    ],
    [

    ],
    CarSprite('images/car.png', (75, 760)),
)

Map4 = (
    [
        WallSprite((500, 0), 1000, 4),
        WallSprite((500, 800), 1000, 4),
        WallSprite((0, 400), 4, 800),
        WallSprite((1000, 400), 4, 800),
        WallSprite((560, 750), 4, 100),
        WallSprite((440, 750), 4, 100),
        WallSprite((500, 600), 800, 4),
        WallSprite((220, 700), 440, 4),
        WallSprite((780, 700), 440, 4),
        WallSprite((100, 350), 4, 500),
        WallSprite((200, 250), 4, 500),
        WallSprite((300, 350), 4, 500),
        WallSprite((900, 350), 4, 500),
        WallSprite((800, 250), 4, 500),
        WallSprite((700, 350), 4, 500),
        WallSprite((500, 100), 400, 4),
        WallSprite((500, 540), 60, 4),
        WallSprite((530, 570), 4, 60),
        WallSprite((470, 570), 4, 60),
    ],
    [
        TrophySprite((465, 15))
    ],
    [

    ],
    [
        Crosswalk((50, 500), 100, 4, interval=30, phase=0),
        Crosswalk((50, 400), 100, 4, interval=30, phase=8),
        Crosswalk((50, 300), 100, 4, interval=30, phase=16),
        Crosswalk((50, 200), 100, 4, interval=30, phase=24),
        Crosswalk((250, 400), 100, 4, interval=35, phase=0),
        Crosswalk((250, 200), 100, 4, interval=35, phase=20),
        Crosswalk((950, 500), 100, 4, interval=30, phase=0),
        Crosswalk((950, 400), 100, 4, interval=30, phase=8),
        Crosswalk((950, 300), 100, 4, interval=30, phase=16),
        Crosswalk((950, 200), 100, 4, interval=30, phase=24),
        Crosswalk((750, 400), 100, 4, interval=35, phase=0),
        Crosswalk((750, 200), 100, 4, interval=35, phase=20),
    ],
    [
        Left((470, 540), 60, 60) if (np.random.random() < 0.5)
        else Right((470, 540), 60, 60)
    ],
    CarSprite('images/car.png', (500, 760)),
)