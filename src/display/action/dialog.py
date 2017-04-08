import pygame

from display import drawer
from display.action.interface import IDomainAction
from sound.channel import ChannelManager

DISPLAY_ANIMATION_TIME = 110
DIALOG_SOUND_VOLUME = 0.4


class Dialog(IDomainAction):
    def __init__(self, name: str, text: str):
        super().__init__()
        self.idx = 0
        self.name = name
        self.text = text
        self.time_elapsed = 0
        self.sound = None

    def display(self, game_display, delta_t):
        self.time_elapsed += delta_t
        if self.sound is None:
            self.sound = pygame.mixer.Sound("resource/sounds/Typing-Machine-3s.wav")
            ChannelManager().play('effect', self.sound, DIALOG_SOUND_VOLUME, -1)

        if self.finished:
            ChannelManager().stop('effect')
            return drawer.display_dialog(game_display, self.name, self.text)
        elif self.time_elapsed < DISPLAY_ANIMATION_TIME:
            return drawer.display_dialog(game_display, self.name, self.text[:self.idx])
        elif self.idx < len(self.text):
            self.time_elapsed = 0
            self.idx += 1
            return drawer.display_dialog(game_display, self.name, self.text[:self.idx])
        else:
            self.finished = True
            return drawer.display_dialog(game_display, self.name, self.text[:self.idx])

