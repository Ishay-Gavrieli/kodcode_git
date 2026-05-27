from calculator import Shape
import math

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        self.name = "Circle"

        area = math.pi * radius ** 2
        perimeter = 2 * math.pi * radius

        super().__init__(area,perimeter)