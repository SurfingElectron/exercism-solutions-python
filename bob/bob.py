def response(hey_bob):
    '''Determine how Bob responses to being addressed.

    Parameters
    hey_bob: str
        The phrase Bob will respond to. Always has correct sentence punctuation.

    If asked a question, Bob responds, 'Sure'
    If shouted at (all caps), Bob responds, 'Whoa, chill out!' 
    If asked a shouted question, Bob responds, 'Calm down, I know what I'm doing!'
    If addressed without saying anything, Bob responds, 'Fine. Be that way!' 
    Anything else, Bob responds, 'Whatever.'   
    '''

    # Strip whitespaces and determine if the phrase is a question, and if it is shouted
    hey_bob = hey_bob.strip()
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')

    # Logic to determine response
    if not hey_bob:
        return 'Fine. Be that way!'      
    if is_shout and is_question: 
        return 'Calm down, I know what I\'m doing!'
    if is_question: 
        return 'Sure.'
    if is_shout:
        return  'Whoa, chill out!'
    else:
        return 'Whatever.'
    