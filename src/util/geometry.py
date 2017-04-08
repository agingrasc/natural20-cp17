import math


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
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def multiply(self, operand):
        return Vector(int(self.x * operand), int(self.y * operand))

    def to_pos(self):
        return self.x, self.y

    def rotate(self, angle):
        theta = math.radians(angle)
        norm = math.sqrt(self.x**2 + self.y**2)
        x = math.cos(theta) * norm
        y = math.sin(theta) * norm
        return Vector(int(abs(x)), int(abs(y)))
