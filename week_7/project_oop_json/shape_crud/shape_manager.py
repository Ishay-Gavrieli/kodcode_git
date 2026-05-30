import json
import os
from square import Square
from circle import Circle
from rectangle import Rectangle

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.filename = "shapes.json"
        self.load_from_json()

    def create_shape(self, shape):
        self.shapes.append(shape)
        self.save_to_json()

    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:
            if shape.id == shape_id:
                if shape.shape_type == "square" and "side" in new_data:
                    shape.side = new_data["side"]
                elif shape.shape_type == "circle" and "radius" in new_data:
                    shape.radius = new_data["radius"]
                elif shape.shape_type == "rectangle":
                    if "width" in new_data:
                        shape.width = new_data["width"]
                    if "height" in new_data:
                        shape.height = new_data["height"]
                self.save_to_json()
                return True
        return False

    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                self.save_to_json()
                return True
        return False

    def save_to_json(self):
        dict_list = [shape.to_dict() for shape in self.shapes]
        with open(self.filename, 'w') as f:
            json.dump(dict_list, f, indent=4)

    def load_from_json(self):
        if not os.path.exists(self.filename):
            self.shapes = []
            return

        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.shapes = []
                for item in data:
                    s_id = item.get("id")
                    s_type = item.get("type")
                    
                    if s_type == "square":
                        self.shapes.append(Square(s_id, item.get("side")))
                    elif s_type == "circle":
                        self.shapes.append(Circle(s_id, item.get("radius")))
                    elif s_type == "rectangle":
                        self.shapes.append(Rectangle(s_id, item.get("width"), item.get("height")))
        except (json.JSONDecodeError, FileNotFoundError):
            self.shapes = []