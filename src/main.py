import collections

import pygame
from pygame import display, Surface
from pygame.time import Clock

from display import color, drawer, dimensions
from display.button import ButtonBuilder, NUMBER_OF_BUTTONS_ROWS, NUMBER_OF_BUTTONS_COLS
from domain.state.stateexecutor import StateExecutor
from event import handler
from util.geometry import Vector

FPS = 60
DEFAULT_BACKGROUND_IMAGE_PATH = 'resource/background/ascenseur.png'
DEFAULT_FLOOR_INDICATOR_IMAGE_PATH = 'resource/img/level_counter.png'


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

    def compute_delta_t(self):
        ticks = pygame.time.get_ticks()
        self.delta_t = ticks - self.last_frame_ticks
        self.last_frame_ticks = ticks

    def construct_background(self, game_display):
        self.persistent_display['background'] = \
            drawer.add_image(game_display,
                             DEFAULT_BACKGROUND_IMAGE_PATH,
                             Vector(),
                             Vector(dimensions.WINDOW_WIDTH, dimensions.WINDOW_HEIGHT))
        self.persistent_display['floor-indicator'] = \
            drawer.add_image(game_display,
                             DEFAULT_FLOOR_INDICATOR_IMAGE_PATH,
                             Vector(135-110, 105-116),
                             Vector(210, 210))

    def init_keypad(self, game_display):
        for i in range(NUMBER_OF_BUTTONS_COLS):
            for j in range(NUMBER_OF_BUTTONS_ROWS):
                self.persistent_display["button-{}-{}".format(i, j)] = ButtonBuilder().add_button(game_display, i, j)

    def main(self):
        game_display: Surface = display.set_mode((self.display_width, self.display_height))
        display.set_caption('Natural 20: Challenge Pixel 2017')
        clock: Clock = pygame.time.Clock()

        self.construct_background(game_display)
        self.init_keypad(game_display)
        crashed = False
        while not crashed:
            game_display.fill(color.BLACK)

            for displayable in self.persistent_display.values():
                displayable()
            for displayable in self.temporary_display:
                displayable()
            self.temporary_display.clear()

            domain_action = self.state_executor.exec(self.delta_t, self.actions)
            self.actions.clear()
            self.temporary_display.append(domain_action.display(game_display, self.delta_t))

            self.compute_delta_t()
            self.temporary_display.append(drawer.add_text(game_display, "{}".format(int(1/(self.delta_t/1000))), Vector(), color.YELLOW))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                else:
                    self.actions.append(handler.handle(game_display, event, self.persistent_display))

            self.actions = [action for action in self.actions if action]

            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.main()
