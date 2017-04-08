from display.action.interface import IDomainAction

floor_to_angle = {0: 89,
                  1: 75,
                  2: 60,
                  3: 35,
                  4: 10,
                  5: -10,
                  6: -35,
                  7: -60,
                  8: -75,
                  9: -89}


class LevelIndicator(IDomainAction):
    def __init__(self, floor):
        super().__init__()
        self.angle = floor_to_angle[floor]