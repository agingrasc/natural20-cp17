from display import dimensions, drawer
from display.action.interface import IDomainAction
from display.cache import ImagesCache
from display.spritesheet import SpriteSheet
from util.geometry import Vector


class FloorCallAction(IDomainAction):
    def __init__(self, floor):
        if floor is None:
            self.floor = -1
        else:
            self.floor = floor
        self.size = Vector(dimensions.WINDOW_WIDTH, dimensions.WINDOW_HEIGHT)
        self.persistent_name = 'background'

    def display(self, game_display, dt):
        self.finished = True
        sprite_sheet: SpriteSheet = ImagesCache().sprites_sheets['background']
        sprite = sprite_sheet.get_element(0, self.floor + 1)
        return drawer.add_image(game_display, sprite, Vector(), self.size)
