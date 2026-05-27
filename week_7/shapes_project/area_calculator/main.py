from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon


def show_menu():
    print("=" * 30)
    print("   GEOMETRIC SHAPE CALCULATOR   ")
    print("=" * 30)
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")
    print("5. Hexagon")
    print("0. Exit")
    print("=" * 30)


def get_positive_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value <= 0:
                print("Invalid input: Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input: Please enter a valid number.")



def main():
    while True:
        show_menu()
        choice = input("Enter your choice:")
        
        if choice == "1":
            width = get_positive_float("Enter the width: ")
            height = get_positive_float("Enter the height: ")
            
            rectangle = Rectangle(width, height)
            print(f"Created Shape: {rectangle.name}, Area: {rectangle.area:.1f}, Perimeter: {rectangle.perimeter:.1f}")
            
        elif choice == "2":
            side = get_positive_float("Enter the side length: ")
            
            square = Square(side)
            print(f"Created Shape: {square.name}, Area: {square.area:.1f}, Perimeter: {square.perimeter:.1f}")
            
        elif choice == "3":
            s1 = get_positive_float("Enter side 1 length:")
            s2 = get_positive_float("Enter side 2 length:")
            s3 = get_positive_float("Enter side 3 length:")
            base = get_positive_float("Enter the base:")
            height = get_positive_float("Enter the height:")
            
            triangle = Triangle(s1, s2, s3, base, height)
            print(f"Created Shape: {triangle.name}, Area: {triangle.area:.1f}, Perimeter: {triangle.perimeter:.1f}")
            
        elif choice == "4":
            radius = get_positive_float("Enter the radius:")
            
            circle = Circle(radius)
            print(f"Created Shape: {circle.name}, Area: {circle.area:.1f}, Perimeter: {circle.perimeter:.1f}")
            
        elif choice == "5":
            side = get_positive_float("Enter the side length:")
            
            hexagon = Hexagon(side)
            print(f"Created Shape: {hexagon.name}, Area: {hexagon.area:.1f}, Perimeter: {hexagon.perimeter:.1f}")
            
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
    

