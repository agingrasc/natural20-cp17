import pygame

from display import drawer
from display.action.interface import IDomainAction
from display.button import ButtonBuilder, Button
from display.cache import ImagesCache
from display.spritesheet import SpriteSheet
from util.geometry import Vector

KEY_FRAME_TIME = 1000


class SpriteAnimationAction(IDomainAction):
    def __init__(self, sprite_sheet_id):
        super().__init__()
        self.sprite_sheet: SpriteSheet = ImagesCache().sprites_sheets[sprite_sheet_id]
        self.elapsed_time = 0
        self.pos = Vector()
        self.scale = Vector()
        self.sprites = self.sprite_sheet.all_sprites()
        self.idx = 0

    def display(self, game_display, dt):
        if self.finished:
            pass
        elif self.elapsed_time < KEY_FRAME_TIME:
            self.elapsed_time += dt
        elif self.idx + 1 < len(self.sprites):
            self.idx += 1
            print("New animation sprite index: {}".format(self.idx))
            self.elapsed_time = 0
        return self.draw_image(game_display)

    def draw_image(self, game_display):
        return drawer.add_image(game_display, self.sprites[self.idx], self.pos, self.scale)


class ButtonAnimationAction(SpriteAnimationAction):
    def __init__(self, floor):
        button: Button = ButtonBuilder().get_button_for_floor(floor)
        super().__init__(button.idx)
        self.pos = button.coordinates
        self.scale = button.size



