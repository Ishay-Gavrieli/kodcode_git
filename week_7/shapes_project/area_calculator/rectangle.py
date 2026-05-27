from calculator import Shape

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.name = "Rectangle"

        calculator_area = width * height
        calculator_perimeter = 2 * (width + height)

        super().__init__(calculator_area,calculator_perimeter)

