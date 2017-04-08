import pygame

from display.spritesheet import SpriteSheet
from util.geometry import Vector
from util.singleton import Singleton


class ImagesCache(metaclass=Singleton):
    def __init__(self):
        self.images = {}
        self.sprites_sheets = {}
        self.fonts = {}

    def add_image(self, idx: str, image_path: str):
        self.images[idx] = pygame.image.load(image_path)

    def add_sprites_sheets(self, idx: str, image_path: str, element_dimensions: Vector):
        self.sprites_sheets[idx] = SpriteSheet(image_path, element_dimensions)

    def add_font(self, idx: str, font_path: str, size):
        self.fonts[idx] = pygame.font.Font(font_path, size)

