import math

def score(x, y):
    '''Calculates the score in a single darts throw.

    Parameters
    x, y: int
        Cartesian coordinates of the dart strike.

    Scoring:
    0: Outside the target
    1: Outer circle (radius 10)
    5: Middle circle (radius 5)
    10: Inner circle (radius 1)
    '''

    dart_radius = math.sqrt(x**2 + y**2)

    if dart_radius <= 1:
        return 10
    if dart_radius <= 5:
        return 5
    if dart_radius <= 10:
        return 1
    return 0
