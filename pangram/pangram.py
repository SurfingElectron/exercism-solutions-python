def is_pangram(sentence):
    '''Checks if a sentence is a panagram (i.e. contains every letter of the alphabet).

    Parameters
    sentence: str
        The sentence being checked for panagraminess! 
    '''
    
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    for letter in ALPHABET: 
        if letter not in sentence.lower():
            return False
    return True
