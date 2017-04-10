from display import drawer
from display.action.interface import IDomainAction

DISPLAY_ANIMATION_TIME = 40
DIALOG_SOUND_VOLUME = 0.8


class Dialog(IDomainAction):
    #def __init__(self, name: str, text: str):
    def __init__(self, name, text):
        super().__init__()
        self.idx = 0
        self.name = name
        self.text = text
        self.time_elapsed = 0

    def display(self, game_display, delta_t):
        self.time_elapsed += delta_t
        self.start_sound_effect("resource/sounds/Typing-Machine-3s.wav", DIALOG_SOUND_VOLUME)

        if self.finished:
            self.stop_sound_effect()
            return drawer.display_dialog(game_display, self.name, self.text)
        elif self.time_elapsed < DISPLAY_ANIMATION_TIME:
            return drawer.display_dialog(game_display, self.name, self.text[:self.idx])
        elif self.idx < len(self.text):
            self.time_elapsed = 0
            self.idx += 1
            return drawer.display_dialog(game_display, self.name, self.text[:self.idx])
        else:
            self.stop_sound_effect()
            self.finished = True
            return drawer.display_dialog(game_display, self.name, self.text[:self.idx])
