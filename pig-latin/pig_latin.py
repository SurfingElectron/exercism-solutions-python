def translate(text):
    '''Converts a phrase from English to Pig Latin using a small set of rules.

    Parameters
    text: str
        The phrase to be converted into Pig Latin.

    Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. 
        - Note: "xr" and "yt" at the beginning of a word make vowel sounds;
    Rule 2: If a word begins with a consonant sound, move it to the end of the word and 
        then add an "ay" sound to the end of the word;
    Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end 
        of the word, and then add an "ay" sound to the end of the word;
    Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in 
        a two letter word it makes a vowel sound. 
    '''

    def translate_word(word):
        if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
            return word + 'ay'
        for consonant_sound in ['sch', 'squ', 'thr', 'ch', 'qu', 'rh', 'th', 'y']:
            if word.startswith(consonant_sound):
                return word[len(consonant_sound):] + consonant_sound + 'ay'
        return word[1:] + word[:1] + 'ay'

    return ' '.join( [ translate_word(text) for text in text.split() ])