class EmptyAction():
    def __init__(self):
        self.finished = False

    def display(self, *args):
        def nop():
            pass
        return nop
