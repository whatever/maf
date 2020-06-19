import math
import unittest

from maf.reals import (
    realmap,
    Vec,
)


from .helpers import MafTestCase


class TestVec(MafTestCase):
    def test_what(self):
        u = Vec([1.0, 3.0])
        v = Vec([1.0, 3.0, 10.0])
        x = Vec([-3.0, 4.0])

        self.assertEqual(len(u), 2)
        self.assertEqual(len(v), 3)

        self.assertEqual(u[0], 1.0)
        self.assertEqual(u[1], 3.0)
        self.assertEqual(v[1], 3.0)
        self.assertEqual(v[2], 10.0)

        self.assertEqual(x.norm(), 5.0)
        self.assertEqual(v.norm(), math.sqrt(1+9+100))

        self.assertVecClose(
            u*3,
            Vec([3.0, 9.0]),
        )

        self.assertVecClose(
            u+x,
            Vec([-2.0, 7.0]),
        )

        self.assertVecClose(
            u-x,
            Vec([4.0, -1.0]),
        )

        self.assertEqual(
            u*x,
            -3.0 + 12.0,
        )



class TestReals(MafTestCase):
    def test_simple(self):

        @realmap(3)
        def f(x):
            return [0.0, 0.0, 0.0]

        self.assertClose(
            f([1, 2, 3]),
            [0.0, 0.0, 0.0],
        )

if __name__ == "__main__":
    unittest.main()
