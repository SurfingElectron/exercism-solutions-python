def square(number):
    """Show how many grains are on a given square.
    
    param number: int - a square on the chessboard

    There are 64 squares on a chessboard, each one has double
    the number of grains previous. Given a square, output the
    number of grains on it.
    """

    # when the square value is not in the acceptable range
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return  2 ** (number - 1)

def total():
    """Calculate the total amount of grains on the chessboard.
    """

    return (2 ** 64) - 1
    