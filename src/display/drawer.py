import functools

from typing import Dict

import pygame
from pygame import draw
from pygame.surface import Surface

from display import color
from util.geometry import Vector


def add_text(surface: Surface, text: str, pos: Vector):
    font = pygame.font.SysFont('Arial', 25)
    font_text = font.render(text, True, color.RED)
    return functools.partial(surface.blit, font_text, pos.to_pos())


def display_dialog(surface: Surface, dialog: str):
    pos = Vector(800-(50+350), 600-(50+200))
    dimensions = Vector(350, 200)
    rect = pygame.Rect(pos.to_pos(), dimensions.to_pos())
    return functools.partial(draw.rect, surface, color.WHITE, rect, 5)
