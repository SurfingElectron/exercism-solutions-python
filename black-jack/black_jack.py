"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

# Define what a ten card is for use in functions.
TEN_CARDS = ('10', 'J', 'Q', 'K')

def value_of_card(card):
    """Determines the scoring value of a card.

    Parameters
    card: str
        Card whose scoring value is to be determined.
    Return
    int
        The value of the card
    """

    if card == 'A':
        return 1
    if card in TEN_CARDS:
        return 10
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters
    card_one, card_two: str
        Cards to be compared.
    Return
    str or tuple
        Resulting Tuple contains both cards if they are of equal value.
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    Parameters
    card_one, card_two: str
        Cards to be compared.
    Return
    int
        Either 1 or 11 value of the upcoming ace card.
    """

    if card_one == 'A' or card_two == 'A':
        return 1
    if value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters
    card_one, card_two: str
        Cards to be compared.
    Return
    bool
        Is the hand is a blackjack (two cards worth 21)?
    """

    return (card_one in TEN_CARDS or card_two in TEN_CARDS) and (card_one == 'A' or card_two == 'A')


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

 Parameters
    card_one, card_two: str
        Cards to be compared.
    Return
    bool
        Can the hand be split into two pairs (i.e. cards are of the same value)?
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    card_one, card_two: str
        Cards to be compared.
    Return
    bool
        Can the hand can be doubled down (i.e. totals 9, 10 or 11 points)?
    """

    return (value_of_card(card_one) + value_of_card(card_two) > 8) and (value_of_card(card_one) + value_of_card(card_two) < 12)
