"""
Python dice roller.

https://github.com/M-Cintron/dice_roller

Bare bones dice roller that allows you to roll any number of dice and get the result, recall the entire roll history of
a given DiceRoller instance, and clear that history.

Usage:
    >>> import dice_roller

    >>> class_instance = DiceRoller()

    >>> class_instance.roll()
    >>> class_instance.roll((1, 10))
    >>> class_instance.roll((3, 5), (2, 4), (1, 100), ...)
    >>> class_instance.history()
    >>> class_instance.clear()
    >>> class_instance.history()
"""
from random import randint


class DiceRoller:
    """
    Objects instantiated by this class can roll any number of dice and recall all the rolls the instance has made.
    """

    def __init__(self):
        # make the instance's records of rolls protected
        self._records = []

    def roll(self, *args):
        """
        Roll any number of dice and return the result

        Note: if no arguments are given to roll(), then it rolls 1, 20 sided die.
        The arguments should be any number of tuples or lists separated by commas.
        Each tuple/list should be formatted as: (<number of dice being rolled>, <num sides of dice>)
        This method returns a tuple formatted as:
        (<roll result>, <min possible roll>, <max possible roll>, <median roll>)
        """
        min_val = 0
        max_val = 0

        # if roll is ran with no parameters, assume we are rolling 1, 20 sided die
        if len(args) == 0:
            args = ((1, 20),)

        for dice_info in args:
            # check that the items in args are either a list or tuple
            if not isinstance(dice_info, (tuple, list)):
                raise TypeError("The arguments must be either lists or tuples")

            # change dice_info into a tuple for convenience
            dice_info = tuple(dice_info)

            # check that the tuples only contain two items
            if len(dice_info) != 2:
                raise TypeError(f"roll expected tuple/list containing 2 items, got {len(dice_info)}")

            num_dice = dice_info[0]
            num_sides = dice_info[1]
            # check that values in the inputted tuples are only integers
            if not isinstance(num_dice, int):
                raise TypeError("The number of dice must be an integer")
            if not isinstance(num_sides, int):
                raise TypeError("The number of sides on the dice must be an integer")

            if num_dice <= 0:
                raise ValueError("Cannot roll zero or negative dice")
            if num_sides <= 0:
                raise ValueError("Cannot roll dice with zero or negative sides")

            min_val += num_dice
            max_val += num_dice * num_sides

        median_val = (min_val + max_val) / 2
        dice_rolled = args

        roll_result = randint(min_val, max_val)
        result = (roll_result, min_val, max_val, median_val)
        self._records.append((dice_rolled, result))
        return result

    def history(self):
        """
        Return a JSON friendly dictionary containing the info for all rolls the current instance of dice_roller has made

        The dictionary created by this method is formatted as follows: the keys are 'Roll_<num>', and the values are
        dictionaries containing the keys: 'Dice', 'Result', 'Min', 'Max', 'Median' with the associated values.
        """

        roll_history = {}
        counter = 0

        for roll_info in self._records:
            result = roll_info[1][0]
            min_roll = roll_info[1][1]
            max_roll = roll_info[1][2]
            median = roll_info[1][3]
            roll_history[f'roll_{counter}'] = {'dice': {}, 'result': result, 'min': min_roll, 'max': max_roll,
                                               'median': median}
            # for every die inputted, add it to the value of the 'dice' key in roll_<current_role>
            dice_counter = 0
            dice = roll_info[0]
            for die in dice:
                num_dice = die[0]
                num_sides = die[1]
                roll_history[f'roll_{counter}']['dice'].update(
                    {f'dice_{dice_counter}': {"number_of_dice": num_dice, "number_of_sides": num_sides}})
                dice_counter += 1

            counter += 1

        return roll_history

    def clear(self):
        """
        Clear the roll history of an instance of dice_roller

        """

        self._records = []
        return "History Cleared!"
