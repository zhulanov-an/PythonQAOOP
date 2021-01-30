import pytest
from triangle import Triangle
from square import Square
from shape import Shape


def test_triangle_angles_equals_three():
    triangle = Triangle(10, 6)
    assert triangle.angles == 3


def test_triangles_equals_area_after_add_area():
    triangle_1 = Triangle(4, 2)
    triangle_2 = Triangle(6, 2)
    assert triangle_1.add_area(triangle_2) == triangle_2.add_area(triangle_1)


def test_error_if_not_figure():
    triangle = Triangle(4, 2)
    with pytest.raises(Exception):
        triangle.add_area(object())


def test_name_triangle():
    triangle = Triangle(4, 2)
    assert triangle.name == "Triangle"


def test_triangle_is_instance_figure():
    assert isinstance(Triangle(4, 2), Shape)
