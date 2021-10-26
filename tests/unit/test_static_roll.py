"""Unit tests for the static_roll() method"""
import unittest
import random
from dice_roller import DiceRoller


class DiceRollerTests(unittest.TestCase):
    # ignore pylint errors for too many public methods and duplicate code (doesn't work)
    # pylint: disable=R0904, R0801
    """Various tests for the static_roll() method"""

    def test_empty_roll(self):
        """test static_roll() with no arguments rolls 1, 20 sided die"""
        roll = DiceRoller.static_roll()
        # check that the random number is some number between 1 and 20 (inclusive)
        self.assertIn(roll[0], range(1, 20 + 1))
        # check that the min, max, and median values are correct
        self.assertEqual(roll[1:], (1, 20, 10.5))

    def test_3_rolls(self):
        """test static_roll() returns the correct response when rolling 3 different dice"""
        roll = DiceRoller.static_roll((1, 20), (2, 10), (1, 100))
        self.assertIn(roll[0], range(4, 140 + 1))
        self.assertEqual(roll[1:], (4, 140, 72))

    def test_3_rolls_lists(self):
        """test static_roll() returns correct response when rolling dice in lists"""
        roll = DiceRoller.static_roll([1, 20], [2, 10], [1, 100])
        self.assertIn(roll[0], range(4, 140 + 1))
        self.assertEqual(roll[1:], (4, 140, 72))

    def test_10_dice_1_side(self):
        """test test static_roll() returns correct response when rolling 10, 1 sided dice"""
        roll = DiceRoller.static_roll((10, 1))
        self.assertEqual(roll, (10, 10, 10, 10))

    def test_0_dice(self):
        """test static_roll() returns correct error when given 0 dice"""
        with self.assertRaisesRegex(ValueError, 'Cannot roll zero or negative dice'):
            DiceRoller.static_roll((0, 5))

    def test_0_sides(self):
        """test static_roll() returns correct error when given 0 sided dice"""
        with self.assertRaisesRegex(ValueError, 'Cannot roll dice with zero or negative sides'):
            DiceRoller.static_roll((10, 0))

    def test_negative_sides(self):
        """test static_roll() returns correct error when given negative sided dice"""
        with self.assertRaisesRegex(ValueError, 'Cannot roll dice with zero or negative sides'):
            DiceRoller.static_roll((1, -10))

    def test_negative_dice(self):
        """test static_roll() returns correct error when given negative number of dice"""
        with self.assertRaisesRegex(ValueError, 'Cannot roll zero or negative dice'):
            DiceRoller.static_roll((-1, 10))

    def test_dict_input(self):
        """test static_roll() raises correct error when given a dict"""
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            DiceRoller.static_roll({2: 5})

    def test_str_input(self):
        """test static_roll() raises correct error when given a string"""
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            DiceRoller.static_roll('egg')

    def test_set_input(self):
        """test static_roll() raises correct error when given a set"""
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            DiceRoller.static_roll({1, 6})

    def test_float_num_dice(self):
        """test static_roll() raises correct error when given a non-integer number of dice"""
        with self.assertRaisesRegex(TypeError, 'The number of dice must be an integer'):
            DiceRoller.static_roll((1.2, 5))

    def test_float_num_sides(self):
        """
        test static_roll() raises correct error when given dice with a non-integer number of sides
        """
        with self.assertRaisesRegex(
                TypeError, 'The number of sides on the dice must be an integer'):
            DiceRoller.static_roll((3, 1.414))

    def test_excess_values(self):
        """test static_roll() raises correct error when a dice input has more than 2 arguments"""
        with self.assertRaisesRegex(
                TypeError, "dice_roller expected tuple/list containing 2 items, got 3"):
            DiceRoller.static_roll((1, 4, 5))

    def test_missing_values(self):
        """test static_roll() raises correct error when a dice input has less than 2 arguments"""
        with self.assertRaisesRegex(TypeError,
                                    "dice_roller expected tuple/list containing 2 items, got 1"):
            DiceRoller.static_roll([2])

    def test_advantage_works(self):
        """Test advantage is working with no defined die tuple"""
        roll = DiceRoller.static_roll(advantage=True, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 20 + 1))
        self.assertEqual(roll[1:4], (1, 20, 10.5))
        self.assertGreaterEqual(roll[0], roll[4])

    def test_advantage_1_die(self):
        """Test advantage is working with one die tuple"""
        roll = DiceRoller.static_roll((1, 10),
                                      advantage=True, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 10 + 1))
        self.assertEqual(roll[1:4], (1, 10, 5.5))
        self.assertGreaterEqual(roll[0], roll[4])

    def test_advantage_3_dice(self):
        """Test advantage is working with three dice tuple"""
        roll = DiceRoller.static_roll((1, 10), (3, 4), (2, 6),
                                      advantage=True, show_advantage_val=True)
        self.assertIn(roll[0], range(6, 34 + 1))
        self.assertEqual(roll[1:4], (6, 34, 20.0))
        self.assertGreaterEqual(roll[0], roll[4])

    def test_disadvantage_works(self):
        """Test disadvantage is working with no defined die tuple"""
        roll = DiceRoller.static_roll(advantage=False, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 20 + 1))
        self.assertEqual(roll[1:4], (1, 20, 10.5))
        self.assertLessEqual(roll[0], roll[4])

    def test_disadvantage_1_die(self):
        """Test disadvantage is working with one die tuple"""
        roll = DiceRoller.static_roll((1, 6),
                                      advantage=False, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 6 + 1))
        self.assertEqual(roll[1:4], (1, 6, 3.5))
        self.assertLessEqual(roll[0], roll[4])

    def test_disadvantage_3_dice(self):
        """Test disadvantage is working with three dice tuples"""
        roll = DiceRoller.static_roll((2, 4), (1, 12), (1, 2),
                                      advantage=False, show_advantage_val=True)
        self.assertIn(roll[0], range(4, 22 + 1))
        self.assertEqual(roll[1:4], (4, 22, 13.0))
        self.assertLessEqual(roll[0], roll[4])

    def test_advantage_none(self):
        """Make sure DiceRoller still works when advantage=None and show_advantage_val=True"""
        roll = DiceRoller.static_roll(advantage=None, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 20 + 1))
        self.assertEqual(roll[1:], (1, 20, 10.5))

    def test_str_advantage_input(self):
        """Make sure DiceRoller returns an error when advantage is given a str"""
        with self.assertRaisesRegex(
                TypeError, "the advantage argument must be either True, False or None"):
            DiceRoller.static_roll(advantage='True')

    def test_int_advantage_input(self):
        """Make sure DiceRoller returns an error when advantage is given an int"""
        with self.assertRaisesRegex(
                TypeError, "the advantage argument must be either True, False or None"):
            DiceRoller.static_roll(advantage=1)

    def test_str_show_advantage_val_input(self):
        """Make sure DiceRoller returns an error when show_advantage_val is given a str"""
        with self.assertRaisesRegex(
                TypeError, "the show_advantage_val argument must be either True or False"):
            DiceRoller.static_roll(show_advantage_val='True')

    def test_int_show_advantage_val_input(self):
        """Make sure DiceRoller returns an error when show_advantage_val is given an int"""
        with self.assertRaisesRegex(
                TypeError, "the show_advantage_val argument must be either True or False"):
            DiceRoller.static_roll(show_advantage_val=1)

    def test_advantage_off(self):
        """
        Make sure advantage re-rolling is not occurring by checking if the roll result returns the
        expected values.
        """
        random.seed(1)
        vals_0 = roll_1000((2, 5))
        self.assertEqual(vals_0, {'7': 168, '4': 115, '5': 147, '8': 107, '6': 211, '9': 94,
                                  '2': 33, '3': 74, '10': 51})

        vals_1 = roll_1000((1, 10))
        self.assertEqual(vals_1, {'1': 95, '5': 88, '9': 100, '7': 90, '6': 120, '10': 101,
                                  '4': 104, '2': 93, '3': 109, '8': 100})

        vals_2 = roll_1000((1, 2), (2, 4))
        self.assertEqual(vals_2, {'9': 100, '5': 170, '6': 207, '7': 222, '8': 155, '4': 91,
                                  '3': 22, '10': 33})

    def test_advantage_on(self):
        """
        Make sure advantage re-rolling is working properly when given a set random.seed() by
        checking the results with the expected values
        """

        random.seed(0)
        vals_0 = roll_1000(advantage=True)
        self.assertEqual(vals_0, {'14': 74, '9': 45, '17': 84, '13': 71, '16': 91, '19': 82,
                                  '10': 41, '20': 97, '18': 83, '11': 49, '12': 60, '7': 24,
                                  '8': 42, '3': 16, '15': 61, '6': 28, '5': 26, '4': 13, '2': 12,
                                  '1': 1})

        vals_1 = roll_1000((1, 6), advantage=True)
        self.assertEqual(vals_1, {'4': 181, '6': 332, '5': 254, '3': 122, '2': 84, '1': 27})

        vals_2 = roll_1000((1, 4), (2, 8), advantage=True)
        self.assertEqual(vals_2, {'17': 76, '19': 20, '8': 33, '16': 98, '20': 7, '13': 146,
                                  '14': 136, '11': 85, '18': 39, '12': 117, '15': 110, '9': 45,
                                  '10': 71, '6': 4, '7': 11, '5': 2})

    def test_disadvantage_on(self):
        """
        Make sure disadvantage re-rolling is working properly when given a set random.seed() by
        checking the results with the expected values
        """

        random.seed(4)
        vals_0 = roll_1000(advantage=False)
        self.assertEqual(vals_0, {'8': 64, '4': 76, '5': 77, '3': 83, '1': 80, '10': 56, '2': 94,
                                  '17': 20, '9': 58, '7': 70, '6': 96, '11': 45, '14': 25,
                                  '12': 48, '13': 36, '16': 28, '15': 30, '20': 1, '19': 4,
                                  '18': 9})

        vals_1 = roll_1000((1, 8), advantage=False)
        self.assertEqual(vals_1, {'1': 235, '2': 207, '4': 125, '3': 188, '6': 70, '5': 117,
                                  '7': 47, '8': 11})

        vals_2 = roll_1000((1, 3), (1, 10), advantage=False)
        self.assertEqual(vals_2, {'9': 72, '7': 102, '3': 125, '6': 138, '11': 31, '10': 57,
                                  '4': 178, '5': 129, '8': 79, '12': 11, '2': 78})


def roll_1000(*args, advantage=None, show_advantage_val=False):
    """ Roll static_roll() 1000 times with the given inputs and return a dictionary, with the keys
    being the numbers that were rolled and the associated values being how many times a given
    number was rolled
    """

    vals = {}
    for _ in range(1000):
        result = DiceRoller.static_roll(*args, advantage=advantage,
                                        show_advantage_val=show_advantage_val)
        val = result[0]
        if f'{val}' not in vals:
            vals[f'{val}'] = 1
        else:
            vals[f'{val}'] += 1
    return vals
