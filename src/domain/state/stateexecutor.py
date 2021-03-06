from domain.day import Day
from domain.state.daystate import DayState


class StateExecutor:
    def __init__(self):
        self.day_nb = 1
        self.current_state = DayState(Day(self.day_nb))
        self.current_state

    def exec(self, dt, actions):
        if self.current_state.is_finish():
            self.day_nb += 1
            self.current_state = DayState(Day(self.day_nb))
        return self.current_state.exec(dt, actions)