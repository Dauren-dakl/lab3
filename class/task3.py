#3
class Shape:
    def __init__(self):
        pass 
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 10)
print("Area:", rectangle.compute_area())  