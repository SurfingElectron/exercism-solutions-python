def is_armstrong_number(number):
    '''Caluculate if a given number is an Armstrong number.
    An Armstrong number is a number that is the sum of its own 
    digits each raised to the power of the number of digits.

    Parameters
    number: int
        the number being checked   
    '''

    armstrong_check = 0
    digits = [int(x) for x in str(number)]

    for x in digits:
      armstrong_check += x ** len(digits)

    if armstrong_check == number:
        return True
    else:
        return False
