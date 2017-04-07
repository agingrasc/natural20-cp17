import functools

import pygame
from pygame import draw
from pygame.surface import Surface

from display import color
from util.geometry import Vector

BUTTON_SIZE = 65


def add_button(surface: Surface, row, col):
    min_width = 75
    min_heigth = 350
    coord = Vector(min_width + row * (BUTTON_SIZE + 5), min_heigth + col * (BUTTON_SIZE + 5))

    rect = pygame.Rect(coord.to_pos(), Vector(BUTTON_SIZE, BUTTON_SIZE).to_pos())
    return functools.partial(draw.rect, surface, color.PURPLE, rect, 0)