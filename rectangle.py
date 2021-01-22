from square import Square


class Rectangle(Square):
    def __init__(self, area, perimeter):
        super().__init__(area=area, perimeter=perimeter, name="Rectangle")
