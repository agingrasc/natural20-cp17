import functools

import pygame
from pygame import draw
from pygame.surface import Surface

from display import color, drawer
from util.geometry import Vector
from util.singleton import Singleton

BUTTON_SIZE = 65
DEFAULT_MIN_WIDTH = 75
DEFAULT_MIN_HEIGHT = 350
DEFAULT_MARGIN = 5


class Button:
    def __init__(self, coordinates: Vector, size: Vector):
        self.coordinates = coordinates
        self.size = size

    def display(self, surface: Surface):
        return drawer.add_rectangle(surface, self.coordinates, self.size, color.PURPLE)


class ButtonBuilder(metaclass=Singleton):
    def __init__(self):
        self.min_width = DEFAULT_MIN_WIDTH
        self.min_height = DEFAULT_MIN_HEIGHT
        self.margin = DEFAULT_MARGIN
        self.buttons = []

    def add_button(self, surface: Surface, row, col):
        coord = Vector(self.min_width + row * (BUTTON_SIZE + 5), self.min_height + col * (BUTTON_SIZE + 5))
        size = Vector(BUTTON_SIZE, BUTTON_SIZE)
        button = Button(coord, size)
        self.buttons.append(button)
        return button.display(surface)

