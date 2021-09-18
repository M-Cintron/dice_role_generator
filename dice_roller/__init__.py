from random import randint
# TODO: How do I make instance variables and methods private / inaccessible by user?

class DiceRoller:
    """
    Objects instantiated by this class can roll any number of dice and recall all the rolls the instance has made.
    """

    def __init__(self):
        self.records = []

    def roll(self, *args):
        """
        Roll any number of dice and return the result

        Note: if no arguments are given to roll(), then it rolls 1, 20 sided die.
        The arguments should be any number of tuples or lists separated by commas, formatted as:
        (<number of dice being rolled>, <num sides of dice>)
        """

        min_val = 0
        max_val = 0

        # if roll is ran with no parameters, assume we are rolling one d20
        if len(args) == 0:
            min_val = 1
            max_val = 20

        for dice_info in args:
            if not isinstance(dice_info, (tuple, list)):
                raise TypeError("The arguments must be either lists or tuples")

            num_dice = dice_info[0]
            num_sides = dice_info[1]
            if not isinstance(num_dice, int):
                raise TypeError("The number of dice must be an integer")
            if not isinstance(num_sides, int):
                raise TypeError("The number of sides on the dice must be an integer")

            if num_dice <= 0:
                raise ValueError("Cannot role zero or negative dice")
            if num_sides <= 0:
                raise ValueError("Cannot role dice with zero or negative sides")

            min_val += num_dice
            max_val += num_dice * num_sides

        median_val = (min_val + max_val) / 2

        role_result = randint(min_val, max_val)
        result = (role_result, min_val, max_val, median_val)
        self.records.append(result)
        return result

    def history(self):
        return self.records


if __name__ == '__main__':
    roll_instance = DiceRoller()
    print(roll_instance.roll((1, 20), (2, 10), (1, 100)))
    print(roll_instance.roll([1, 20], [2, 10], [1, 100]))

