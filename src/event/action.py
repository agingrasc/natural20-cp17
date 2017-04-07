class Action:
    def __init__(self):
        self.data = {}


class UserKeyAction(Action):
    def __init__(self):
        super().__init__()
        self.data = {'spacebar': True }


class FloorSelected(Action):
    def __init__(self, floor):
        super().__init__()
        self.data = {'floor': floor}
        print("Floor {} selected!".format(floor))
