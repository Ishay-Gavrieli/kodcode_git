from rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self, base, height,side_a,side_b,side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        area = (base * height) / 2
        perimeter = side_a + side_b + side_c

        super().__init__(area,perimeter)
        self.name = "Triangle"