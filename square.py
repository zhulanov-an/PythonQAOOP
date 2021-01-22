from shape import Shape


class Square(Shape):
    def __init__(self, area, perimeter, name="Square"):
        super().__init__(name=name, area=area, angles=4, perimeter=perimeter)
