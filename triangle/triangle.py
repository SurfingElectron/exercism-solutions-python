def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and is_triangle(sides)

def isosceles(sides):
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and is_triangle(sides) 

def scalene(sides):
    return sides[0] != sides[1] != sides[2] and sides[0] != sides[2] and is_triangle(sides)

def is_triangle(sides):
    '''Checks if we have a valid triangle.

    Parameters
    sides: array of int or float
        The length of the triangle sides
    '''
    
    return (sides.count(0) == 0
        and sides[0] + sides[1] >= sides[2] 
        and sides[1] + sides[2] >= sides[0] 
        and sides[0] + sides[2] >= sides[1])
