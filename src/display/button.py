import functools

import pygame
from pygame import draw
from pygame.surface import Surface

from display import color, drawer
from display.cache import ImagesCache
from display.spritesheet import SpriteSheet
from util.geometry import Vector
from util.singleton import Singleton
from domain import images

BUTTON_SIZE = 26
BUTTON_SPRITE_SIZE = Vector(107, 107)
DEFAULT_MIN_WIDTH = 107
DEFAULT_MIN_HEIGHT = 175
DEFAULT_MARGIN = 2
NUMBER_OF_BUTTONS_ROWS = 5
NUMBER_OF_BUTTONS_COLS = 2


class Button:
    def __init__(self, coordinates: Vector, size: Vector, floor: int):
        idx, _ = images.BUTTON_PATTERN
        self.idx = idx.format(floor)
        self.coordinates = coordinates
        self.size = size
        self.floor = floor

    def display(self, surface: Surface):
        img_cache = ImagesCache()
        sprite_sheet: SpriteSheet = img_cache.sprites_sheets['button-{}'.format(self.floor)]
        sprite = sprite_sheet.get_element(0, 0)
        return drawer.add_image(surface, sprite, self.coordinates, self.size)

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
        floor = compute_floor(row, col)
        button = Button(coord, size, floor)
        self.buttons.append(button)
        return button.display(surface)

    def add_button_hack_for_ut(self, row, col):
        floor = compute_floor(row, col)
        button = Button((0, 0), (0,0), floor)
        self.buttons.append(button)

    def get_button_for_floor(self, floor):
        for button in self.buttons:
            if button.floor == floor:
                return button


def compute_floor(row, col):
    return (NUMBER_OF_BUTTONS_ROWS - col) * NUMBER_OF_BUTTONS_COLS + row - NUMBER_OF_BUTTONS_COLS

