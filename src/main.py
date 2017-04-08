import collections

import pygame
from pygame import display, Surface
from pygame.time import Clock

from display import color, drawer, dimensions, button
from display.action.indicator import DEFAULT_FLOOR_INDICATOR_POS, DEFAULT_FLOOR_INDICATOR_SCALE, FloorIndicatorAction
from display.button import ButtonBuilder, NUMBER_OF_BUTTONS_ROWS, NUMBER_OF_BUTTONS_COLS
from display.cache import ImagesCache
from display.drawer import DIALOG_POLICE_SIZE
from domain.state.stateexecutor import StateExecutor
from domain import images
from event import handler
from util.geometry import Vector
from domain.blackboard import Blackboard

FPS = 60
DEFAULT_BACKGROUND_IMAGE_PATH = 'resource/background/ascenseur.png'


class Game:
    def __init__(self):
        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_t = 0
        self.display_width = dimensions.WINDOW_WIDTH
        self.display_height = dimensions.WINDOW_HEIGHT
        self.persistent_display = collections.OrderedDict()
        self.temporary_display = []
        self.actions = []
        self.state_executor = StateExecutor()
        self.image_cache = ImagesCache()
        self.init_cache()

    def init_cache(self):
        self.image_cache.add_image(*images.BACKGROUND_IMAGE)
        self.image_cache.add_image(*images.FLOOR_INDICATOR)
        self.image_cache.add_font("dialog", "resource/font/OldNewspaperTypes.ttf", DIALOG_POLICE_SIZE)
        self.image_cache.add_font("tips", "resource/font/OldStandard-Regular.ttf", 20)

        for i in range(10):
            idx, path = images.BUTTON_PATTERN
            idx = idx.format(i)
            path = path.format(i)
            self.image_cache.add_sprites_sheets(idx, path, button.BUTTON_SPRITE_SIZE)

    def compute_delta_t(self):
        ticks = pygame.time.get_ticks()
        self.delta_t = ticks - self.last_frame_ticks
        self.last_frame_ticks = ticks

    def construct_background(self, game_display):
        self.persistent_display['background'] = \
            drawer.add_image(game_display,
                             self.image_cache.images['background'],
                             Vector(),
                             Vector(dimensions.WINDOW_WIDTH, dimensions.WINDOW_HEIGHT),
                             0)
        self.persistent_display['floor-indicator'] = \
            drawer.add_image(game_display,
                             self.image_cache.images['floor-indicator'],
                             DEFAULT_FLOOR_INDICATOR_POS,
                             DEFAULT_FLOOR_INDICATOR_SCALE,
                             89)

    def init_keypad(self, game_display):
        for i in range(NUMBER_OF_BUTTONS_COLS):
            for j in range(NUMBER_OF_BUTTONS_ROWS):
                floor = button.compute_floor(i, j)
                self.persistent_display["button-{}".format(floor)] = ButtonBuilder().add_button(game_display, i, j)

    def main(self):

        game_display: Surface = display.set_mode((self.display_width, self.display_height))
        display.set_caption('Natural 20: Challenge Pixel 2017')
        clock: Clock = pygame.time.Clock()

        self.construct_background(game_display)
        self.init_keypad(game_display)

        indicator_action = FloorIndicatorAction(1, 5)
        crashed = False
        accumulated_time = 0
        while not crashed:
            game_display.fill(color.BLACK)
            self.compute_delta_t()

            for displayable in self.persistent_display.values():
                displayable()
            for displayable in self.temporary_display:
                displayable()
            self.temporary_display.clear()

            domain_action = self.state_executor.exec(self.delta_t, self.actions)
            self.actions.clear()
            if domain_action.persistent_name:
                self.persistent_display[domain_action.persistent_name] = domain_action.display(game_display, self.delta_t)
            else:
                self.temporary_display.append(domain_action.display(game_display, self.delta_t))

            self.temporary_display.append(drawer.add_text(game_display, "{}".format(int(1/(self.delta_t/1000))), Vector(), color.YELLOW))
            str_tips = "{:0>6.2f}$".format(Blackboard().tips)
            self.temporary_display.append(drawer.add_text(game_display, str_tips, Vector(self.display_width - len(str_tips)*9, 0), color.GREEN))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                else:
                    self.actions.append(handler.handle(game_display, event, self.persistent_display))

            self.actions = [action for action in self.actions if action]

            # TEST SECTION

            pygame.display.update()

            clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.main()
