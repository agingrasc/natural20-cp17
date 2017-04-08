import functools

import math

import pygame
from pygame import draw
from pygame.surface import Surface
from typing import Tuple

from display import color
from display import dimensions
from util.dialog import break_dialog_lines
from util.geometry import Vector

DIALOG_POLICE_SIZE = 16


def add_text(surface: Surface, text: str, pos: Vector, text_color=color.TEXT_FOREGROUND_COLOR):
    font = pygame.font.SysFont('Arial', 25)
    font_text = font.render(text, True, text_color)
    return functools.partial(surface.blit, font_text, pos.to_pos())


def add_rectangle(surface: Surface, coord: Vector, size: Vector, rect_color: Tuple[int, int, int]):
    rect = pygame.Rect(coord.to_pos(), size.to_pos())
    return functools.partial(draw.rect, surface, rect_color, rect, 0)


def add_image(surface: Surface, image: Surface, pos: Vector, scale: Vector, angle = 0):
    rotated = rot_center(image, angle)
    rescaled_img = pygame.transform.scale(rotated, scale.to_pos())
    return functools.partial(surface.blit, rescaled_img, pos.to_pos())


def display_dialog(surface: Surface, name: str, dialog: str):
    canevas = Surface((355, 205))
    canevas.fill(color.TEXT_BACKGROUND_COLOR)
    pos = Vector(dimensions.WINDOW_WIDTH-(50+350), dimensions.WINDOW_HEIGHT-(50+200))
    sizes = Vector(350, 200)
    rect = pygame.Rect(Vector().to_pos(), sizes.to_pos())
    draw.rect(canevas, color.WHITE, rect, 5)
    font = pygame.font.Font("resource/font/OldNewspaperTypes.ttf", DIALOG_POLICE_SIZE)
    font_name = font.render("{}: ".format(name), True, color.TEXT_NAME_COLOR)
    canevas.blit(font_name, (5, 4))
    height = 30
    for line in break_dialog_lines(dialog):
        font_text = font.render(line, True, color.TEXT_FOREGROUND_COLOR)
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
