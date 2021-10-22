"""
Python dice roller.

https://github.com/M-Cintron/dice_roller

Bare bones dice roller that allows you to create a class that can roll any number of dice and get
the result, recall the entire roll history of a given DiceRoller instance, and clear that history.
Or just roll some dice without creating a class instance.  DiceRoller can also perform
advantage/disadvantage rolling and can show the number thrown out due to advantage/disadvantage.

Usage:
>>> import dice_roller

>>> class_instance = dice_roller.DiceRoller()

>>> print(class_instance.roll())
>>> print(class_instance.roll((1, 10), advantage=True), show_advantage_val=True)
>>> print(class_instance.roll((3, 5), (2, 4), (1, 100), (4, 6)))
>>> print(class_instance.history())
>>> class_instance.clear()
>>> print(class_instance.history())

OR:
>>> from dice_roller import DiceRoller

>>> print(DiceRoller.static_roll())
>>> print(DiceRoller.static_roll((1, 4), (2, 6), advantage=False))
>>> print(DiceRoller.static_roll((7, 2), (1, 8), (1, 12), advantage=False, show_advantage_val=True))

"""
from random import randint


class DiceRoller:
    """
    Objects instantiated by this class can roll any number of dice and recall all the rolls the
    instance has made.
    """

    def __init__(self):
        # make the instance's records of rolls protected
        self._records = []

    def roll(self, *args, advantage=None, show_advantage_val=False):
        """
        Roll any number of dice, return and the dice rolled and the result.

        If no arguments are given to roll(), then it rolls 1, 20 sided die.
        The arguments should be any number of tuples or lists separated by commas.
        Each tuple/list should be formatted as: (<number of dice being rolled>,
                                                 <num sides of dice>)

        By default, this method returns a tuple formatted as:
        (<roll result>, <min possible roll>, <max possible roll>, <median roll>)

        This method accepts two keyword arguments: advantage and show_advantage_val.  By default
        advantage is set to None.  If advantage is set to True, then DiceRoller will perform two
        rolls with the same dice and return the higher value as the roll result.  If advantage is
        set to False, then DiceRoller will perform two rolls with the same dice and return the
        lower value as the roll result. By default show_advantage_val is set to False.  If
        advantage is either True or False and show_advantage_val is set to True, then this
        method returns a tuple formatted as (thrown out val is the number that
        advantage/disadvantage didn't select):
        (<roll result>, <min possible roll>, <max possible roll>, <median roll>, <thrown out val>)

        This method also stores the dice rolled and the result of said roll which can be accessed
        with the history() method (Note: the thrown out advantage val is NOT recorded)
        """

        dice_rolled, result = self._calculate_roll(*args, advantage=advantage,
                                                   show_advantage_val=show_advantage_val)
        self._records.append((dice_rolled, result))
        return result

    @staticmethod
    def static_roll(*args, advantage=None, show_advantage_val=False):
        """
        Roll any number of dice, and return the result.

        Note: if no arguments are given to static_roll(), then it rolls 1, 20 sided die.
        The arguments should be any number of tuples or lists separated by commas.
        Each tuple/list should be formatted as: (<number of dice being rolled>,
                                                 <num sides of dice>)

        By default, this method returns a tuple formatted as:
        (<roll result>, <min possible roll>, <max possible roll>, <median roll>)

        This method accepts two keyword arguments: advantage and show_advantage_val.  By default
        advantage is set to None.  If advantage is set to True, then DiceRoller will perform two
        rolls with the same dice and return the higher value as the roll result.  If advantage is
        set to False, then DiceRoller will perform two rolls with the same dice and return the
        lower value as the roll result. By default show_advantage_val is set to False.  If
        advantage is either True or False and show_advantage_val is set to True, then this
        method returns a tuple formatted as (thrown out val is the number that
        advantage/disadvantage didn't select):
        (<roll result>, <min possible roll>, <max possible roll>, <median roll>, <thrown out val>)
        """
        result = DiceRoller._calculate_roll(*args, advantage=advantage,
                                            show_advantage_val=show_advantage_val)[1]
        return result

    def history(self):
        """
        Return a JSON friendly dictionary containing the info for all rolls the current instance
        of dice_roller has made

        The dictionary created by this method is formatted as follows: the keys are 'Roll_<num>'
        and the values are dictionaries containing the keys: 'Dice', 'Result', 'Min', 'Max',
        'Median' with the associated values.
        """

        roll_history = {}
        counter = 0

        for roll_info in self._records:
            result = roll_info[1][0]
            min_roll = roll_info[1][1]
            max_roll = roll_info[1][2]
            median = roll_info[1][3]
            roll_history[f'roll_{counter}'] = {'dice': {}, 'result': result, 'min': min_roll,
                                               'max': max_roll, 'median': median}
            # for every die inputted, add it to the value of the 'dice' key in roll_<current_roll>
            dice_counter = 0
            dice = roll_info[0]
            for die in dice:
                num_dice = die[0]
                num_sides = die[1]
                roll_history[f'roll_{counter}']['dice'].update(
                    {f'dice_{dice_counter}': {"number_of_dice": num_dice,
                                              "number_of_sides": num_sides}})
                dice_counter += 1

            counter += 1

        return roll_history

    def clear(self):
        """
        Clear the roll history of an instance of dice_roller

        """

        self._records = []
        return "History Cleared!"

    @staticmethod
    def _calculate_roll(*args, advantage=None, show_advantage_val=False):
        """
        The method that performs the roll logic for roll() and static_roll()
        Roll any number of dice, return and the dice rolled and the result.

        If no arguments are given to _calculate_roll(), then it rolls 1, 20 sided die.
        The arguments should be any number of tuples or lists separated by commas.
        Each tuple/list should be formatted as: (<number of dice being rolled>, <num sides of dice>)

        By default, this method returns a tuple formatted as:
        ((<dice rolled>), (<roll result>, <min possible roll>, <max possible roll>, <median roll>))

        This method accepts two keyword arguments: advantage and show_advantage_val.  By default
        advantage is set to None.  If advantage is set to True, then DiceRoller will perform two
        rolls with the same dice and return the higher value as the roll result.  If advantage is
        set to False, then DiceRoller will perform two rolls with the same dice and return the
        lower value as the roll result. By default show_advantage_val is set to False.  If
        advantage is either True or False and show_advantage_val is set to True, then this
        method returns a tuple formatted as (thrown out val is the number that
        advantage/disadvantage didn't select):
        ((<dice rolled>), (<roll result>, <min possible roll>, <max possible roll>, <median roll>,
         <thrown out val>))
        """

        # check that all the arguments given are valid for this method
        DiceRoller._check_types(*args, advantage=advantage, show_advantage_val=show_advantage_val)

        # if _calculate_roll() is ran with no parameters, assume we are rolling 1, 20 sided die
        if len(args) == 0:
            args = ((1, 20),)

        # calculate the min and max possible roll values
        min_val = 0
        max_val = 0
        for dice_tuple in args:
            min_val += dice_tuple[0]
            max_val += dice_tuple[0] * dice_tuple[1]

        # check if advantage is True or False, then perform the appropriate roll
        if advantage:
            advantage_rolls = DiceRoller._advantage_rolling(*args)
            lower_val = advantage_rolls[0]
            higher_val = advantage_rolls[1]
            roll_result = higher_val
        elif not advantage:
            advantage_rolls = DiceRoller._advantage_rolling(*args)
            lower_val = advantage_rolls[0]
            higher_val = advantage_rolls[1]
            roll_result = lower_val
        else:
            roll_result = DiceRoller._get_roll_results(*args)

        median_val = (min_val + max_val) / 2
        result = (roll_result, min_val, max_val, median_val)
        # append the thrown away advantage value to result if show_advantage_val is true
        if show_advantage_val is True and advantage is True:
            result += (lower_val,)
        elif show_advantage_val is True and advantage is False:
            result += (higher_val,)

        dice_rolled = args
        return dice_rolled, result

    @staticmethod
    def _get_roll_results(*args):
        """
        Method that calculates the actual roll results for _calculate_roll()
        """

        roll_result = 0
        # go through every dice tuple
        for dice_info in args:
            # change dice_info into a tuple for convenience
            dice_info = tuple(dice_info)

            num_dice = dice_info[0]
            num_sides = dice_info[1]

            for _ in range(num_dice):
                # roll each die, and add the result to roll_result
                roll_result += randint(1, num_sides)

        return roll_result

    @staticmethod
    def _advantage_rolling(*args):
        """
        Generate two random numbers from the same dice, and return them in a sorted list

        The first number in advantage_rolls is the smaller number and the second number is the
        larger number.
        """

        roll_0 = DiceRoller._get_roll_results(*args)
        roll_1 = DiceRoller._get_roll_results(*args)
        advantage_rolls = [roll_0, roll_1]
        advantage_rolls.sort()
        return advantage_rolls

    @staticmethod
    def _check_types(*args, advantage=None, show_advantage_val=False):
        """
        Go through all the arguments given to _calculate_roll() and check that they're the correct
        data types.  Raise appropriate error if not.
        """

        # check if advantage is either True, False or None, if not then raise error
        if advantage is not True and advantage is not False and advantage is not None:
            raise TypeError('the advantage argument must be either True, False or None')

        # check if show_advantage_val is either True or False, if not then raise error
        if show_advantage_val is not True and show_advantage_val is not False:
            raise TypeError('the show_advantage_val argument must be either True or False')

        for dice_info in args:
            # check that the items in args are either a list or tuple
            if not isinstance(dice_info, (tuple, list)):
                raise TypeError("The arguments must be either lists or tuples")

            # check that the tuples only contain two items
            if len(dice_info) != 2:
                raise TypeError(f"dice_roller expected tuple/list containing 2 items, "
                                f"got {len(dice_info)}")

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
