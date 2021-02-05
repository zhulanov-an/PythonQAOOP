from shape import Shape


class Square(Shape):
    def __new__(cls, *args, **kwargs):
        print("__new__", cls, args, kwargs)
        return super(Square, cls).__new__(cls)

    def __init__(self, area, perimeter):
        print("__init__", self, area, perimeter)
        super().__init__(name="Square", area=area, angles=4, perimeter=perimeter)

    def __call__(self, *args, **kwargs):
        print(type(self), "__call__", args, kwargs)
        super(Square, self).__call__(self, *args, **kwargs)
