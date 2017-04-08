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
        self.initial_angle = floor_to_angle[actual_floor]
        self.target_angle = floor_to_angle[target_floor]
        self.angle = self.initial_angle
        self.persistent_name = "floor-indicator"
        self.accumulated_time = 0

    def display(self, game_display, dt):
        dt /= 1000.0
        if self.finished:
            pass
        elif self.accumulated_time < DEFAULT_TIME_TO_CLIMB_A_FLOOR:
            self.accumulated_time += dt
            delta_angle = self.target_angle - self.initial_angle
            #self.angle = self.initial_angle + delta_angle * self.accumulated_time / DEFAULT_TIME_TO_CLIMB_A_FLOOR
            self.angle = self.initial_angle + easing(self.accumulated_time, 0, delta_angle, DEFAULT_TIME_TO_CLIMB_A_FLOOR)
        else:
            self.finished = True
        return self.draw_image(game_display)

    def draw_image(self, game_display):
        image = ImagesCache().images['floor-indicator']
        pos = DEFAULT_FLOOR_INDICATOR_POS
        scale = DEFAULT_FLOOR_INDICATOR_SCALE
        return drawer.add_image(game_display, image, pos, scale, self.angle)
#elapsed, start, end, total
def easing(t, b, c, d):
    t /= d
    return -c * t * (t - 2) + b;
