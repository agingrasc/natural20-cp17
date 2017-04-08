from typing import Dict

import pygame

from util.singleton import Singleton


class ChannelManager(metaclass=Singleton):
    def __init__(self):
        self.channels: Dict[str, pygame.mixer.ChannelType] = {'music': pygame.mixer.Channel(0),
                         'effect': pygame.mixer.Channel(1),
                         'extra': pygame.mixer.Channel(2)}

    def play(self, channel: str, Sound: pygame.mixer.SoundType, volume: float, loops=0):
        self.channels[channel].play(Sound, loops)
        self.channels[channel].set_volume(volume)

    def stop(self, channel):
        self.channels[channel].stop()
