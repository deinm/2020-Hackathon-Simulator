import pygame
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT


class Control:
    def __init__(self):
        self.up_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': K_UP})
        self.down_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': K_DOWN})
        self.right_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': K_RIGHT})
        self.left_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': K_LEFT})

    def up(self):
        try:
            pygame.event.post(self.up_event)
        except pygame.error:
            pass

    def down(self):
        try:
            pygame.event.post(self.down_event)
        except pygame.error:
            pass

    def right(self):
        try:
            pygame.event.post(self.right_event)
        except pygame.error:
            pass

    def left(self):
        try:
            pygame.event.post(self.left_event)
        except pygame.error:
            pass
