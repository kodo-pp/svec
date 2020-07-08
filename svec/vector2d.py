"""Module dedicated to 2D vectors"""

from svec.common import ScalarType

from math import sqrt
from typing import Tuple


class Vector2d:
    """2D vector"""
    __slots__ = ('x', 'y')

    def __init__(self, x: ScalarType, y: ScalarType) -> None:
        """Construct a vector given its coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2d') -> 'Vector2d':
        """Add two vectors."""
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2d') -> 'Vector2d':
        """Subtract `other` from `self`."""
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: ScalarType) -> 'Vector2d':
        """Multiply this vector by a scalar and return the result."""
        return Vector2d(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: ScalarType) -> 'Vector2d':
        return self * scalar

    def __truediv__(self, scalar: ScalarType) -> 'Vector2d':
        """Divide this vector by a non-zero scalar and return the result.

        Exceptions:
            ZeroDivisionError -- raised by the floating point division operation
                                 if `scalar` is zero.
        """
        return self * (1.0 / scalar)

    def __neg__(self) -> 'Vector2d':
        """Return the additive inverse of `self`."""
        return self * (-1)

    def coords(self) -> Tuple[ScalarType, ScalarType]:
        """Return the coordinates of this vector as a pair of scalars."""
        return self.x, self.y

    def __repr__(self) -> str:
        x, y = self.coords()
        return f'Vector2d({x}, {y})'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector2d) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        return hash(('vector2d', self.coords())) + 395

    def dot(self, other: 'Vector2d') -> float:
        """Compute the dot product of `self` and `other`.

        If `self == Vector2d(x1, y1)` and `other == Vector2d(x2, y2)`,
        then the dot product of `self` and `other` is `x1 * x2 + y1 * y2`.
        """
        return self.x * other.x + self.y * other.y

    def length_sq(self) -> float:
        """Return the squared length of this vector."""
        return self.dot(self)

    def __abs__(self) -> float:
        """Return the length (a.k.a. norm) of this vector

        If it is only necessary to compare the lengths of several vectors,
        consider calling `length_sq` instead. `length_sq` is faster and it
        might be more precise because it does not involve computing the square
        root of the length.
        """
        return sqrt(self.length_sq())

    def normalized(self) -> 'Vector2d':
        """Return the vector with the same direction but having the length 1.

        This vector must have a non-zero length for this operation to be possible.

        Exceptions:
            ZeroDivisionError -- raised if this vector is the zero vector"""
        length = abs(self)
        if length == 0.0:
            raise ZeroDivisionError('Cannot normalize the zero vector')
        return self / length
