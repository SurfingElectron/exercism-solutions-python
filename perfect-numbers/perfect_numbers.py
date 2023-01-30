def classify(number):
    """Determines if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

    Parameters
    number: int
        A positive integer
    Return
    str
        The classification of the input integer
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_check = 0
    
    for i in range(1, number):
        if number % i == 0:
            aliquot_check += i
    
    if aliquot_check == number:
        return 'perfect'
    if aliquot_check > number:
        return 'abundant'
    return 'deficient'