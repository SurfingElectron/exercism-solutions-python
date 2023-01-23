def is_valid(isbn):
    '''Checks if a given string is a valid ISBN code.

    Parameters
    isbn: str
        A 9 digit (plus 1 check character) string

    Validity for ISBN can be checked using the following formula:
    (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    '''

    # Remove any hyphens from the input, convert to a list
    clean_isbn = list(isbn.replace('-',''))

    # Check the code is the correct length
    if len(clean_isbn) != 10:
        return False

    # Change the check digit to 10 if it's an X, and confirm only digits left
    if clean_isbn[-1] == 'X':
        clean_isbn[-1] = '10'
    if not all([n.isdigit() for n in clean_isbn]):
       return False

    # Covert list to intergers, and check if a valid ISBN using the formula
    isbn_check = list(map(int, clean_isbn))
    return sum(n * (10 - i) for i, n in enumerate(isbn_check)) % 11 == 0
