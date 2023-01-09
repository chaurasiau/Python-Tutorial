# https://realpython.com/python-super/

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def justlikethat(self):
        print("Just like that!!")


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


square = Square(4)
print(f"Area of a square is {square.area()}")

cube = Cube(3)
print(f"Surface Area of a cube is {cube.surface_area()}")
print(f"Volume of a cube is {cube.volume()}")

cube.justlikethat()
