from random import randint


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
        (<number of dice being rolled>, <num sides of dice>).
        This method returns a tuple formatted as:
        (<roll result>, <min possible roll>, <max possible roll>, <median roll>)
        """

        min_val = 0
        max_val = 0
        dice_rolled = []

        # if roll is ran with no parameters, assume we are rolling one d20
        if len(args) == 0:
            min_val = 1
            max_val = 20

        # check that the arguments given to .roll() are either a list or tuple
        for dice_info in args:
            if not isinstance(dice_info, (tuple, list)):
                raise TypeError("The arguments must be either lists or tuples")

            # change dice_info into a tuple for consistency when its values get appended to dice_rolled
            dice_info = tuple(dice_info)

            # check that the tuples or lists only contain two items
            if len(dice_info) != 2:
                raise TypeError(f"roll expected tuple(s)/list(s) containing 2 items, got {len(dice_info)}")

            num_dice = dice_info[0]
            num_sides = dice_info[1]
            # check that values in the inputted tuples or lists are only integers
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

            dice_rolled.append(dice_info)

        median_val = (min_val + max_val) / 2

        role_result = randint(min_val, max_val)
        result = (role_result, min_val, max_val, median_val)
        self.records.append((dice_rolled, result))
        return result

    def history(self):
        return self.records

    def _save_results(self):
        # TODO: create a way to export all the roll info in a JSON friendly dict
        pass


if __name__ == '__main__':
    roll_instance = DiceRoller()
    print(roll_instance.roll((1, 20), (2, 10), (1, 100)))
    print(roll_instance.roll([1, 20], [2, 10], [1, 100]))
    print(roll_instance.history())
