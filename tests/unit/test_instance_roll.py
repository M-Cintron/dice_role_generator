"""Unit tests for the static roll() method"""
import unittest
import dice_roller

dice_roller_instance = dice_roller.DiceRoller()


class DiceRollerTests(unittest.TestCase):

    # test .roll() with no arguments rolls 1, 20 sided die
    def test_empty_roll(self):
        roll = dice_roller_instance.roll()
        # check that the random number is some number between 1 and 20 (inclusive)
        self.assertIn(roll[0], range(1, 20+1))
        # check that the min, max, and median values are correct
        self.assertEqual(roll[1:], (1, 20, 10.5))

    # test .roll() returns the correct response when rolling 3 different dice
    def test_3_rolls(self):
        roll = dice_roller_instance.roll((1, 20), (2, 10), (1, 100))
        self.assertIn(roll[0], range(4, 140+1))
        self.assertEqual(roll[1:], (4, 140, 72))

    # test .roll() returns correct response when rolling dice in lists
    def test_3_rolls_lists(self):
        roll = dice_roller_instance.roll([1, 20], [2, 10], [1, 100])
        self.assertIn(roll[0], range(4, 140+1))
        self.assertEqual(roll[1:], (4, 140, 72))

    # test test .roll() returns correct response when rolling 10, 1 sided dice
    def test_10_dice_1_side(self):
        roll = dice_roller_instance.roll((10, 1))
        self.assertEqual(roll, (10, 10, 10, 10))

    # test .roll() returns correct error when given 0 dice
    def test_0_dice(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll zero or negative dice'):
            dice_roller_instance.roll((0, 5))

    # test .roll() returns correct error when given 0 sided dice
    def test_0_sides(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll dice with zero or negative sides'):
            dice_roller_instance.roll((10, 0))

    # test .roll() returns correct error when given negative sided dice
    def test_negative_sides(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll dice with zero or negative sides'):
            dice_roller_instance.roll((1, -10))

    # test .roll() returns correct error when given negative number of dice
    def test_negative_dice(self):
        with self.assertRaisesRegex(ValueError, 'Cannot roll zero or negative dice'):
            dice_roller_instance.roll((-1, 10))

    # test .roll() raises correct error when given a dict
    def test_dict_input(self):
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            dice_roller_instance.roll({2: 5})

    # test .roll() raises correct error when given a string
    def test_str_input(self):
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            dice_roller_instance.roll('egg')

    # test .roll() raises correct error when given a set
    def test_set_input(self):
        with self.assertRaisesRegex(TypeError, 'The arguments must be either lists or tuples'):
            dice_roller_instance.roll({1, 6})

    # test .roll() raises correct error when given a non-integer number of dice
    def test_float_num_dice(self):
        with self.assertRaisesRegex(TypeError, 'The number of dice must be an integer'):
            dice_roller_instance.roll((1.2, 5))

    # test .roll() raises correct error when given dice with a non-integer number of sides
    def test_float_num_sides(self):
        with self.assertRaisesRegex(TypeError, 'The number of sides on the dice must be an integer'):
            dice_roller_instance.roll((3, 1.414))

    # test .roll() raises correct error when a dice input has more than 2 arguments
    def test_excess_values(self):
        with self.assertRaisesRegex(TypeError, "dice_roller expected tuple/list containing 2 items, got 3"):
            dice_roller_instance.roll((1, 4, 5))

    # test .roll() raises correct error when a dice input has less than 2 arguments
    def test_missing_values(self):
        with self.assertRaisesRegex(TypeError,
                                    "dice_roller expected tuple/list containing 2 items, got 1"):
            dice_roller_instance.roll([2])

    def test_advantage_works(self):
        roll = dice_roller_instance.roll(advantage=True, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 20+1))
        self.assertEqual(roll[1:4], (1, 20, 10.5))
        self.assertGreaterEqual(roll[0], roll[4])

    def test_advantage_1_die(self):
        roll = dice_roller_instance.roll((1, 10), advantage=True, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 10 + 1))
        self.assertEqual(roll[1:4], (1, 10, 5.5))
        self.assertGreaterEqual(roll[0], roll[4])

    def test_advantage_3_dice(self):
        roll = dice_roller_instance.roll((1, 10), (3, 4), (2, 6), advantage=True, show_advantage_val=True)
        self.assertIn(roll[0], range(6, 34 + 1))
        self.assertEqual(roll[1:4], (6, 34, 20.0))
        self.assertGreaterEqual(roll[0], roll[4])

    def test_disadvantage_works(self):
        roll = dice_roller_instance.roll(advantage=False, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 20+1))
        self.assertEqual(roll[1:4], (1, 20, 10.5))
        self.assertLessEqual(roll[0], roll[4])

    def test_disadvantage_1_die(self):
        roll = dice_roller_instance.roll((1, 6), advantage=False, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 6 + 1))
        self.assertEqual(roll[1:4], (1, 6, 3.5))
        self.assertLessEqual(roll[0], roll[4])

    def test_disadvantage_3_dice(self):
        roll = dice_roller_instance.roll((2, 4), (1, 12), (1, 2), advantage=False, show_advantage_val=True)
        self.assertIn(roll[0], range(4, 22 + 1))
        self.assertEqual(roll[1:4], (4, 22, 13.0))
        self.assertLessEqual(roll[0], roll[4])

    def test_advantage_None(self):
        roll = dice_roller_instance.roll(advantage=None, show_advantage_val=True)
        self.assertIn(roll[0], range(1, 20+1))
        self.assertEqual(roll[1:], (1, 20, 10.5))

    def test_str_advantage_input(self):
        with self.assertRaisesRegex(TypeError, "the advantage argument must be either True, False or None"):
            dice_roller_instance.roll(advantage='True')

    def test_int_advantage_input(self):
        with self.assertRaisesRegex(TypeError, "the advantage argument must be either True, False or None"):
            dice_roller_instance.roll(advantage=1)

    def test_str_show_advantage_val_input(self):
        with self.assertRaisesRegex(TypeError, "the show_advantage_val argument must be either True or False"):
            dice_roller_instance.roll(show_advantage_val='True')

    def test_int_show_advantage_val_input(self):
        with self.assertRaisesRegex(TypeError, "the show_advantage_val argument must be either True or False"):
            dice_roller_instance.roll(show_advantage_val=1)