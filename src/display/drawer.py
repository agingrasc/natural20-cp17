import functools

import math

import pygame
from pygame import draw
from pygame.surface import Surface
from typing import Tuple

from display import color
from display import dimensions
from display.cache import ImagesCache
from util.dialog import break_dialog_lines
from util.geometry import Vector

DIALOG_POLICE_SIZE = 16


def add_text(surface: Surface, text: str, pos: Vector, text_color=color.TEXT_FOREGROUND_COLOR):
    font_text = ImagesCache().fonts["tips"].render(text, True, text_color)
    return functools.partial(surface.blit, font_text, pos.to_pos())


def add_rectangle(surface: Surface, coord: Vector, size: Vector, rect_color: Tuple[int, int, int]):
    rect = pygame.Rect(coord.to_pos(), size.to_pos())
    return functools.partial(draw.rect, surface, rect_color, rect, 0)


def add_image(surface: Surface, image: Surface, pos: Vector=Vector(0,0), scale: Vector= None, angle = 0):
    if angle != 0:
        rotated_img = rot_center(image, angle)
    else:
        rotated_img = image
    if not scale is None:
        rescaled_img = pygame.transform.scale(rotated_img, scale.to_pos())
    else:
        rescaled_img = image
    return functools.partial(surface.blit, rescaled_img, pos.to_pos())


def display_dialog(surface: Surface, name: str, dialog: str):
    WIDTH = 455
    HEIGHT = 205
    BORDER = 5

    IN_WIDTH = WIDTH - BORDER
    IN_HEIGHT = HEIGHT - BORDER
    canevas = Surface((WIDTH, HEIGHT))
    canevas.fill(color.TEXT_BACKGROUND_COLOR)
    pos = Vector(dimensions.WINDOW_WIDTH-(30+IN_WIDTH), dimensions.WINDOW_HEIGHT-(30+IN_HEIGHT))
    sizes = Vector(IN_WIDTH, IN_HEIGHT)
    rect = pygame.Rect(Vector().to_pos(), sizes.to_pos())
    draw.rect(canevas, color.WHITE, rect, 5)

    font_name = ImagesCache().fonts["dialog"].render("{}: ".format(name), True, color.TEXT_NAME_COLOR)
    canevas.blit(font_name, (5, 4))
    height = 30
    for line in break_dialog_lines(dialog):
        font_text = ImagesCache().fonts["dialog"].render(line, True, color.TEXT_FOREGROUND_COLOR)
        canevas.blit(font_text, (10, height))
        height += 20
    return functools.partial(surface.blit, canevas, pos.to_pos())


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()

    return rot_image
