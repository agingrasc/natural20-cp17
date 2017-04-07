from display import drawer

DISPLAY_ANIMATION_TIME = 100


class Dialog:
    def __init__(self, text: str):
        self.idx = 0
        self.text = text
        self.time_elapsed = 0
        self.finished = False

    def display(self, game_display, delta_t):
        self.time_elapsed += delta_t
        if self.time_elapsed < DISPLAY_ANIMATION_TIME:
            return drawer.display_dialog(game_display, self.text[:self.idx])
        elif self.idx < len(self.text):
            self.time_elapsed = 0
            self.idx += 1
            return drawer.display_dialog(game_display, self.text[:self.idx])
        else:
            self.finished = True
            return drawer.display_dialog(game_display, self.text[:self.idx])

