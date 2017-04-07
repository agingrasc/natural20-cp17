import pygame
from pygame import display, Surface
from pygame.time import Clock

from display import color, drawer
from event import handler
from util.geometry import Vector


class Game:
    def __init__(self):
        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_t = 0
        self.display_width = 800
        self.display_height = 600

    def compute_delta_t(self):
        ticks = pygame.time.get_ticks()
        self.delta_t = ticks - self.last_frame_ticks
        self.last_frame_ticks = ticks

    def main(self):
        game_display: Surface = display.set_mode((self.display_width, self.display_height))
        display.set_caption('Natural 20: Challenge Pixel 2017')
        clock: Clock = pygame.time.Clock()

        crashed = False
        while not crashed:
            game_display.fill(color.BLACK)
            self.compute_delta_t()
            drawer.add_text(game_display, str(self.delta_t), Vector())
            drawer.display_dialog(game_display, "Hello, world!")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                else:
                    handler.handle(game_display, event)
                print(event)

            pygame.display.update()
            clock.tick(30)

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.main()
