import math


class Vec(object):
    def __init__(self, xs):
        self.xs = list(xs)

    def __len__(self):
        return len(self.xs)


    def __getitem__(self, i):
        return self.xs[i]

    def __setitem__(self, i, v):
        self.xs[i] = v
        return self.xs[i]

    def norm(self):
        return math.sqrt(sum(
            x**2
            for x in self.xs
        ))

    def __repr__(self):
        return "[{}]".format(", ".join(
            str(x)
            for x in self.xs
        ))

    def __mul__(self, c):
        if isinstance(c, Vec):
            assert len(self) == len(c)
            return sum(
                x*y
                for x, y in zip(self.xs, c.xs)
            )

        return Vec(c*x for x in self.xs)
        

    def __add__(self, rhs):
        assert len(self) == len(rhs)
        return Vec(
            x+y
            for x, y in zip(self.xs, rhs.xs)
        )

    def __sub__(self, rhs):
        return self+rhs*-1




def realmap(n):

    def decorator(f):
        
        def fn(xs):
            assert len(xs) == n
            return [0]*n
        
        return fn

    return decorator
