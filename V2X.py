from Car import CarSprite
import numpy as np


class V2X:
    MAX_DISTANCE = 400

    def __init__(self, position, name="V2X"):
        self.name = name
        self.position = position

    def is_in_range(self, car: CarSprite):
        x0, y0 = self.position
        left, top, width, height = car.rect
        x = left + (width / 2)
        y = top + (height / 2)
        distance = np.sqrt((x0 - x) ** 2 + (y0 - y) ** 2)

        if distance > V2X.MAX_DISTANCE:
            return False
        else:
            return True
