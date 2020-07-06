from svec.vector2d import Vector2d

from math import isclose, sqrt, sin, cos

import pytest


def test_eq():
    assert Vector2d(1, 2) == Vector2d(1, 2)
    assert not (Vector2d(1, 2) != Vector2d(1, 2))

    assert not (Vector2d(1, 2) == Vector2d(2, 1))
    assert Vector2d(1, 2) != Vector2d(2, 1)

    assert Vector2d(1, 1) == Vector2d(1, 1)
    assert Vector2d(0.99, 1) != Vector2d(0.98, 1)
    assert Vector2d(1, 1) != Vector2d(1, 2)
    assert Vector2d(1, 1) != Vector2d(2, 1)


def test_add():
    assert Vector2d(1, 2) + Vector2d(3, 4) == Vector2d(4, 6)
    assert Vector2d(0, 0) + Vector2d(19, 41) == Vector2d(19, 41)
    assert Vector2d(6, 8) + Vector2d(7, 3) == Vector2d(7, 3) + Vector2d(6, 8) == Vector2d(13, 11)


def test_sub():
    assert Vector2d(1, 2) - Vector2d(3, 4) != Vector2d(3, 4) - Vector2d(1, 2)
    assert Vector2d(5, 3) - Vector2d(11, 2) == Vector2d(-6, 1)


def test_mul():
    assert 3 * Vector2d(1, 3) == Vector2d(1, 3) * 3 == Vector2d(3, 9)
    assert 0 * Vector2d(4, 11) == Vector2d(4, 11) * 0 == Vector2d(0, 0)


def test_length():
    a = Vector2d(3, 4)
    b = Vector2d(1, 1)
    c = Vector2d(0, 0)
    d = Vector2d(9.5, 0)
    e = Vector2d(0, 6.8)
    assert isclose(a.length_sq(), 25)
    assert isclose(b.length_sq(), 2)
    assert isclose(c.length_sq(), 0)
    assert isclose(d.length_sq(), 9.5**2)
    assert isclose(e.length_sq(), 6.8**2)
    assert isclose(abs(a), 5)
    assert isclose(abs(b), sqrt(2))
    assert isclose(abs(c), 0)
    assert isclose(abs(d), 9.5)
    assert isclose(abs(e), 6.8)


def are_vecs_close(a, b):
    return abs(a - b) < 1e-9


def test_div():
    assert are_vecs_close(Vector2d(3, 4) / 2, Vector2d(1.5, 2))
    assert are_vecs_close(Vector2d(0, 11) / 6, Vector2d(0, 11/6))
    assert are_vecs_close(Vector2d(0, 0) / 7, Vector2d(0, 0))
    with pytest.raises(ZeroDivisionError):
        Vector2d(3, 5) / 0


def test_neg():
    assert -Vector2d(1, -5) == Vector2d(-1, 5)
    assert -Vector2d(2, 8) == Vector2d(-2, -8)
    assert -Vector2d(0, 0) == Vector2d(0, 0)


def test_coords():
    assert Vector2d(2.1, 5.4).coords() == (2.1, 5.4)


def test_repr_sanity():
    r = repr(Vector2d(15624, 37505))
    assert '15624' in r
    assert '37505' in r
    assert r.index('15624') < r.index('37505')


def test_dot():
    assert Vector2d(3, 1).dot(Vector2d(2, 5)) == 11
    assert Vector2d(0, 3).dot(Vector2d(31, -21)) == -63
    assert Vector2d(0, 1).dot(Vector2d(2, 0)) == 0
    assert Vector2d(0, 0).dot(Vector2d(4, 5)) == 0


def test_normalized():
    assert are_vecs_close(Vector2d(3, 4).normalized(), Vector2d(0.6, 0.8))
    assert are_vecs_close(Vector2d(4, -3).normalized(), Vector2d(0.8, -0.6))
    assert are_vecs_close(Vector2d(1, 0).normalized(), Vector2d(1, 0))
    phi = 83593
    assert are_vecs_close(Vector2d(sin(phi), cos(phi)).normalized(), Vector2d(sin(phi), cos(phi)))
    with pytest.raises(ZeroDivisionError):
        Vector2d(0, 0).normalized()
