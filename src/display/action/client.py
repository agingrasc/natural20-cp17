from display import drawer
from display.action.interface import IDomainAction
from display.cache import ImagesCache
from util.geometry import Vector

POS_CHARACTER = Vector(418,770)


class ClientAction(IDomainAction):
    #def __init__(self, client_name: str):
    def __init__(self, client_name):
        super().__init__()
        self.client_name = client_name
        self.persistent_name = 'client'

    def display(self, game_display, dt):
        def nop():
            pass
        if self.client_name is None:
            return nop
        image = ImagesCache().images[self.client_name]
        height = image.get_rect().size[1]
        return drawer.add_image(game_display, image, POS_CHARACTER- Vector(0, height))


class NoClientAction(ClientAction):
    def __init__(self):
        super().__init__(None)
