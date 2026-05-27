
class Shape:
    def __init__(self,area,perimeter):
        self.area = area
        self.perimeter = perimeter
        
    def get_area(self):
        return f"the area of the shape is {self.area}"
    
    def get_perimeter(self):
        return f"the perimeter of the shape is {self.perimeter}"
    
    def __str__(self):
        return f"Shape (Area: {self.area}, Perimeter: {self.perimeter})"
    
    def __repr__(self):
        return self.__str__() 






