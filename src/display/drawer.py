import functools

from typing import Dict

import pygame
from pygame import draw
from pygame.surface import Surface

from display import color, dimensions
from util.geometry import Vector


def add_text(surface: Surface, text: str, pos: Vector):
    font = pygame.font.SysFont('Arial', 25)
    font_text = font.render(text, True, color.RED)
    return functools.partial(surface.blit, font_text, pos.to_pos())


def display_dialog(surface: Surface, dialog: str):
    canevas = Surface(Vector(405, 255).to_pos())
    pos = Vector(dimensions.WINDOW_WIDTH-(50+350), dimensions.WINDOW_HEIGHT-(50+200))
    sizes = Vector(350, 200)
    rect = pygame.Rect(Vector().to_pos(), sizes.to_pos())
    draw.rect(canevas, color.WHITE, rect, 5)
    font = pygame.font.SysFont("Arial", 25)
    font_text = font.render(dialog, True, color.BLUE)
    canevas.blit(font_text, Vector(10, 10).to_pos())
    return functools.partial(surface.blit, canevas, pos.to_pos())
