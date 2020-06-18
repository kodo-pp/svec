from svec.common import ScalarType

from typing import Tuple


class Vector2d:
    __slots__ = ('x', 'y')

    def __init__(self, x: ScalarType, y: ScalarType):
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

    def __neg__(self) -> 'Vector2d':
        return self * (-1)

    def coords(self) -> Tuple[ScalarType, ScalarType]:
        return self.x, self.y

    def __repr__(self) -> str:
        x, y = self.coords()
        return f'Vector2d({x}, {y})'

    def __eq__(self, other: 'Vector2d') -> bool:
        return (self.x, self.y) == (other.x, other.y)
