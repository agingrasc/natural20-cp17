from display import drawer
from display.action.interface import IDomainAction

DISPLAY_ANIMATION_TIME = 200


class Dialog(IDomainAction):
    def __init__(self, text: str):
        super().__init__()
        self.idx = 0
        self.text = text
        self.time_elapsed = 0

    def display(self, game_display, delta_t):
        self.time_elapsed += delta_t
        if self.finished:
            return drawer.display_dialog(game_display, self.text)
        elif self.time_elapsed < DISPLAY_ANIMATION_TIME:
            return drawer.display_dialog(game_display, self.text[:self.idx])
        elif self.idx < len(self.text):
            self.time_elapsed = 0
            self.idx += 1
            return drawer.display_dialog(game_display, self.text[:self.idx])
        else:
            self.finished = True
            return drawer.display_dialog(game_display, self.text[:self.idx])

