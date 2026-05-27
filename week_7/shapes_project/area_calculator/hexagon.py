from calculator import Shape
import math


class Hexagon(Shape):
    def __init__(self,side):
        self.side = side

        self.name = "Hexagon"

        area = (3 * math.sqrt(3) * side ** 2) / 2
        perimeter = 6 * side

        super().__init__(area,perimeter)    