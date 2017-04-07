import pygame
from pygame import display, Surface
from pygame.time import Clock

from display import color, drawer, dimensions
from display.action.dialog import Dialog
from display.button import ButtonBuilder
from event import handler
from util.geometry import Vector

FPS = 60


class Game:
    def __init__(self):
        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_t = 0
        self.display_width = dimensions.WINDOW_WIDTH
        self.display_height = dimensions.WINDOW_HEIGHT
        self.persistent_display = {}
        self.temporary_display = []

    def compute_delta_t(self):
        ticks = pygame.time.get_ticks()
        self.delta_t = ticks - self.last_frame_ticks
        self.last_frame_ticks = ticks

    def init_keypad(self, game_display):
        for i in range(3):
            for j in range(3):
                self.persistent_display["button-{}-{}".format(i, j)] = ButtonBuilder().add_button(game_display, i, j)

    def main(self):
        game_display: Surface = display.set_mode((self.display_width, self.display_height))
        display.set_caption('Natural 20: Challenge Pixel 2017')
        clock: Clock = pygame.time.Clock()

        dialog = Dialog("Hello, world! Foo bar baz\nGood bye!lakjadslkdjaslkjdaslkdj")
        self.init_keypad(game_display)
        crashed = False
        while not crashed:
            game_display.fill(color.BLACK)

            for displayable in self.temporary_display:
                displayable()
            self.temporary_display.clear()
            for displayable in self.persistent_display.values():
                displayable()

            self.compute_delta_t()
            self.temporary_display.append(drawer.add_text(game_display, "{}".format(int(1/(self.delta_t/1000))), Vector(), color.YELLOW))
            self.temporary_display.append(dialog.display(game_display, self.delta_t))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                else:
                    handler.handle(game_display, event, self.persistent_display)

            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.main()
