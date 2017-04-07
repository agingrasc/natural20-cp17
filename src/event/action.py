class Action:
    def __init__(self):
        self.data = {}


class FloorSelected(Action):
    def __init__(self, floor):
        super().__init__()
        self.data = {'floor': floor}
        print("Floor {} selected!".format(floor))
