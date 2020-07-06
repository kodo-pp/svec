from svec.common import ScalarType

from math import sqrt
from typing import Tuple


class Vector2d:
    __slots__ = ('x', 'y')

    def __init__(self, x: ScalarType, y: ScalarType) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: ScalarType) -> 'Vector2d':
        return Vector2d(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: ScalarType) -> 'Vector2d':
        return self * scalar

    def __truediv__(self, scalar: ScalarType) -> 'Vector2d':
        return self * (1.0 / scalar)

    def __neg__(self) -> 'Vector2d':
        return self * (-1)

    def coords(self) -> Tuple[ScalarType, ScalarType]:
        return self.x, self.y

    def __repr__(self) -> str:
        x, y = self.coords()
        return f'Vector2d({x}, {y})'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector2d) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        return hash(('vector2d', self.coords())) + 395

    def dot(self, other: 'Vector2d') -> float:
        return self.x * other.x + self.y * other.y

    def length_sq(self) -> float:
        return self.dot(self)

    def __abs__(self) -> float:
        return sqrt(self.length_sq())

    def normalized(self) -> 'Vector2d':
        length = abs(self)
        if length == 0.0:
            raise ZeroDivisionError('Cannot normalize the zero vector')
        return self / length
