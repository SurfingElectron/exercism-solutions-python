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

    def is_vowel(text):
        return text.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt'))

    def is_consonant_sound(text):
        return text.startswith(('y', 'ch', 'qu',  'th',  'rh', 'squ', 'sch', 'thr'))

    if is_vowel(text):
        return text + 'ay'
    if is_consonant_sound(text):
        for consonant in ['y', 'ch', 'qu',  'th',  'rh', 'squ', 'sch', 'thr']:
            return 'consonantsound' #text[len(consonant):] + consonant + 'ay'
    else: return text[1:] + text[:1] + 'ay'