import unittest


class MafTestCase(unittest.TestCase):

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

    def assertVecClose(self, u, v, d=0.00001):
        assert (u-v).norm() < d, f"{u} != {v}"
