from display import drawer

DISPLAY_ANIMATION_TIME = 100


class Dialog:
    def __init__(self, game_display, text: str):
        self.idx = 0
        self.text = text
        self.game_display = game_display
        self.time_elapsed = 0

    def display(self, delta_t):
        self.time_elapsed += delta_t
        if self.time_elapsed < DISPLAY_ANIMATION_TIME:
            return drawer.display_dialog(self.game_display, self.text[:self.idx])
        elif self.idx < len(self.text):
            self.time_elapsed = 0
            self.idx += 1
            return drawer.display_dialog(self.game_display, self.text[:self.idx])
        else:
            return drawer.display_dialog(self.game_display, self.text[:self.idx])

