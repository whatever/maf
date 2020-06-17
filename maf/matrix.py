class Vector(object):
    """Represent a Vector"""

    def __init__(self, it):
        self.vec = list(it)

    def __mul__(self, rhs):
        """Matrix/Dot multiplication"""
        n = len(self.vec)

        if n != len(rhs):
            raise "Vector sizes don't match"

        s = 0.0

        for i in range(n):
            s += self.vec[i] * rhs.vec[i]

        return s

    def __len__(self):
        """Return length of vector"""
        return len(self.vec)


class Matrix(object):
    """Represent a matrix"""

    def __init__(self, it):
        pass

    def dims(self):
        pass


def vscale(u, c):
    return [
        c*x
        for x in u
    ]


def vsum(u, v):
    assert len(u) == len(v)
    return [
      x+y
      for x, y in zip(u, v)
    ]


def gradient(f, n):

    h = 0.00001

    def fn(*xs):
        if len(xs) != n:
            raise "LengthMismatch"

        y = []

        for i in range(n):
            v = [0]*n
            v[i] = h
            a = vsum(xs, v)
            b = vsum(xs, vscale(v, -1))
            c = (f(*a) - f(*b)) / 2.0 / h
            y.append(c)

        return y

    return fn


def jacobian(f):

    def fn(*x):
        return 0.0

    return fn
