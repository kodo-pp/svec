"""Module dedicated to points on a plane"""

from svec.common import ScalarType
from svec.vector2d import Vector2d

from typing import Tuple, Union, overload

class Point2d:
    """A point on a 2D plane"""

    __slots__ = ('vec',)

    def __init__(self, vec: Vector2d) -> None:
        """Construct a point with the same coordinates as a specified vector.

        Essentially, it means constructing a point P = O + v, where O = (0, 0)
        and v is the given vector
        """
        self.vec = vec

    def __add__(self, other: 'Vector2d') -> 'Point2d':
        """Return a point offset from this one by a given vector.

        The new point's coordinates will be equal to the elementwise sum of the coordinates
        of this point and the vector.

        Example:
        ```
        p = Point2d(Vector2d(1, 4))
        q = p + Vector2d(3, 4)
        print(q)  # prints 'Point2d(4, 8)'; 4 = 1 + 3, 8 = 4 + 4
        ```
        """
        return Point2d(self.vec + other)

    @overload
    def __sub__(self, other: 'Vector2d') -> 'Point2d':
        ...

    @overload
    def __sub__(self, other: 'Point2d') -> 'Vector2d':
        ...

    def __sub__(self, other: Union['Vector2d', 'Point2d']) -> Union['Vector2d', 'Point2d']:
        """Subtract a vector or another point from this point and return the result.

        If a vector is subtracted, this operation is equivalent to adding -1 times the vector.
        If a point is subtracted, the vector from the subtracted point to this one is returned.
        In both cases the coordinates of the returned point or vector will be equal to the coordinates
        of the current point minus (elementwise) the coordinates of `other`.

        Example:
        ```
        p = Point2d(Vector2d(1, 2))
        q = Point2d(Vector2d(3, 1))
        v = Vector2d(2, 5)

        # Subtract a vector
        print(p - v)  # prints 'Point2d(-1, -3)'; -1 = 1 - 2, -3 = 2 - 5
        # Subtract a point
        print(p - q)  # prints 'Vector2d(-2, 1)'; -2 = 1 - 3, 1 = 2 - 1
        ```
        """
        if isinstance(other, Vector2d):
            return self + (-other)
        return self.vec - other.vec

    def coords(self) -> Tuple[ScalarType, ScalarType]:
        """Return the coordinates of this point as a pair of scalars."""
        return self.vec.coords()

    def ints(self) -> Tuple[int, int]:
        """Return the coordinates of this point rounded using `int()` as a pair of ints."""
        x, y = self.coords()
        return int(x), int(y)

    def __repr__(self) -> str:
        x, y = self.coords()
        return f'Point2d({x}, {y})'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Point2d) and self.vec == other.vec

    def __hash__(self) -> int:
        return hash(('point2d', self.coords())) + 197
