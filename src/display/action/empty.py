class EmptyAction():
    def __init__(self):
        pass

    def display(self, *args):
        def nop():
            pass
        return nop
