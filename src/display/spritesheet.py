import pygame

from util.geometry import Vector


class SpriteSheet:
    """" Charge en memoire une sprite sheet et permet d'y acceder correctement. """

    def __init__(self, sprite_sheet_path: str, element_dimensions: Vector):
        self.image = pygame.image.load(sprite_sheet_path)
        self.image_size = Vector(*self.image.get_rect().size)
        self.element_dimensions = element_dimensions

    def get_element(self, row, col):
        """ Return None si out of bound. """
        if self.is_inbound(col, row):
            sprite = pygame.Surface(self.element_dimensions.to_pos(), pygame.SRCALPHA)
            x_offset = col * self.element_dimensions.x
            y_offset = row * self.element_dimensions.y
            area = (x_offset, y_offset, self.element_dimensions.x, self.element_dimensions.y)
            sprite.blit(self.image_size, (0, 0), area)
            return sprite

    def is_inbound(self, col, row):
        x_in_bound = (col + 1) * self.element_dimensions.x <= self.image_size.x
        y_in_bound = (row + 1) * self.element_dimensions.y <= self.image_size.y
        return x_in_bound and y_in_bound

    def all_sprites(self):
        max_col = int(self.image_size.x / self.element_dimensions.x)
        max_row = int(self.image_size.y / self.element_dimensions.y)
        for row in range(max_row):
            for col in range(max_col):
                yield self.get_element(row, col)
