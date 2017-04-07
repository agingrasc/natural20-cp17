import pygame
from pygame import draw
from pygame.surface import Surface

from display import color
from util.geometry import Vector


def add_text(surface: Surface, text: str, pos: Vector):
    font = pygame.font.SysFont('Arial', 25)
    font_text = font.render(text, True, color.RED)
    surface.blit(font_text, pos.to_pos())


def display_dialog(surface: Surface, dialog: str):
    pos = Vector(300, 300)
    dimensions = Vector(50, 50)
    rect = pygame.Rect(pos.to_pos(), dimensions.to_pos())
    draw.rect(surface, color.WHITE, rect, 10)
    print(rect)

