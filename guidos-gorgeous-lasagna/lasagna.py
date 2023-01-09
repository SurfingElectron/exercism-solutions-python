"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# Cookbook's expected timings
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# Functions
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to prepare the lasagne.

    :param prepartion_time: int * the number of layers.
    :return: int * the prepartion time each layer derived from 'PREPARATION_TIME'.

    Function that takes the number of layers in the lasagna as an argument
    returns how many minutes it will take to prepare based on the `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time already spend cooking.

    :param prepartion_time: int * int.
    :return: time to prepare layers + time already spent in the oven

    Function that takes the number of layers and the time spent in the over and
    returns how long has been spent cooking so far.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
