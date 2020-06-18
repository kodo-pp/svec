from svec.common import ScalarType
from svec.vector2d import Vector2d

from typing import Tuple, overload


class Point2d:
    __slots__ = ('vec',)

    def __init__(self, vec: Vector2d):
        self.vec = vec

    def __add__(self, other: 'Vector2d') -> 'Point2d':
        return Point2d(self.vec + other)

    @overload
    def __sub__(self, other: 'Vector2d') -> 'Point2d':
        ...

    @overload
    def __sub__(self, other: 'Point2d') -> 'Vector2d':
        ...

    def __sub__(self, other):
        if isinstance(other, Vector2d):
            return self + (-other)
        return other.vec - self.vec

    def coords(self) -> Tuple[ScalarType, ScalarType]:
        return self.vec.coords()

    def ints(self) -> Tuple[int, int]:
        x, y = self.coords()
        return int(x), int(y)
