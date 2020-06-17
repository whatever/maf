#!/usr/bin/env python3


import unittest


from math import sin, cos

from maf import (
    Vector,
    gradient,
    jacobian,
)


class MatrixTest(unittest.TestCase):
    def test_dot(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([0, 1, 0, 1])
        self.assertEqual(a*a, 1+4+9+16)
        self.assertEqual(a*b, 2+4)

    def test_matrix(self):
        pass


class MathTestCase(unittest.TestCase):

    @staticmethod
    def _norm(u):
        return sum(
          x*x
          for x in u
        )

    @staticmethod
    def _sub(u, v):
        assert len(u) == len(v)
        return [
            a-b
            for a, b in zip(u, v)
        ]

    def assertClose(self, u, v, d=0.00001):
        assert self._norm(self._sub(u, v)) < d



class JacobianTest(MathTestCase):

    def test_gradient(self):

        f = lambda x, y: x*y
        g = gradient(f, n=2)

        self.assertEqual(
            g(0.0, 2.0),
            [2.0, 0.0],
        )

        f = lambda x, y: 2*x
        g = gradient(f, n=2)

        self.assertClose(
            g(2.0, 2.0),
            [2.0, 0.0],
        )

        self.assertClose(
            g(2000.0, 2.0),
            [2.0, 0.0],
        )

        f = lambda x, y: cos(2*x) + y**2
        fx = lambda x, y: -2*sin(2*x)
        fy = lambda x, y: 2*y
        g = gradient(f, n=2)

        u = [1.0, -0.3]

        self.assertClose(
          g(*u),
          [fx(*u), fy(*u)]
        )




if __name__ == "__main__":
    unittest.main()
