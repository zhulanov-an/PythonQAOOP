from shape import Shape


class Square(Shape):
    def __init__(self, area, perimeter):
        super().__init__(name="Square", area=area, angles=4, perimeter=perimeter)
