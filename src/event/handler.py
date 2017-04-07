import pygame
from pygame.event import EventType
from pygame.surface import Surface


def handle(game_display: Surface, event: EventType):
    handler = dispatcher.get(event.type, None)
    if handler:
        handler(game_display, event)
    else:
        print(event)


def mouse_motion(game_display: Surface, event: EventType):
    pass


dispatcher = {pygame.MOUSEMOTION: mouse_motion}
