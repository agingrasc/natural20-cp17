from util.singleton import Singleton


class BlackBox(metaclass=Singleton):
    def __init__(self):
        self.stage = 1
        self.tips = 0.0
        self.flags = []