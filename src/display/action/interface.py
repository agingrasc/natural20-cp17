import abc


class IDomainAction(metaclass=abc.ABCMeta):

    def __init__(self):
        self.finished = False

    @abc.abstractmethod
    def display(self, game_display, dt):
        def nop():
            pass
        return nop
