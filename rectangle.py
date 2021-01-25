from shape import Shape


class Rectangle(Shape):
    def __init__(self, area, perimeter):
        super().__init__(name="Rectangle", area=area, angles=4, perimeter=perimeter)
