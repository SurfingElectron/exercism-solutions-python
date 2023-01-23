def rotate(text, key):
    '''Applies a simple rotational cipher to text.
    
    Parameters
    text: str
        The text string to be transposed
    key: int
        The shift to be applied

    The cipher is a simple shift cipher that relies on transposing all the
    letters in the alphabet using an integer key between 0 and 26. The letter
    is shifted for as many values as the value of the key.
    '''

    # Create the cipher based on the key
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ALPHABET[key:] + ALPHABET[:key]

    # Create the mapping table
    cipher_map = text.maketrans(ALPHABET + ALPHABET.upper(), cipher + cipher.upper())

    # Translate!
    return text.translate(cipher_map)
    