from shape_manager import ShapeManager
from square import Square
from circle import Circle
from rectangle import Rectangle

def main():
    manager = ShapeManager()
    
    def get_next_id():
        existing_shapes = manager.get_all_shapes()
        if not existing_shapes:
            return 1
        return max(shape.id for shape in existing_shapes) + 1

    while True:
        print("--- Shape Management Menu ---")
        print("1. Add shape")
        print("2. Show all shapes")
        print("3. Update shape")
        print("4. Delete shape")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Select shape type:")
            print("1. Square")
            print("2. Rectangle")
            print("3. Circle")
            type_choice = input("Enter choice: ")
            
            shape_id = get_next_id()
            
            if type_choice == "1":
                try:
                    side = float(input("Enter side length: "))
                    new_shape = Square(shape_id, side)
                    manager.create_shape(new_shape)
                    print(f"Square added successfully with ID: {shape_id}")
                except ValueError:
                    print("Invalid numeric input.")
                    
            elif type_choice == "2":
                try:
                    width = float(input("Enter width: "))
                    height = float(input("Enter height: "))
                    new_shape = Rectangle(shape_id, width, height)
                    manager.create_shape(new_shape)
                    print(f"Rectangle added successfully with ID: {shape_id}")
                except ValueError:
                    print("Invalid numeric input.")
                    
            elif type_choice == "3":
                try:
                    radius = float(input("Enter radius: "))
                    new_shape = Circle(shape_id, radius)
                    manager.create_shape(new_shape)
                    print(f"Circle added successfully with ID: {shape_id}")
                except ValueError:
                    print("Invalid numeric input.")
            else:
                print("Invalid shape selection.")

        elif choice == "2":
            shapes = manager.get_all_shapes()
            if not shapes:
                print("No shapes found.")
            for shape in shapes:
                print(f"ID: {shape.id}")
                print(f"Type: {shape.shape_type.capitalize()}")
                
                if shape.shape_type == "square":
                    print(f"Side: {shape.side}")
                elif shape.shape_type == "circle":
                    print(f"Radius: {shape.radius}")
                elif shape.shape_type == "rectangle":
                    print(f"Width: {shape.width}, Height: {shape.height}")
                    
                print(f"Area: {shape.get_area():.2f}")
                print(f"Perimeter: {shape.get_perimeter():.2f}")

        elif choice == "3":
            try:
                shape_id = int(input("Enter shape ID to update: "))
                target_shape = None
                for s in manager.get_all_shapes():
                    if s.id == shape_id:
                        target_shape = s
                        break
                
                if not target_shape:
                    print("Shape ID not found.")
                    continue
                
                new_data = {}
                if target_shape.shape_type == "square":
                    new_data["side"] = float(input("Enter new side: "))
                elif target_shape.shape_type == "circle":
                    new_data["radius"] = float(input("Enter new radius: "))
                elif target_shape.shape_type == "rectangle":
                    new_data["width"] = float(input("Enter new width: "))
                    new_data["height"] = float(input("Enter new height: "))
                
                if manager.update_shape(shape_id, new_data):
                    print("Shape updated successfully.")
                else:
                    print("Update failed.")
            except ValueError:
                print("Invalid input value.")

        elif choice == "4":
            try:
                shape_id = int(input("Enter shape ID to delete: "))
                if manager.delete_shape(shape_id):
                    print("Shape deleted successfully.")
                else:
                    print("Shape ID not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()