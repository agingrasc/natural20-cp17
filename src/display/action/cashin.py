from display.action.interface import IDomainAction


class CashInAction(IDomainAction):
    def __init__(self):
        super().__init__()
        self.accumulated_time = 0

    def display(self, game_display, dt):
        self.accumulated_time += (dt/1000)
        self.start_sound_effect("resource/sounds/Cashier-2s.wav")

        if self.accumulated_time > 2:
            self.stop_sound_effect()
            self.finished = True

        def nop():
            pass
        return nop