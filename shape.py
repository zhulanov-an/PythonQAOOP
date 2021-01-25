class Shape():
    def __init__(self, name, area, angles, perimeter):
        self._name = name
        self._area = area
        self._angles = angles
        self._perimeter = perimeter

    def get_area(self):
        return self._area

    def add_area(self, other_figure):
        if not isinstance(other_figure, Shape):
            raise Exception("not a figure")
        return self.get_area() + other_figure.get_area()

    def get_angles(self):
        return self._angles

    def get_name(self):
        return self._name
