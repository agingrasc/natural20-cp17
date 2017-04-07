class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other, self.z)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, int):
            return Vector(self.x - other, self.y - other, self.z)
        else:
            raise NotImplementedError

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def multiply(self, operand):
        return Vector(self.x * operand, self.y * operand)

    def to_pos(self):
        return self.x, self.y
