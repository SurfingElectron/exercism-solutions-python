def is_isogram(string):
    '''Checks if a given string is an isogram (i.e. no repeated letters).
    
    Parameters
    string: str
        The string being checked for isograminess!
    '''

    clean_string = string.replace('-','').replace(' ','').lower()

    for letter in clean_string:
        if clean_string.count(letter) > 1:
            return False
    return True
