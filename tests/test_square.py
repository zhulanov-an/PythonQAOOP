import pytest
from triangle import Triangle
from square import Square
from shape import Shape


def test_square_angles_equals_four():
    rectangle = Square(10, 6)
    assert rectangle.angles == 4


def test_squares_equals_area_after_add_area():
    square_1 = Square(4, 2)
    triangle_2 = Triangle(6, 2)
    assert square_1.add_area(triangle_2) == triangle_2.add_area(square_1)


def test_error_if_not_figure():
    rectangle = Square(4, 2)
    with pytest.raises(Exception):
        rectangle.add_area(object())


def test_name_square():
    rectangle = Square(4, 2)
    assert rectangle.name == "Square"


def test_square_is_instance_figure():
    assert isinstance(Square(4, 2), Shape)
