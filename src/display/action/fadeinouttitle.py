import functools

import pygame

from display import drawer
from display.action.client import POS_CHARACTER
from display.action.interface import IDomainAction
from display.cache import ImagesCache
from util.geometry import Vector

IN_OUT_TIME_SECOND = 0.6

class FadeInOutTitleAction(IDomainAction):
    def __init__(self, client_name: str, is_in):
        super().__init__()
        self.client_name = client_name
        self.is_in = is_in
        self.accumulated_time = 0

    def display(self, game_display, dt):
        self.image = ImagesCache().images[self.client_name]
        move = Vector(0, 500)
        if self.accumulated_time < IN_OUT_TIME_SECOND:
            self.accumulated_time += dt/1000
        else:
            self.finished = True
        per = self.accumulated_time/IN_OUT_TIME_SECOND
        if self.is_in:
            move = move.multiply(1-per)
        else:
            move = move.multiply(per)
        height = self.image.get_rect().size[1]
        pos = POS_CHARACTER- Vector(0, height) + move
        return functools.partial(game_display.blit, self.image, pos.to_pos())


#elapsed, start, end, total
def easing(t, b, c, d):
    t /= d
    return -c * t * (t - 2) + b;
