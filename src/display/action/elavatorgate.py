from display import drawer
from display.action.interface import IDomainAction
from display.cache import ImagesCache
from util.animation import easing
from util.geometry import Vector

DEFAULT_POSITION = Vector(275, 0)
OPEN_WIDTH = 125
CLOSED_WIDTH = 520
DEFAULT_HEIGHT = 600

DEFAULT_TIME_DOOR = 5


class ElevatorGateOpenAction(IDomainAction):
    def __init__(self):
        super().__init__()
        self.coordinates = DEFAULT_POSITION
        self.size = Vector(CLOSED_WIDTH, DEFAULT_HEIGHT)
        self.accumulated_time = 0
        self.persistent_name = 'elevator-gate'

    def display(self, game_display, dt):
        self.accumulated_time += (dt/1000)
        image = ImagesCache().images['elevator-gate']
        self.start_sound_effect("resource/sounds/Porte-ouvre-ferme-2s.wav")
        if self.accumulated_time < DEFAULT_TIME_DOOR:
            delta_x = OPEN_WIDTH - CLOSED_WIDTH
            width = CLOSED_WIDTH + easing(self.accumulated_time, 0, delta_x, DEFAULT_TIME_DOOR)
            self.size.x = int(width)
        else:
            self.stop_sound_effect()
            self.finished = True
        return drawer.add_image(game_display, image, self.coordinates, self.size)


class ElevatorGateCloseAction(IDomainAction):
    def __init__(self):
        super().__init__()
        self.coordinates = DEFAULT_POSITION
        self.size = Vector(OPEN_WIDTH, DEFAULT_HEIGHT)
        self.accumulated_time = 0
        self.persistent_name = 'elevator-gate'

    def display(self, game_display, dt):
        self.accumulated_time += (dt/1000)
        image = ImagesCache().images['elevator-gate']
        self.start_sound_effect("resource/sounds/Porte-ouvre-ferme-2s.wav")
        if self.accumulated_time < DEFAULT_TIME_DOOR:
            delta_x = CLOSED_WIDTH - OPEN_WIDTH
            width = OPEN_WIDTH + easing(self.accumulated_time, 0, delta_x, DEFAULT_TIME_DOOR)
            self.size.x = int(width)
        else:
            self.stop_sound_effect()
            self.finished = True
        return drawer.add_image(game_display, image, self.coordinates, self.size)
