from random import randint
# TODO: How do I make instance variables and methods private / inaccessible by user?

class DiceRoller:
    """

    """
    def __init__(self):
        self.records = []

    def roll(self):
        min_val = 1
        max_val = 20
        median_val = (min_val + max_val) / 2

        role_result = randint(min_val, max_val)
        result = (role_result, min_val, max_val, median_val)

        self.records.append(result)

        return result

    def history(self):
        return self.records
