import abc

import pygame

from sound.channel import ChannelManager


class IDomainAction(metaclass=abc.ABCMeta):

    def __init__(self):
        self.sound = None
        self.sound_finished = False
        self.finished = False
        self.persistent_name = ""

    @abc.abstractmethod
    def display(self, game_display, dt):
        def nop():
            pass
        return nop

    def stop_sound_effect(self):
        if self.sound:
            self.sound = None
            self.sound_finished = True
            ChannelManager().stop('effect')

    def start_sound_effect(self, sound_path, sound_level=0.4):
        if self.sound is None and not self.sound_finished:
            self.sound = pygame.mixer.Sound(sound_path)
            ChannelManager().play('effect', self.sound, sound_level, -1)
