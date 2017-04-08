from display import drawer
from display.action.interface import IDomainAction
from display.cache import ImagesCache
from util.geometry import Vector

DEFAULT_POSITION = Vector(275, 0)
OPEN_WIDTH = 125
CLOSED_WIDTH = 520
DEFAULT_HEIGHT = 600


class ElevatorGateOpenAction(IDomainAction):
    def __init__(self):
        self.coordinates = DEFAULT_POSITION
        self.size = Vector(CLOSED_WIDTH, DEFAULT_HEIGHT)
        self.accumulated_time = 0

    def display(self, game_display, dt):
        self.accumulated_time += dt
        image = ImagesCache().images['elevator-gate']
        return drawer.add_image(game_display, image, self.coordinates, self.size)



class ElevatorGateCloseAction(IDomainAction):
    def __init__(self):
        self.coorinates = DEFAULT_POSITION
        self.size = Vector(OPEN_WIDTH, DEFAULT_HEIGHT)

    def display(self, game_display, dt):
        return None