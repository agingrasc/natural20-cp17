import abc

class State(abc.ABC):

    def __init__(self, init_substate):
        self.next_substate = init_substate
    @abc.abstractmethod
    def exec(self, dt, actions):
        pass

    @abc.abstractmethod
    def is_finish(self):
        pass

    def change_substate_and_exec(self, next_substate, dt=None, actions=None):
        self.next_substate = next_substate
        self.next_substate(dt, actions)