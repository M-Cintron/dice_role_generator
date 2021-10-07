"""Unit tests for static_roll() method"""
import unittest
from dice_roller import DiceRoller


class DiceRollerTests(unittest.TestCase):

    # test static_roll() with no arguments rolls 1, 20 sided die
    def test_empty_roll(self):
        roll_0 = DiceRoller.static_roll()
        # check that the random number is some number between 1 and 20 (inclusive)
        self.assertIn(roll_0[0], range(1, 20+1))
        # check that the min, max, and median values are correct
        self.assertEqual(roll_0[1:], (1, 20, 10.5))

    # test static_roll() returns the correct response when rolling 3 different dice
    def test_3_rolls(self):
        roll_1 = DiceRoller.static_roll((1, 20), (2, 10), (1, 100))
        self.assertIn(roll_1[0], range(4, 140+1))
        self.assertEqual(roll_1[1:], (4, 140, 72))

    # test static_roll() returns correct response when rolling dice in lists
    def test_3_rolls_lists(self):
        roll_2 = DiceRoller.static_roll([1, 20], [2, 10], [1, 100])
        self.assertIn(roll_2[0], range(4, 140+1))
        self.assertEqual(roll_2[1:], (4, 140, 72))

    # test test static_roll() returns correct response when rolling 10, 1 sided dice
    def test_10_dice_1_side(self):
        roll_3 = DiceRoller.static_roll((10, 1))
        self.assertEqual(roll_3, (10, 10, 10, 10))

    # test static_roll() returns correct error when given 0 dice
    def test_0_dice(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll zero or negative dice'):
            DiceRoller.static_roll((0, 5))

    # test static_roll() returns correct error when given 0 sided dice
    def test_0_sides(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll dice with zero or negative sides'):
            DiceRoller.static_roll((10, 0))

    # test static_roll() returns correct error when given negative sided dice
    def test_negative_sides(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll dice with zero or negative sides'):
            DiceRoller.static_roll((1, -10))

    # test static_roll() returns correct error when given negative number of dice
    def test_negative_dice(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll zero or negative dice'):
            DiceRoller.static_roll((-1, 10))

    # test static_roll() raises correct error when given a dict
    def test_dict_input(self):
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            DiceRoller.static_roll({2: 5})

    # test static_roll() raises correct error when given a string
    def test_str_input(self):
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            DiceRoller.static_roll('egg')

    # test static_roll() raises correct error when given a set
    def test_set_input(self):
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            DiceRoller.static_roll({1, 6})

    # test static_roll() raises correct error when given a non-integer number of dice
    def test_float_num_dice(self):
        with self.assertRaisesRegex(TypeError, 'The number of dice must be an integer'):
            DiceRoller.static_roll((1.2, 5))

    # test static_roll() raises correct error when given dice with a non-integer number of sides
    def test_float_num_sides(self):
        with self.assertRaisesRegex(TypeError, 'The number of sides on the dice must be an integer'):
            DiceRoller.static_roll((3, 1.414))

    # test static_roll() raises correct error when a dice input has more than 2 arguments
    def test_excess_values(self):
        with self.assertRaisesRegex(TypeError, "dice_roller expected tuple/list containing 2 items, got 3"):
            DiceRoller.static_roll((1, 4, 5))

    # test static_roll() raises correct error when a dice input has less than 2 arguments
    def test_missing_values(self):
        with self.assertRaisesRegex(TypeError,
                                    "dice_roller expected tuple/list containing 2 items, got 1"):
            DiceRoller.static_roll([2])
