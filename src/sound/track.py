import pygame

from sound.channel import ChannelManager
from util.singleton import Singleton

TRACK_VOLUME = 0.2


class BackgroundMusicTrack(metaclass=Singleton):
    def __init__(self):
        #self.sound: pygame.mixer.SoundType = pygame.mixer.Sound("resource/music/Trame-classique-2m40s.wav")
        self.sound = pygame.mixer.Sound("resource/music/Trame-classique-2m40s.wav")
        self.sound.set_volume(TRACK_VOLUME)
        self.sound.play(-1)

    def stop(self):
        ChannelManager().stop()

    def play(self):
        ChannelManager().play('music', self.sound, TRACK_VOLUME, -1)

    def change_track(self, track_path):
        self.stop()
        self.sound = pygame.mixer.Sound(track_path)
        self.play()
