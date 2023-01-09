def steps(number):
    """Calculate the number of steps in the Collatz Conjecture.
 
    :param number: int - must be a positive integer
 
    Given a number n, do the following:
    - If n is even, divide n by 2 (n / 2)
    - If n is odd, multiply n by 3 and add 1 (3n + 1)
    - Repeat and until n = 1
    - Return the number of steps to get there.
    """

    # Raising an exception if the number is 0 or negative
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    # Setting the number of iterations to 0
    i = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            i += 1
        else:
            number = 3 * number + 1
            i += 1
    return i
