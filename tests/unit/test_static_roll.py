"""Unit tests for the static_roll() method"""
import unittest
from dice_roller import DiceRoller


class DiceRollerTests(unittest.TestCase):
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
        """test static_roll() raises correct error when given dice with a non-integer number of sides"""
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
