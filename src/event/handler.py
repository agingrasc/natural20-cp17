import functools

import pygame
from pygame.event import EventType
from pygame.surface import Surface

from display import drawer
from display.button import ButtonBuilder
from event.action import FloorSelected, UserKeyAction
from util.geometry import Vector
from display import color


def handle(game_display: Surface, event: EventType, displayables):
    handler = dispatcher.get(event.type, None)
    if handler:
        return handler(game_display, event, displayables)
    else:
        return None


def mouse_motion(game_display: Surface, event: EventType, displayables):
    x, y = event.dict.get("pos", (0, 0))
    # displayables['x-actual-coordinate'] = drawer.add_text(game_display, str(x), Vector(800-100, 600-25), text_color=color.RED)
    # displayables['y-actual-coordinate'] = drawer.add_text(game_display, str(y), Vector(800-50, 600-25), text_color=color.RED)
    return None


def on_click(game_display: Surface, event: EventType, displayables):
    click_coordinate = event.dict['pos']
    pos = Vector(*click_coordinate)
    for button in ButtonBuilder().buttons:
        if button.is_inside(pos):
            return FloorSelected(button.floor)
    return UserKeyAction()


def on_keydown(game_display: Surface, event: EventType, displaybles):
    if event.dict['key'] == pygame.K_SPACE:
        return UserKeyAction()
    if event.dict['key'] == pygame.K_0:
        act = FloorSelected(0)
        return act
    if event.dict['key'] == pygame.K_1:
        act = FloorSelected(1)
        return act
    if event.dict['key'] == pygame.K_2:
        act = FloorSelected(2)
        return act
    if event.dict['key'] == pygame.K_3:
        act = FloorSelected(3)
        return act
    if event.dict['key'] == pygame.K_4:
        act = FloorSelected(4)
        return act
    if event.dict['key'] == pygame.K_5:
        act = FloorSelected(5)
        return act
    if event.dict['key'] == pygame.K_6:
        act = FloorSelected(6)
        return act
    if event.dict['key'] == pygame.K_7:
        act = FloorSelected(7)
        return act
    if event.dict['key'] == pygame.K_8:
        act = FloorSelected(8)
        return act
    if event.dict['key'] == pygame.K_9:
        act = FloorSelected(9)
        return act


dispatcher = {pygame.MOUSEMOTION: mouse_motion,
              pygame.MOUSEBUTTONDOWN: on_click,
              pygame.KEYDOWN: on_keydown}
