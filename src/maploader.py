import pytmx

from pytmx.util_pygame import load_pygame

class MapLoader:
    def __init__(self):
        self.tiled_map = load_pygame('ressource/map/test.tmx')
