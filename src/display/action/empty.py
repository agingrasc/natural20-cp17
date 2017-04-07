from display.action.interface import IDomainAction


class EmptyAction(IDomainAction):
    def __init__(self):
        super().__init__()

    def display(self, *args):
        def nop():
            pass
        return nop
