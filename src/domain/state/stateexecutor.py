from domain.state.daystate import DayState

class StateExecutor:
    def __init__(self):
        self.day_nb = 1
        self.current_state = DayState(self.day_nb)

    def exec(self, dt, action):
        if not self.current_state.is_finish():
            self.day_nb += 1
            self.current_state = DayState(self.day_nb)
        return self.current_state.exec(dt, action)