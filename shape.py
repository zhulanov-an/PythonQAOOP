class Shape:
    def __init__(self, name, area, angles, perimeter):
        print("__init__", self, name, area, angles, perimeter)
        self.__name = name
        self.__area = area
        self.__angles = angles
        self.__perimeter = perimeter

    def __new__(cls, *args, **kwargs):
        print("__new__", cls, args, kwargs)
        return super(Shape, cls).__new__(cls)
    
    def __call__(self, *args, **kwargs):
        print(type(self),"__call__", self, args, kwargs)

    @property
    def area(self):
        return self.__area

    def add_area(self, other_figure):
        if not isinstance(other_figure, Shape):
            raise Exception("not a figure")
        return self.area + other_figure.area

    @property
    def angles(self):
        return self.__angles

    @property
    def name(self):
        return self.__name
