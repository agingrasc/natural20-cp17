import pygame
from pygame import display, draw, Surface, Color
import pymunk
from pygame.time import Clock

from util.geometry import Vector

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game():

    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 25)
        self.last_frame_ticks = pygame.time.get_ticks()
        self.delta_t = 0

    def compute_delta_t(self):
        ticks = pygame.time.get_ticks()
        self.delta_t = ticks - self.last_frame_ticks
        self.last_frame_ticks = ticks

    def add_text(self, surface: Surface, text: str, pos: Vector):
        font = self.font.render(text, True, RED)
        surface.blit(font, pos.to_pos())

    def main(self):
        display_width = 800
        display_height = 600
        game_display: Surface = display.set_mode((display_width, display_height))
        display.set_caption('Natural 20: Challenge Pixel 2017')
        clock: Clock = pygame.time.Clock()

        circle_pos = Vector(300, 300)

        crashed = False
        while not crashed:
            self.compute_delta_t()
            self.add_text(game_display, str(self.delta_t), Vector())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                print(event)

                game_display.fill(WHITE)

            circle_pos += 10
            draw.circle(game_display, Color(255, 0, 0), circle_pos.to_pos(), 50, 0)

            pygame.display.update()
            clock.tick(30)

if __name__ == "__main__":
    game = Game()
    game.main()
