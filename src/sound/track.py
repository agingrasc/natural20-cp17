import pygame

from util.singleton import Singleton


class BackgroundMusicTrack(metaclass=Singleton):
    def __init__(self):
        self.sound: pygame.mixer.SoundType = pygame.mixer.Sound("resource/music/Trame-classique-2m40s.wav")
        self.sound.play(-1)

    def stop(self):
        self.sound.stop()

    def play(self):
        self.sound.play()

    def change_track(self, track_path):
        self.sound.stop()
        self.sound = pygame.mixer.Sound(track_path)
        self.sound.play(-1)
