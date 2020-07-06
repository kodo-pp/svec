from svec.point2d import Point2d
from svec.vector2d import Vector2d


def test_eq():
    assert Point2d(Vector2d(2, 2)) == Point2d(Vector2d(2, 2))
    assert Point2d(Vector2d(1, 2)) != Point2d(Vector2d(2, 1))
    assert Point2d(Vector2d(1, 1)) != Point2d(Vector2d(2, 1))
    assert Point2d(Vector2d(1, 1)) != Point2d(Vector2d(1, 2))
    assert Point2d(Vector2d(4, 5)) != Point2d(Vector2d(2, -9))


def test_add():
    assert Point2d(Vector2d(2, -5)) + Vector2d(1, 3) == Point2d(Vector2d(3, -2))
    assert Point2d(Vector2d(0, 3)) + Vector2d(2, 2) == Point2d(Vector2d(2, 5))


def test_sub_vector():
    assert Point2d(Vector2d(-3, -7)) - Vector2d(3, 3) == Point2d(Vector2d(-6, -10))
    assert Point2d(Vector2d(0, 0)) - Vector2d(1, 2) == Point2d(Vector2d(-1, -2))


def test_sub_point():
    assert Point2d(Vector2d(3, 5)) - Point2d(Vector2d(1, -2)) == Vector2d(2, 7)
    assert Point2d(Vector2d(2, 8)) - Point2d(Vector2d(2, 88)) == Vector2d(0, -80)


def test_coords():
    assert Point2d(Vector2d(14, -51)).coords() == (14, -51)
    assert Point2d(Vector2d(1.3, 9.85)).coords() == (1.3, 9.85)


def test_ints():
    assert Point2d(Vector2d(14, -51)).ints() == (14, -51)
    assert Point2d(Vector2d(1.3, 9.85)).ints() == (1, 9)


def test_repr_sanity():
    r = repr(Point2d(Vector2d(15624, 37505)))
    assert '15624' in r
    assert '37505' in r
    assert r.index('15624') < r.index('37505')
