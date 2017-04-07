import functools

import pygame
from pygame import draw
from pygame.surface import Surface

from display import color, drawer
from util.geometry import Vector
from util.singleton import Singleton

BUTTON_SIZE = 35
DEFAULT_MIN_WIDTH = 100
DEFAULT_MIN_HEIGHT = 175
DEFAULT_MARGIN = 2
NUMBER_OF_BUTTONS_ROWS = 5
NUMBER_OF_BUTTONS_COLS = 2
DEFAULT_BUTTON_IMAGE_PATH_PATTERN = "resource/sprite_sheets/button_{}_sprite_sheet.png"


class Button:
    def __init__(self, coordinates: Vector, size: Vector, floor: int):
        self.coordinates = coordinates
        self.size = size
        self.floor = floor

    def display(self, surface: Surface):
        sprite_sheet_size = Vector(108, 109)
        sprite_sheet_offset = Vector(0, 0)
        return drawer.add_image_from_sprite_sheet(surface, DEFAULT_BUTTON_IMAGE_PATH_PATTERN.format(1), self.coordinates, self.size, sprite_sheet_size, sprite_sheet_offset)

    def is_inside(self, pos: Vector):
        down_right_corner = self.coordinates + self.size
        return self.coordinates.x <= pos.x <= down_right_corner.x and self.coordinates.y <= pos.y <= down_right_corner.y


class ButtonBuilder(metaclass=Singleton):
    def __init__(self):
        self.min_width = DEFAULT_MIN_WIDTH
        self.min_height = DEFAULT_MIN_HEIGHT
        self.margin = DEFAULT_MARGIN
        self.buttons = []

    def add_button(self, surface: Surface, row, col):
        coord = Vector(self.min_width + row * (BUTTON_SIZE + DEFAULT_MARGIN), self.min_height + col * (BUTTON_SIZE + DEFAULT_MARGIN))
        size = Vector(BUTTON_SIZE, BUTTON_SIZE)
        floor = (NUMBER_OF_BUTTONS_ROWS - col) * NUMBER_OF_BUTTONS_COLS + row - NUMBER_OF_BUTTONS_COLS
        button = Button(coord, size, floor)
        self.buttons.append(button)
        return button.display(surface)
