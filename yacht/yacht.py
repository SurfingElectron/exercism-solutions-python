# Score categories.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: numbers_score(1, dice)
TWOS = lambda dice: numbers_score(2, dice)
THREES = lambda dice: numbers_score(3, dice)
FOURS = lambda dice: numbers_score(4, dice)
FIVES = lambda dice: numbers_score(5, dice)
SIXES = lambda dice: numbers_score(6, dice)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and any(dice.count(x) == 3 for x in dice) else 0
FOUR_OF_A_KIND = 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2,3,4,5,6] else 0
CHOICE = lambda dice: sum(dice)

def numbers_score(number, dice):
    '''Calculates the points value for number categories (e.g. "ones", "fours", etc) 

    Parameters
    number: num
        The number being scored
    dice: array of num
        Five values each ranging between 1-6 (inclusive).

    The score is number * how often that number appears in the roll.
    e.g. number = 2 and dice = [2 2 2 4 5] - output is 6 (2 * 3)
    If the dice do not satisfy the requirements of a category, the score is 0. 
    '''

    return number * dice.count(number)


def score(dice, category):
    '''Outputs the score for a dice roll in Yacht.

    Parameters
    dice: array of num
        The roll, five values each ranging between 1-6 (inclusive).
    category: str
        The scoring categories as defined above.

    If the dice do not satisfy the requirements of a category, the score is 0. 
    '''

    return category(dice)
