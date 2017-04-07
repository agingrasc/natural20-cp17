import functools

import pygame
from pygame import draw
from pygame.surface import Surface
from typing import Tuple

from display import color
from display import dimensions
from util.dialog import break_dialog_lines
from util.geometry import Vector



def add_text(surface: Surface, text: str, pos: Vector, text_color=color.TEXT_FOREGROUND_COLOR):
    font = pygame.font.SysFont('Arial', 25)
    font_text = font.render(text, True, text_color)
    return functools.partial(surface.blit, font_text, pos.to_pos())


def add_rectangle(surface: Surface, coord: Vector, size: Vector, rect_color: Tuple[int, int, int]):
    rect = pygame.Rect(coord.to_pos(), size.to_pos())
    return functools.partial(draw.rect, surface, rect_color, rect, 0)


def add_image(surface: Surface, image_path, pos: Vector, scale: Vector):
    img = pygame.image.load(image_path)
    rescaled_img = pygame.transform.scale(img, scale.to_pos())
    return functools.partial(surface.blit, rescaled_img, pos.to_pos())


def add_image_from_sprite_sheet(surface: Surface, sprite_sheet_path: str, pos: Vector, scale: Vector,
                                sprite_sheet_size: Vector, sprite_sheet_offset: Vector):
    sprite_sheet = pygame.image.load(sprite_sheet_path)
    area = sprite_sheet_offset.x, sprite_sheet_offset.y, sprite_sheet_size.x, sprite_sheet_size.y
    img = Surface(sprite_sheet_size.to_pos(), pygame.SRCALPHA)
    img.blit(sprite_sheet, Vector(0, 0).to_pos(), area)
    rescaled_img = pygame.transform.scale(img, scale.to_pos())
    return functools.partial(surface.blit, rescaled_img, pos.to_pos())


def display_dialog(surface: Surface, dialog: str):
    canevas = Surface(Vector(355, 205).to_pos())
    canevas.fill(color.TEXT_BACKGROUND_COLOR)
    pos = Vector(dimensions.WINDOW_WIDTH-(50+350), dimensions.WINDOW_HEIGHT-(50+200))
    sizes = Vector(350, 200)
    rect = pygame.Rect(Vector().to_pos(), sizes.to_pos())
    draw.rect(canevas, color.WHITE, rect, 5)

    font = pygame.font.SysFont("Arial", 25)

    height = 10
    for line in break_dialog_lines(dialog):
        font_text = font.render(line, True, color.TEXT_FOREGROUND_COLOR)
        canevas.blit(font_text, Vector(10, height).to_pos())
        height += 15
    return functools.partial(surface.blit, canevas, pos.to_pos())


