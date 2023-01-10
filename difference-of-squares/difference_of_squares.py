def square_of_sum(number):
    '''Calculate the square of the sum.

    The formula to sum n natural numbers can be calculated using the
    formula n(n+1)/2 
    '''
    return (number * (number +1) / 2) ** 2

def sum_of_squares(number):
    '''Calculate the sum of the squares.

    The formula for the sum of squares of n natural numbers can be
    calculated using the formula (n(n+1)(2n+1))/6
    '''
    return (number * (number + 1) * (2 * number + 1)) / 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
