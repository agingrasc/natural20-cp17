from display import drawer
from display.action.interface import IDomainAction
from display.cache import ImagesCache
from util.geometry import Vector

DEFAULT_FLOOR_INDICATOR_IMAGE_PATH = 'resource/img/level_counter.png'
DEFAULT_FLOOR_INDICATOR_POS = Vector(135-108, 105-106)
DEFAULT_FLOOR_INDICATOR_SCALE = Vector(210, 210)
DEFAULT_TIME_TO_CLIMB_A_FLOOR = 2


floor_to_angle = {0: 89,
                  1: 75,
                  2: 60,
                  3: 35,
                  4: 10,
                  5: -10,
                  6: -35,
                  7: -60,
                  8: -75,
                  9: -89}


class FloorIndicatorAction(IDomainAction):
    def __init__(self, actual_floor, target_floor):
        super().__init__()
        self.angle = floor_to_angle[actual_floor]
        self.actual_floor = actual_floor
        self.target_floor = target_floor
        self.persistent_name = "floor-indicator"
        self.accumulated_time = 0

    def display(self, game_display, dt):
        dt /= 1000.0
        if self.finished:
            pass
        elif self.accumulated_time < DEFAULT_TIME_TO_CLIMB_A_FLOOR:
            self.accumulated_time += dt
            initial_angle = floor_to_angle[self.actual_floor]
            target_angle = floor_to_angle[self.actual_floor+1] if self.target_floor > self.actual_floor else floor_to_angle[self.actual_floor-1]
            delta_angle = target_angle - initial_angle
            self.angle += (delta_angle * dt) / DEFAULT_TIME_TO_CLIMB_A_FLOOR
        else:
            self.actual_floor = self.actual_floor + 1 if self.target_floor > self.actual_floor else self.actual_floor - 1
            self.angle = floor_to_angle[self.actual_floor]
            self.accumulated_time = 0
            if self.actual_floor == self.target_floor:
                self.finished = True
        return self.draw_image(game_display)

    def draw_image(self, game_display):
        image = ImagesCache().images['floor-indicator']
        pos = DEFAULT_FLOOR_INDICATOR_POS
        scale = DEFAULT_FLOOR_INDICATOR_SCALE
        return drawer.add_image(game_display, image, pos, scale, self.angle)
