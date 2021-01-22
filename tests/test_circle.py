import pytest
from circle import Circle
from shape import Shape


def test_circle_angles_equals_zero():
    circle_1 = Circle(10)
    assert circle_1.get_angles() == 0


def test_circles_equals_area_after_add_area():
    circle_1 = Circle(1)
    circle_2 = Circle(2)
    assert circle_1.add_area(circle_2) == circle_2.add_area(circle_1)


@pytest.mark.parametrize("item", [object(), list(), set()])
def test_error_if_not_figure(item):
    circle_1 = Circle(1)
    with pytest.raises(Exception):
        circle_1.add_area(item)


def test_name_circle():
    circle_1 = Circle(1)
    assert circle_1.get_name() == "Circle"


def test_circle_is_instance_figure():
    assert isinstance(Circle(1), Shape)
