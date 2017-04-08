import pygame

from display import drawer
from display.action.interface import IDomainAction
from util.geometry import Vector

KEY_FRAME_TIME = 500


class SpriteAnimationAction(IDomainAction):
    def __init__(self, sprite_sheet_path):
        self.img = pygame.image.load(sprite_sheet_path)
        self.elapsed_time = 0
        self.pos = Vector()
        self.scale = Vector()

    def display(self, game_display, dt):
        if self.finished:
            pass
        elif self.elapsed_time < KEY_FRAME_TIME:
            self.elapsed_time += dt
        # TODO: branche qui va recuperer la prochaine sprite
        return self.draw_image(game_display)

    def draw_image(self, game_display):
        return drawer.add_image_from_sprite_sheet(game_display, None, self.pos, self.scale)
