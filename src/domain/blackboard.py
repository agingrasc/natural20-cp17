from util.singleton import Singleton


class Blackboard(metaclass=Singleton):
    def __init__(self):
        self.stage = 1
        self.tips = 0.0
        self.flags = []

    def add_tips(self, value: int):
        new_value = value + self.tips
        self.tips = max([new_value, 0])
