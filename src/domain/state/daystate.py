from domain.state.state import State

class DayState(State):
    def __init__(self, day):
        super().__init__(self.introduce_next_client)
        self.day = day

    def introduce_next_client(self, dt, action):
        self.current_client = self.day.pop_clients()
        self.change_substate_and_exec(self.move_client_to_elevator)

    def move_client_to_elevator(self, dt, actions):
        pass

    def exec(self, dt=None, actions=None):
        self.current_substate(dt, actions)

    def is_finish(self):
        pass