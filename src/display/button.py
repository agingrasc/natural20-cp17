import functools

import pygame
from pygame import draw
from pygame.surface import Surface

from display import color
from util.geometry import Vector

BUTTON_SIZE = 65
DEFAULT_MIN_WIDTH = 75
DEFAULT_MIN_HEIGHT = 350
DEFAULT_MARGIN = 5


class ButtonBuilder:
    def __init__(self):
        self.min_width = DEFAULT_MIN_WIDTH
        self.min_height = DEFAULT_MIN_HEIGHT
        self.margin = DEFAULT_MARGIN

    def add_button(self, surface: Surface, row, col):
        coord = Vector(self.min_width + row * (BUTTON_SIZE + 5), self.min_height + col * (BUTTON_SIZE + 5))

        rect = pygame.Rect(coord.to_pos(), Vector(BUTTON_SIZE, BUTTON_SIZE).to_pos())
        return functools.partial(draw.rect, surface, color.PURPLE, rect, 0)