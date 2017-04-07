import functools

import pygame
from pygame.event import EventType
from pygame.surface import Surface

from display import drawer
from util.geometry import Vector


def handle(game_display: Surface, event: EventType, displayables):
    handler = dispatcher.get(event.type, None)
    if handler:
        handler(game_display, event, displayables)
    else:
        print(event)


def mouse_motion(game_display: Surface, event: EventType, displayables):
    x, y = event.dict.get("pos", (0, 0))
    displayables['x-actual-coordinate'] = drawer.add_text(game_display, str(x), Vector(800-100, 600-25))
    displayables['y-actual-coordinate'] = drawer.add_text(game_display, str(y), Vector(800-50, 600-25))


dispatcher = {pygame.MOUSEMOTION: mouse_motion}
