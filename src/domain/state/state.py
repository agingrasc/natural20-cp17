import abc

from display.action.empty import EmptyAction
from display.action.interface import IDomainAction


class State(abc.ABC):

    def __init__(self, init_substate):
        self.next_substate = init_substate

    def exec(self, dt=None, actions=[]):
        res = self.next_substate(dt, actions)
        if res is None:
            return []
        elif isinstance(res, IDomainAction):
            return [res]
        else:
            return res

    @abc.abstractmethod
    def is_finish(self):
        pass

    def change_substate_and_exec(self, next_substate, dt=None, actions=[]):
        self.next_substate = next_substate
        self.next_substate(dt, actions)

    def change_substate(self, next_substate):
        self.next_substate = next_substate